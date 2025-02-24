from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_DETAILS = os.getenv("MONGO_DETAILS", "mongodb://localhost:27017")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.payroll_db
payroll_collection = database.get_collection("payroll")

# Helper function to convert a Mongo document to a dict
def payroll_helper(payroll) -> dict:
    payroll["id"] = str(payroll["_id"])
    del payroll["_id"]
    return payroll

# Create a new payroll record
async def create_payroll(payroll_data: dict) -> dict:
    payroll = await payroll_collection.insert_one(payroll_data)
    new_payroll = await payroll_collection.find_one({"_id": payroll.inserted_id})
    return payroll_helper(new_payroll)

# Retrieve a payroll record by its id
async def retrieve_payroll(payroll_id: str) -> dict:
    from bson import ObjectId
    payroll = await payroll_collection.find_one({"_id": ObjectId(payroll_id)})
    if payroll:
        return payroll_helper(payroll)

# Retrieve all payroll records
async def retrieve_payrolls() -> list:
    payrolls = []
    async for payroll in payroll_collection.find():
        payrolls.append(payroll_helper(payroll))
    return payrolls

# Update an existing payroll record by id
async def update_payroll(payroll_id: str, data: dict):
    from bson import ObjectId
    if len(data) < 1:
        return False
    payroll = await payroll_collection.find_one({"_id": ObjectId(payroll_id)})
    if payroll:
        updated_payroll = await payroll_collection.update_one(
            {"_id": ObjectId(payroll_id)}, {"$set": data}
        )
        if updated_payroll:
            return True
    return False

# Delete a payroll record by id
async def delete_payroll(payroll_id: str):
    from bson import ObjectId
    payroll = await payroll_collection.find_one({"_id": ObjectId(payroll_id)})
    if payroll:
        await payroll_collection.delete_one({"_id": ObjectId(payroll_id)})
        return True
    return False
