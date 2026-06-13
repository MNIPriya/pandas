# 📊 Student Performance Analysis using Pandas

## 📌 Project Overview

This project analyzes student performance data using the Python Pandas library. The project demonstrates data cleaning, manipulation, analysis, and reporting techniques using real-world student datasets.

## 🎯 Objectives

* Read and analyze CSV data using Pandas.
* Calculate student percentages and grades.
* Identify toppers and low-performing students.
* Analyze attendance records.
* Generate summary statistics and reports.
* Practice core Pandas operations for data analysis.

## 🛠️ Technologies Used

* Python 3.12
* Pandas
* NumPy
* Matplotlib (Optional)
* VS Code

## 📂 Dataset Columns

* Student_ID
* Name
* Age
* Gender
* Math
* Science
* English
* Attendance

## 📈 Features Implemented

### Data Loading

* Read CSV files using `pd.read_csv()`

### Data Exploration

* `head()`
* `tail()`
* `shape`
* `columns`
* `info()`
* `describe()`

### Data Cleaning

* `isnull()`
* `fillna()`
* `dropna()`
* `str.strip()`

### Data Analysis

* Calculate percentages
* Assign grades
* Find topper
* Find lowest scorer
* Attendance analysis
* Subject-wise averages
* Gender-wise analysis
* Sorting and filtering

### Reporting

* Export final reports using `to_csv()`

## 📊 Sample Insights

* Highest Scorer
* Lowest Scorer
* Average Marks in Each Subject
* Students with Attendance Below 80%
* Grade Distribution

## 📚 Pandas Concepts Covered

* DataFrame Creation
* Series Operations
* Indexing
* Boolean Filtering
* `loc[]` and `iloc[]`
* `groupby()`
* `mean()`
* `max()`
* `min()`
* `sort_values()`
* `apply()`
* `value_counts()`
* `to_csv()`

## 🚀 Future Improvements

* Add data visualizations using Matplotlib and Seaborn.
* Build an interactive dashboard using Streamlit.
* Connect with SQL databases.
* Generate automated PDF reports.
* Add machine learning models for performance prediction.

## ▶️ How to Run

```bash
pip install pandas
python analysis.py
```

## 📁 Project Structure

```
Student_Performance_Project/
│
├── students.csv
├── analysis.py
├── students_report.csv
├── README.md

```

## 🏆 Learning Outcome

This project helped in understanding real-world data analysis workflows using Pandas, including data cleaning, transformation, aggregation, and report generation.
