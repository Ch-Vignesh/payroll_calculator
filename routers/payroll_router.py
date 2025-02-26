from fastapi import APIRouter, HTTPException
from models.payroll import PayrollInput, PayrollOutput
from services.payroll_service import calculate_payroll
from services.database_service import (
    create_payroll,
    retrieve_payroll,
    retrieve_payrolls,
    update_payroll,
    delete_payroll,
)

router = APIRouter()

# Endpoint for payroll calculation without saving to DB
# @router.post("/calculate_salary", response_model=PayrollOutput)
# async def calculate_salary_endpoint(data: PayrollInput):
#     result = calculate_payroll(data)
#     return result

# Endpoint to calculate payroll and save it to MongoDB
@router.post("/payrolls", response_model=PayrollOutput)
async def create_payroll_endpoint(data: PayrollInput):
    payroll_result = calculate_payroll(data)
    payroll_dict = payroll_result.model_dump()
    new_payroll = await create_payroll(payroll_dict)
    return new_payroll

# Get a single payroll record by its id
@router.get("/payrolls/{payroll_id}")
async def get_payroll(payroll_id: str):
    payroll = await retrieve_payroll(payroll_id)
    if payroll:
        return payroll
    raise HTTPException(status_code=404, detail="Payroll not found")

# Get all payroll records
@router.get("/payrolls")
async def get_payrolls():
    payrolls = await retrieve_payrolls()
    return payrolls

# # Update a payroll record by id
# @router.put("/payrolls/{payroll_id}")
# async def update_payroll_endpoint(payroll_id: str, data: dict):
#     updated = await update_payroll(payroll_id, data)
#     if updated:
#         return {"message": "Payroll updated successfully"}
#     raise HTTPException(status_code=404, detail="Payroll not found")

# Delete a payroll record by id
@router.delete("/payrolls/{payroll_id}")
async def delete_payroll_endpoint(payroll_id: str):
    deleted = await delete_payroll(payroll_id)
    if deleted:
        return {"message": "Payroll deleted successfully"}
    raise HTTPException(status_code=404, detail="Payroll not found")
