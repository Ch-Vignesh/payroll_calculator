This FastAPI project is a comprehensive payroll calculator designed to compute detailed monthly salaries for employees by taking into account various factors such as overtime, taxes, bonuses, deductions, allowances, and more. Here's a brief overview:

How It Works
Input Processing:
The project accepts a JSON payload containing all necessary payroll parameters (like basic salary, hours worked, overtime rates, performance rating, loan details, etc.) defined by Pydantic models. This ensures that the input data is validated and structured.

Payroll Calculation:
A dedicated payroll service processes the input data. It computes:

Overtime: Standard and weekend overtime pay based on the hourly rate.
Bonuses: Performance-based bonuses calculated as a percentage of the basic salary.
Deductions: For leaves, late arrivals, early leaves, and loan payments (with interest).
Allowances: Such as fuel, food, internet, night, and weekend shift bonuses.
Taxes: Progressive tax calculation based on defined tax slabs.
Insurance Contributions: Health and retirement deductions calculated as percentages of the basic salary.
Database Integration:
The calculated payroll data can be saved into a MongoDB database using asynchronous CRUD operations. This ensures data persistence and provides endpoints to create, retrieve, update, and delete payroll records.

Why You Need This Project
Automation and Accuracy:
Payroll calculations are complex and error-prone when done manually. This system automates the process, reducing human errors and ensuring consistent application of business rules.

Modularity and Scalability:
By separating the payroll calculation logic, database operations, and API routing into distinct microservices-like modules, the system is easier to maintain, test, and scale. Each component can evolve independently.

Integration Ready:
With RESTful endpoints, the project can be easily integrated with other systems, such as HR management platforms, accounting software, or employee self-service portals.

Components and Modules
Models (models/payroll.py):
Define data structures (PayrollInput and PayrollOutput) and the tax slab details to standardize data across the application.

Payroll Service (services/payroll_service.py):
Contains the business logic for computing all payroll-related figures. This module processes input parameters and returns the calculated payroll output.

Database Service (services/database_service.py):
Manages MongoDB interactions using Motor (an async MongoDB driver). It provides functions to perform CRUD operations on payroll records.

API Router (routers/payroll_router.py):
Exposes endpoints for:

Calculating payroll without saving.
Calculating and saving payroll to the database.
Retrieving (single or multiple) payroll records.
Updating and deleting payroll records.
Main Application (main.py):
Integrates the routers into a single FastAPI application, serving as the entry point for the project.

Key Parameters Used
Employee Data: employee_id, basic_salary
Time & Overtime: hours_worked, standard_hours, overtime_rate, weekend_overtime_rate, weekend_overtime_hours
Performance: performance_rating
Leave & Penalties: leaves_taken, leave_deduction_per_day, late_arrivals, late_penalty_per_minute, early_leaves, early_leave_penalty_per_minute
Loans & Interest: loan_balance, monthly_loan_payment, loan_interest_rate
Shifts & Allowances: night_shifts, night_shift_bonus_per_shift, weekend_shifts, weekend_shift_bonus_per_shift, along with miscellaneous allowances like fuel, food, and internet.
Sales: sales_commission_percentage, sales_made
Insurance: insurance_deductions containing health and retirement percentages.
Tax Slabs: A list of objects specifying different tax rates for various income ranges.