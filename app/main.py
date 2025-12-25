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


def monster_function(a, b, c, d, e):
    # This nested mess significantly increases "Cyclomatic Complexity"
    if a:
        if b:
            if c:
                return 1
            elif d:
                return 2
            else:
                for i in range(10):
                    if i > e:
                        return 3
        else:
            if d:
                return 4
            while e < 10:
                e += 1
                if e == 5:
                    return 5
    elif b:
        if c:
            return 6
    return 7
