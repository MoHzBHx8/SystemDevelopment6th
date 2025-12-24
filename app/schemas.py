from pydantic import BaseModel, Field


class ExpenseBase(BaseModel):
    description: str
    amount: float = Field(..., gt=0, description="Amount must be greater than zero")
    category: str


class ExpenseCreate(ExpenseBase):
    pass


class Expense(ExpenseBase):
    id: int

    class Config:
        from_attributes = True
