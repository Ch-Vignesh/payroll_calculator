from models.payroll import PayrollInput, PayrollOutput

def calculate_payroll(data: PayrollInput) -> PayrollOutput:
    # Calculate hourly rate
    hourly_rate = data.basic_salary / data.standard_hours

    # Overtime calculation 
    overtime_hours = max(0, data.hours_worked - data.standard_hours)
    overtime_pay = overtime_hours * hourly_rate * 1.5

    # Weekend overtime
    weekend_overtime_pay = data.weekend_overtime_hours * hourly_rate * 2

    # Performance bonus logic
    if data.performance_rating < 3:
        performance_bonus = 0
    elif 3 <= data.performance_rating <= 4:
        performance_bonus = data.basic_salary * 0.05
    else:
        performance_bonus = data.basic_salary * 0.10

    # Leave deductions
    leave_deductions = data.leaves_taken * data.leave_deduction_per_day

    # Shift allowances
    night_shift_bonus = data.night_shifts * data.night_shift_bonus_per_shift
    weekend_shift_bonus = data.weekend_shifts * data.weekend_shift_bonus_per_shift

    # Sales commission
    sales_commission = (data.sales_made * data.sales_commission_percentage) / 100

    # Penalties (assuming 10 minutes per occurrence)
    late_penalty = data.late_arrivals * 10 * data.late_penalty_per_minute
    early_leave_penalty = data.early_leaves * 10 * data.early_leave_penalty_per_minute

    # Loan deductions and interest
    loan_interest = data.loan_balance * (data.loan_interest_rate / 100)
    loan_deduction = data.monthly_loan_payment

    # Miscellaneous allowances
    fuel_allowance = data.misc_allowances.get("fuel_allowance", 0)
    food_allowance = data.misc_allowances.get("food_allowance", 0)
    internet_allowance = data.misc_allowances.get("internet_allowance", 0)
    total_misc_allowance = fuel_allowance + food_allowance + internet_allowance

    # Total earnings (sum of all positive components)
    total_earnings = (
        data.basic_salary +
        overtime_pay +
        weekend_overtime_pay +
        performance_bonus +
        night_shift_bonus +
        weekend_shift_bonus +
        sales_commission +
        total_misc_allowance
    )

    # Non-tax deductions
    non_tax_deductions = leave_deductions + late_penalty + early_leave_penalty + loan_deduction + loan_interest

    # Adjust gross salary
    gross_salary = total_earnings - non_tax_deductions

    # Progressive tax calculation using provided slabs
    tax = 0
    for slab in data.tax_slabs:
        slab_min = slab.min
        slab_max = slab.max if slab.max is not None else float('inf')
        if gross_salary > slab_min:
            taxable_amount = min(gross_salary, slab_max) - slab_min
            tax += taxable_amount * (slab.rate / 100)
    tax_deduction = tax

    # Insurance deductions
    health_insurance_deduction = data.basic_salary * (data.insurance_deductions.get("health_insurance", 0) / 100)
    retirement_contribution = data.basic_salary * (data.insurance_deductions.get("retirement_contribution", 0) / 100)

    net_salary = gross_salary - tax_deduction - health_insurance_deduction - retirement_contribution

    return PayrollOutput(
        employee_id=data.employee_id,
        basic_salary=data.basic_salary,
        overtime_hours=overtime_hours,
        overtime_pay=round(overtime_pay, 2),
        weekend_overtime_hours=data.weekend_overtime_hours,
        weekend_overtime_pay=round(weekend_overtime_pay, 2),
        performance_bonus=round(performance_bonus, 2),
        leave_deductions=round(leave_deductions, 2),
        night_shift_bonus=round(night_shift_bonus, 2),
        weekend_shift_bonus=round(weekend_shift_bonus, 2),
        sales_commission=round(sales_commission, 2),
        late_penalty=round(late_penalty, 2),
        early_leave_penalty=round(early_leave_penalty, 2),
        loan_interest=round(loan_interest, 2),
        loan_deduction=round(loan_deduction, 2),
        fuel_allowance=fuel_allowance,
        food_allowance=food_allowance,
        internet_allowance=internet_allowance,
        gross_salary=round(gross_salary, 2),
        tax_deduction=round(tax_deduction, 2),
        health_insurance_deduction=round(health_insurance_deduction, 2),
        retirement_contribution=round(retirement_contribution, 2),
        net_salary=round(net_salary, 2)
    )
