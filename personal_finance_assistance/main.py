from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import os

app = FastAPI(title="Personal Finance Tracker API")

# ==========================
# Create folders and files
# ==========================
os.makedirs("data", exist_ok=True)
os.makedirs("charts", exist_ok=True)

if not os.path.exists("data/income.csv"):
    pd.DataFrame(
        columns=["id", "date", "source", "amount"]
    ).to_csv("data/income.csv", index=False)

if not os.path.exists("data/expense.csv"):
    pd.DataFrame(
        columns=["id", "date", "category", "description", "amount"]
    ).to_csv("data/expense.csv", index=False)

if not os.path.exists("data/budget.csv"):
    pd.DataFrame({
        "category": ["Food", "Shopping", "Transport", "Entertainment"],
        "budget": [5000, 10000, 3000, 4000]
    }).to_csv("data/budget.csv", index=False)


# ==========================
# Pydantic Schemas
# ==========================
class Income(BaseModel):
    date: date
    source: str
    amount: float


class Expense(BaseModel):
    date: date
    category: str
    description: str
    amount: float


# ==========================
# Root Endpoint
# ==========================
@app.get("/")
def home():
    return {"message": "Personal Finance Tracker API"}


# ==========================
# Add Income
# ==========================
@app.post("/income")
def add_income(data: Income):
    df = pd.read_csv("data/income.csv")

    if df.empty:
        new_id = 1
    else:
        new_id = int(df["id"].max()) + 1

    new_row = {
        "id": new_id,
        "date": data.date,
        "source": data.source,
        "amount": data.amount
    }

    df = pd.concat(
        [df, pd.DataFrame([new_row])],
        ignore_index=True
    )

    df.to_csv("data/income.csv", index=False)

    return {
        "message": "Income Added Successfully"
    }


# ==========================
# Add Expense
# ==========================
@app.post("/expense")
def add_expense(data: Expense):
    df = pd.read_csv("data/expense.csv")

    if df.empty:
        new_id = 1
    else:
        new_id = int(df["id"].max()) + 1

    new_row = {
        "id": new_id,
        "date": data.date,
        "category": data.category,
        "description": data.description,
        "amount": data.amount
    }

    df = pd.concat(
        [df, pd.DataFrame([new_row])],
        ignore_index=True
    )

    df.to_csv("data/expense.csv", index=False)

    return {
        "message": "Expense Added Successfully"
    }


# ==========================
# Monthly Report
# ==========================
@app.get("/monthly-report")
def monthly_report():
    income_df = pd.read_csv("data/income.csv")
    expense_df = pd.read_csv("data/expense.csv")

    total_income = income_df["amount"].sum()
    total_expense = expense_df["amount"].sum()

    savings = total_income - total_expense

    if total_income > 0:
        savings_rate = (savings / total_income) * 100
    else:
        savings_rate = 0

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "savings": savings,
        "savings_rate": round(savings_rate, 2)
    }


# ==========================
# Category Analysis
# ==========================
@app.get("/category-analysis")
def category_analysis():
    df = pd.read_csv("data/expense.csv")

    if df.empty:
        return {}

    result = (
        df.groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
        .to_dict()
    )

    return result


# ==========================
# Budget Analysis
# ==========================
@app.get("/budget-analysis")
def budget_analysis():
    expense_df = pd.read_csv("data/expense.csv")
    budget_df = pd.read_csv("data/budget.csv")

    if expense_df.empty:
        return {
            row["category"]: "No Expenses"
            for _, row in budget_df.iterrows()
        }

    spent = (
        expense_df
        .groupby("category")["amount"]
        .sum()
        .reset_index()
    )

    merged = budget_df.merge(
        spent,
        on="category",
        how="left"
    )

    merged["amount"] = (
        merged["amount"].fillna(0)
    )

    result = {}

    for _, row in merged.iterrows():

        if row["amount"] > row["budget"]:
            result[row["category"]] = (
                "Budget Exceeded"
            )
        else:
            result[row["category"]] = (
                "Within Budget"
            )

    return result


# ==========================
# Expense Pie Chart
# ==========================
@app.get("/expense-chart")
def expense_chart():
    df = pd.read_csv("data/expense.csv")

    if df.empty:
        return {
            "message": "No expense data found."
        }

    data = (
        df.groupby("category")["amount"]
        .sum()
    )

    plt.figure(figsize=(7, 7))

    plt.pie(
        data,
        labels=data.index,
        autopct="%1.1f%%"
    )

    plt.title("Expense Distribution")

    path = "charts/expense_pie.png"

    plt.savefig(path)
    plt.close()

    return {
        "message": "Chart Created",
        "path": path
    }


# ==========================
# Category Bar Chart
# ==========================
@app.get("/category-chart")
def category_chart():
    df = pd.read_csv("data/expense.csv")

    if df.empty:
        return {
            "message": "No expense data found."
        }

    data = (
        df.groupby("category")["amount"]
        .sum()
    )

    plt.figure(figsize=(8, 5))

    plt.bar(
        data.index,
        data.values
    )

    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Category Wise Spending")

    path = "charts/category_bar.png"

    plt.savefig(path)
    plt.close()

    return {
        "message": "Chart Created",
        "path": path
    }


# ==========================
# Savings Line Chart
# ==========================
@app.get("/savings-chart")
def savings_chart():
    income_df = pd.read_csv("data/income.csv")
    expense_df = pd.read_csv("data/expense.csv")

    if income_df.empty:
        return {
            "message": "No income data found."
        }

    income_df["date"] = pd.to_datetime(
        income_df["date"]
    )

    expense_df["date"] = pd.to_datetime(
        expense_df["date"]
    )

    income_month = (
        income_df
        .groupby(
            income_df["date"].dt.to_period("M")
        )["amount"]
        .sum()
    )

    expense_month = (
        expense_df
        .groupby(
            expense_df["date"].dt.to_period("M")
        )["amount"]
        .sum()
    )

    savings = (
        income_month
        .subtract(expense_month,
                  fill_value=0)
    )

    plt.figure(figsize=(8, 5))

    plt.plot(
        savings.index.astype(str),
        savings.values,
        marker="o"
    )

    plt.xlabel("Month")
    plt.ylabel("Savings")
    plt.title("Monthly Savings Trend")

    path = "charts/savings_line.png"

    plt.savefig(path)
    plt.close()

    return {
        "message": "Chart Created",
        "path": path
    }