products="yogurt eggs cookies cookies eggs yogurt apple yogurt apple"
products=list(products.split(" "))
products_dict={}
for i in products:
    if i not in products_dict:
        products_dict[i]=1
    else:
        products_dict[i]+=1
print(products_dict)

initial_stock = {"apple": 50,"banana": 100,"orange": 75}
sold_item = {"apple": 10, "banana": 20, "orange": 15}
current_stock={}
for i in initial_stock:
    current_stock[i]=initial_stock[i]-sold_item[i]
print(current_stock)

sales_data = [
    {"region": "North", "sales": 15000},
    {"region": "South", "sales": 8000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000}
]
sales_dict={}
for record in sales_data:
    region=record['region']
    sales=record['sales']
    if region in sales_dict:
        sales_dict[region]+=sales
    else:
        sales_dict[region]=sales
print(sales_dict)

mobile_num=input("Enter your mobile number : ")
numbers_dict={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}

l=''
for i in mobile_num:
    l+=" "+numbers_dict[int(i)]
print(l)