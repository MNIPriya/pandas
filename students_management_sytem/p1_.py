import pandas as pd 

df = pd.read_csv("students.csv")

print(df)

print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe)

#finding the missing value 
print(df.isnull().sum())#no null values present 

#creating a column 
df["percentage"] = (
    df["Math"]+ df["Science"] + df["English"]
)/3

print(df)
def grade(x):
    if x >= 90 :
        return "A"
    elif 90 > x >= 80:
        return "B"
    elif 80 > x >= 70:
        return "C"
    elif 70 > x >= 35 :
        return "D"
    else:
        return "F" 
df["Grade"] = df["percentage"].apply(grade)
topper = df.loc[df["percentage"].idxmax()]
print(topper)
#finding the attendence less than 80 

low_att = df[df["Attendance"] < 80]
print(low_att)

#subject-wise avg
print("maths average :", df["Math"].mean())
print("Science avg : ", df["Science"].mean())
print("English avg : ", df["English"].mean())

#saving to report 
df.to_csv(
    "students_report.csv",
    index = False
)