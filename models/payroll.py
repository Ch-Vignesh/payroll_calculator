from pydantic import BaseModel
from typing import Optional, List, Dict

class TaxSlab(BaseModel):
    min: float
    max: Optional[float]  # None means no upper bound
    rate: float

class PayrollInput(BaseModel):
    employee_id: int
    basic_salary: float
    hours_worked: float
    standard_hours: float
    overtime_rate: float
    weekend_overtime_rate: float
    weekend_overtime_hours: float
    performance_rating: float
    leaves_taken: int
    leave_deduction_per_day: float
    loan_balance: float
    monthly_loan_payment: float
    loan_interest_rate: float
    night_shifts: int
    night_shift_bonus_per_shift: float
    weekend_shifts: int
    weekend_shift_bonus_per_shift: float
    late_arrivals: int
    late_penalty_per_minute: float
    early_leaves: int
    early_leave_penalty_per_minute: float
    sales_commission_percentage: float
    sales_made: float
    misc_allowances: Dict[str, float]
    insurance_deductions: Dict[str, float]
    tax_slabs: List[TaxSlab]

class PayrollOutput(BaseModel):
    employee_id: int
    basic_salary: float
    overtime_hours: float
    overtime_pay: float
    weekend_overtime_hours: float
    weekend_overtime_pay: float
    performance_bonus: float
    leave_deductions: float
    night_shift_bonus: float
    weekend_shift_bonus: float
    sales_commission: float
    late_penalty: float
    early_leave_penalty: float
    loan_interest: float
    loan_deduction: float
    fuel_allowance: float
    food_allowance: float
    internet_allowance: float
    gross_salary: float
    tax_deduction: float
    health_insurance_deduction: float
    retirement_contribution: float
    net_salary: float
