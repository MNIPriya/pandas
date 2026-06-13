import pandas as pd 

df = pd.read_csv("employee_salary_dataset.csv")
#counting the first 5
print(df.head())
#last 5 
print(df.tail())
#discription of mathematical funtion , mean , count , std , max
print(df.describe())
#tells about the types 
print(df.info())
#number of rows and coulumn 
print(df.shape)

#department_wise salary analysis 
dept_sal = df.groupby("Department")["Monthly_Salary"].agg(['mean',"max","min"])
print(dept_sal)

#top 5 higest paid 
top_5 = df.sort_values(by= "Monthly_Salary", ascending=False).head(5)
print(top_5)

#collection of experienced and freshers 
experienced_employee =  df[df["Experience_Years"] > 5] \
    .sort_values(by="Experience_Years", ascending=False)
print(experienced_employee)

freshers = df[df["Experience_Years"]<2]
print(freshers)

#usage of loc features 
Marketing= df.loc[df["Department"] == "Marketing"]
print(Marketing)

#sorting 

sorted_salary = df.sort_values(by = "Monthly_Salary" , ascending=False)