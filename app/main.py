from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, database

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="FinTrack Pro")


@app.post("/expenses/", response_model=schemas.Expense)
def create_expense(
    expense: schemas.ExpenseCreate, db: Session = Depends(database.get_db)
):
    db_expense = models.Expense(**expense.model_dump())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


@app.get("/expenses/", response_model=List[schemas.Expense])
def read_expenses(db: Session = Depends(database.get_db)):
    return db.query(models.Expense).all()


def calculate_complex_tax_and_discount(
    amount: float, category: str, user_type: str, region: str, is_holiday: bool
):
    """
    A monster function with high cyclomatic complexity (Grade C or D).
    Intended to trigger a Radon CI failure.
    """
    final_amount = amount

    if amount > 0:
        if user_type == "GOLD":
            if is_holiday:
                final_amount *= 0.8  # 20% discount
            else:
                final_amount *= 0.9  # 10% discount
        elif user_type == "SILVER":
            if amount > 500:
                final_amount *= 0.95
            else:
                final_amount *= 0.98
        else:
            if region == "EU":
                if category == "FOOD":
                    final_amount += amount * 0.05  # Low tax
                else:
                    final_amount += amount * 0.20  # High tax
            elif region == "US":
                if amount > 1000:
                    for i in range(3):  # Arbitrary nested loop logic
                        if i == 0:
                            final_amount += 5
                        else:
                            final_amount += 2
                else:
                    final_amount += 10
            else:
                final_amount += amount * 0.15
    else:
        return 0

    return round(final_amount, 2)
