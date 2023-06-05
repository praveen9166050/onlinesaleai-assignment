# importing the pandas library
import pandas as pd

# reading the csv files
dept = pd.read_csv('ASDE Assignment - Departments.csv')
emp = pd.read_csv('ASDE Assignment - Employees.csv')
sal = pd.read_csv('ASDE Assignment - Salaries.csv')

# selecting the top 3 departments
top3_dept = dept.iloc[:3, :]

# joining the top3_dept and emp dataframes using their id columns
dept_emp = pd.merge(left=top3_dept, right=emp, how='inner', left_on="ID", right_on="DEPT ID", copy=True)

# joining the dept_emp and sal dataframes using their id columns
final = pd.merge(left=dept_emp, right=sal, how='inner', left_on="ID_y", right_on="EMP_ID", copy=True)

# keeping the relavant columns only
final = final[["NAME_x", "AMT (USD)"]]

# grouping the result by department and aggregating the salaries using mean function
res = final.groupby(by="NAME_x").agg('mean')

# renaming the column names as required in the result
res.index.name = "DEPT_NAME"
res.columns = ["AVG_MONTHLY_SALARY (USD)"]

# printing the result
print(res)