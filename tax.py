salary=int(input("Enter salary of employee :"))
allowances=int(input("Enter allowances :"))

gross_salary=salary+allowances
print(f"Gross salary is : {gross_salary}")

if gross_salary>=500000:
    tax=(gross_salary*0.2)
else:
    tax=(gross_salary*0.1)

print("Tax is :",tax)

net_salary=gross_salary-tax
print("Net salary is :",net_salary)

