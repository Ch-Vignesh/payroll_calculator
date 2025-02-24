from fastapi import FastAPI
from routers import payroll_router

app = FastAPI(title="Payroll Microservices API")

# Include the payroll router under a common prefix (e.g. /api)
app.include_router(payroll_router.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
