PricesList_inr =[3000,56000,45000,2300]
def conversion():
    usd=list(map(lambda x:x*0.012 , PricesList_inr))
    euro=list(map(lambda x:x*0.011 ,PricesList_inr))
    print(f"Conversion to usd {usd}")
    print(f"Conversion to euro {euro}")
conversion()

student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad","Samalla Akshay"]
def lonenames():
    lone_names_list=list(filter(lambda x: len(x)>6,student_name_list))
    print(" name which has more than 6 characters",lone_names_list)
lonenames() 

products = [
    {"name": "Laptop", "price": 92000},
    {"name": "Smartphone", "price": 48000},
    {"name": "Tablet", "price": 20000},
    {"name": "Monitor", "price": 8000}
    ]
def ascendingorder():
    ascend=sorted(products,key=lambda x:x['price'])
    print("Product in ascending order based on the price",ascend)
ascendingorder()

numbers=[1,7,5,4,9,8]
def filtering():
    global numbers
    oddlist=list(filter(lambda x:x%2!=0,numbers))
    numberslist=list(map(lambda x:x**2 if x%2==0 else x,numbers))
    numberslist.sort()
    print("odd ones list",oddlist)
    print("List after squaring even and sorting in ascending order",numberslist)
filtering()

cities = [
    {"name": "New York", "population": 8419600},
    {"name": "Los Angeles", "population": 3980400},
    {"name": "Chicago", "population": 2716000},
    {"name": "Houston", "population": 2328000}
]
def descendingorder():
    descend=sorted(cities,key=lambda x: -x['population'])
    print("Sorting the cities in descending order of their population",descend)
descendingorder()

users = [
    {"email": "alice@example.com", "verified": True},
    {"email": "bob@example.com", "verified": False},
    {"email": "charlie@example.com", "verified": True},
    {"email": "daisy@example.com", "verified": False}
	 ]
def verifiedusers():
    verifieduser=list(filter(lambda x: x['verified']==True ,users))
    verifieduseremail=list(map(lambda x:{"email": x['email']},verifieduser))
    print("emails of verified users",verifieduseremail)
verifiedusers() 

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Headphones", "price": 80},
    {"name": "Smartphone", "price": 700},
    {"name": "Monitor", "price": 150}
]

def discounts():
    discount_eligible_list = list(filter(lambda x: x['price'] > 100, products))
    discount_list=list(map(lambda x:x['price']*0.8 if x['price']>100 else x['price'], products))
    discounted_products = list(map(lambda x: {"name": x['name']}, discount_eligible_list))
    print("Updated prices are",discount_list)
    print("Discounted Products:",discounted_products)

discounts()


words = ["apple", "banana", "cherry", "date", "fig"]
def sortwords():
    sortwords_list=sorted(words,key=lambda x:len(x))
    print(sortwords_list)
sortwords()

numbers3=[2,2,4,6,3,4,6,1]
num=[]
for i in numbers3:
    if i not in num:
        num.append(i)
print(num)
