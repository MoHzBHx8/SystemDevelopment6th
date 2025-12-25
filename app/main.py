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


def complex_function(x):
    if x > 0:
        if x < 10:
            if x == 1:
                return "one"
            elif x == 2:
                return "two"
            else:
                return "small"
        else:
            if x < 20:
                return "medium"
            else:
                return "large"
    return "zero"
