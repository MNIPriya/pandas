import pandas as pd 

df = pd.read_csv("customers-100.csv")

#finding the total number of customer 
print(df.info())
print(df.shape)
print(df.describe())
#datatype 
print(df.dtypes)
#finding the missing values 
missing_value = df.isnull().sum()
print(missing_value)
#i din't find any missing values so i continued with my questions 

#country with most coustomers 
country_count = df["Country"].value_counts()
top_countries = country_count.idxmax()
customer_count = country_count.max()
print(f"country with most coustomers : {top_countries}")
print(f"number coustomers : {customer_count}")

#which city has most customers 
city_counts = df["City"].value_counts()
top_ciy = city_counts.idxmax()
city_customer_count = city_counts.max()
print(f"city with most coustomers : {top_ciy}")
print(f"number coustomers : {city_customer_count}")

#finding the top ten cities 
top_10_cities = df["City"].value_counts().head(10)
print(top_10_cities)

#Which company has the highest number of customers?
company_highest = df["Company"].value_counts()
top_companies = company_highest.idxmax()
companies_ustomer_count = company_highest.count()

#checking on subscription 
df["Subscription Date"] = pd.to_datetime(df["Subscription Date"])

#How many customers subscribed each year? 
subscription_per_year = df["Subscription Date"].dt.year.value_counts().sort_index()

#Which year had the maximum subscriptions?
year_count = df["Subscription Date"].dt.year.value_counts()
max_year = year_count.idxmax()
max_subscriptions = year_count.max()
print("Year with maximum subscriptions:", max_year)
print("Number of subscriptions:", max_subscriptions)

# Which month had the highest subscriptions?
max_month = df["Subscription Date"].dt.month_name().value_counts()
top_month = max_month.idxmax()
top_count = max_month.max()
print("Month with highest subscriptions:", top_month)
print("Number of subscriptions:", top_count)


