"""  1. **Students Result Filter**
 Use `filter()` to get only the students who passed (marks ≥ 50).
 ```python
 students = [
 {"name": "Ali", "marks": 45},
 {"name": "Zara", "marks": 78},
 {"name": "Ahmed", "marks": 90},
 {"name": "Sara", "marks": 32},
 {"name": "Hamza", "marks": 60}
 ]
 ```"""

students = [
 {"name": "Ali", "marks": 45},
 {"name": "Zara", "marks": 78},
 {"name": "Ahmed", "marks": 90},
 {"name": "Sara", "marks": 32},
 {"name": "Hamza", "marks": 60}
 ]

result = list(filter(lambda m:m['marks']>=50,students))
print("----------------------------------------")
print("STUDENTS WITH GREATER THAN 50 MARKS : ")
print("----------------------------------------")
for i in result:
    print(i)
else:
    print("-------------------------------")   

"""
 2. **Employee Salary Filter**
 Use `filter()` to get employees who earn more than 50,000.
 ```python
 employees = [
 {"name": "Asad", "salary": 45000},
 {"name": "Hina", "salary": 70000},
 {"name": "Usman", "salary": 52000},
 {"name": "Tariq", "salary": 40000}
 ]
 ```"""


employees = [
 {"name": "Asad", "salary": 45000},
 {"name": "Hina", "salary": 70000},
 {"name": "Usman", "salary": 52000},
 {"name": "Tariq", "salary": 40000}
 ]
result = list(filter(lambda s : s['salary']>50000,employees))
print("----------------------------------------")
print("EMPLOYEE THOSE WHO EARN MORE THAN 50K ")
print("----------------------------------------")
for i in result:
    print(i)
else:
    print("---------------------------------")    





"""
 3. **Product Availability**
 Use `filter()` to get only the available products.
 ```python
 products = [
 {"name": "Laptop", "available": True},
 {"name": "Phone", "available": False},
 {"name": "Keyboard", "available": True},
 {"name": "Mouse", "available": False}
 ]
 """



products = [
 {"name": "Laptop", "available": True},
 {"name": "Phone", "available": False},
 {"name": "Keyboard", "available": True},
 {"name": "Mouse", "available": False}
]

result = list(filter(lambda p : p['available']==True ,products))
print("-----------------------------")
print("PRODUCTS WHICH ARE AVAILABLE")
print("-----------------------------")
for i in result:
    print(i)
else:
    print("-----------------------------")

"""
 4. **Temperature Data**
 Use `filter()` to get only the readings greater than 30°C.
 ```python
 temperatures = [
 {"city": "Karachi", "temp": 36},
 {"city": "Lahore", "temp": 29},
 {"city": "Quetta", "temp": 33},
 {"city": "Islamabad", "temp": 27}
 ]
"""

temperatures = [
 {"city": "Karachi", "temp": 36},
 {"city": "Lahore", "temp": 29},
 {"city": "Quetta", "temp": 33},
 {"city": "Islamabad", "temp": 27}
 ]
print("-----------------------------")
print("TEMPERATURE BEFORE FILTER : ")
print("-----------------------------")
for i in temperatures:
    print(i)


result = list(filter(lambda t:t['temp']>30,temperatures))
print("------------------------------------")
print("TEMPERATURE GREATER THAN 30 DEGREE !")
print("------------------------------------")
for i in result:
    print(i)
else:
    print("------------------------------------")


"""
 5. **Car Model Filter**
 Use `filter()` to get cars made after 2018.
 ```python
 cars = [
 {"model": "Civic", "year": 2017},
{"model": "Corolla", "year": 2019},
 {"model": "Alto", "year": 2020},
 {"model": "Suzuki Mehran", "year": 2015}
 ]
"""


cars = [
 {"model": "Civic", "year": 2017},
 {"model": "Corolla", "year": 2019},
 {"model": "Alto", "year": 2020},
 {"model": "Suzuki Mehran", "year": 2015}
 ]

print("-------------------------")
print("CARS WITH ALL MODELS : ")
print("-------------------------")
for i in cars:
    print(i)
else:
    print("---------------------------------")
    print("CARS MODEL WITH GREATER THAN 2018")
    print("---------------------------------")
result = list(filter(lambda m:m['year']>2018,cars))
for i in result : 
    print(i)
else:
    print("---------------------------")
    print("PROGRAM HAS BEEN COMPLETE !")
    print("---------------------------")






"""
 6. **Bank Account Filter**
 Use `filter()` to get accounts with balance less than 1000 (low balance warning).
 ```python
 accounts = [
 {"name": "Ali", "balance": 1200},
 {"name": "Fatima", "balance": 800},
 {"name": "Bilal", "balance": 300},
 {"name": "Ayesha", "balance": 4000}
 ]
 """


accounts = [
 {"name": "Ali", "balance": 1200},
 {"name": "Fatima", "balance": 800},
 {"name": "Bilal", "balance": 300},
 {"name": "Ayesha", "balance": 4000}
 ]
print("--------------------------")
print("ACCOUNTS BEFORE FILTER ! ")
print("--------------------------")

for i in accounts:
    print(i)
else:
    print("-------------------------")   
    print("ACCOUNTS AFTER FILTER : ")
    print("-------------------------")   
result = list(filter(lambda a:a['balance']<1000,accounts))
for i in result:
    print(i)
else:
    print("--------------------")  
    print("PROGRAM COMPLETE !") 
    print("--------------------")  



"""
 7. **Book Rating Filter**
 Use `filter()` to get only books with a rating above 4.0.
 ```python
 books = [
 {"title": "Python Basics", "rating": 4.5},
 {"title": "AI Concepts", "rating": 3.9},
 {"title": "Machine Learning", "rating": 4.8},
 {"title": "Data Science 101", "rating": 4.0}
 ]
"""

books = [
 {"title": "Python Basics", "rating": 4.5},
 {"title": "AI Concepts", "rating": 3.9},
 {"title": "Machine Learning", "rating": 4.8},
 {"title": "Data Science 101", "rating": 4.0}
 ]
print("--------------------------------------")
print("BOOKS WITH ALL RATING BEFORE FILTER !")
print("--------------------------------------")
for i in books:
    print(i)
else:
    print("--------------------------------------")
    print("BOOKS AFTER FILTERED WITH CONDITION !") 
    print("--------------------------------------")
result = list(filter(lambda r:r['rating']>4.0,books))
for i in result:
    print(i)
else:
    print("----------------------------")  
    print("PROGRAM HAS BEEN COMPLETE !")  
    print("-----------------------------")

"""
 8. **Customer Age Filter**
 Use `filter()` to get customers older than 30 years.
 ```python
 customers = [
 {"name": "Ali", "age": 25},
 {"name": "Sara", "age": 35},
 {"name": "Zain", "age": 40},
 {"name": "Hina", "age": 22}
 ]
"""

customers = [
 {"name": "Ali", "age": 25},
 {"name": "Sara", "age": 35},
 {"name": "Zain", "age": 40},
 {"name": "Hina", "age": 22}
 ]

print("-------------------------------")
print("CUSTOMERS AGES BEFORE FILTER !")
print("--------------------------------")
for i in customers:
    print(i)
else:
    print("---------------------------------")
    print("CUSTOMERS AGE AFTER FILTERATION !") 
    print("----------------------------------")

result = list(filter(lambda a:a['age']>30,customers))
for  i in result:
    print(i)   
else:
    print("----------------------------")  
    print("PROGRAM HAS BEEN COMPLETE !")  
    print("-----------------------------")


"""
 9. **Movie Duration Filter**
 Use `filter()` to get movies longer than 120 minutes.
 ```python
 movies = [
 {"title": "Inception", "duration": 148},
 {"title": "Toy Story", "duration": 95},
 {"title": "Interstellar", "duration": 169},
 {"title": "Cars", "duration": 117}
 ]
 """

movies = [
 {"title": "Inception", "duration": 148},
 {"title": "Toy Story", "duration": 95},
 {"title": "Interstellar", "duration": 169},
 {"title": "Cars", "duration": 117}
 ]

print("-----------------------")
print("MOVIES BEFORE FILTER : ")
print("-----------------------")

for i in movies:
    print(i)
else:
    print("-----------------------")
    print("MOVIES AFTER FILTER : ")
    print("-----------------------")
result = list(filter(lambda m:m['duration']>120,movies))
for i in result:
    print(i)
else:
    print("----------------------------")
    print("PROGRAM HAS BEEN COMPLETE !")
    print("----------------------------")




"""
 Use `filter()` to get websites with more than 10,000 visitors.
 ```python
 traffic = [
 {"site": "Google", "visitors": 100000},
 {"site": "YouTube", "visitors": 95000},
{"site": "MyBlog", "visitors": 7000},
 {"site": "LocalShop", "visitors": 800}
 ]
"""


traffic = [
 {"site": "Google", "visitors": 100000},
 {"site": "YouTube", "visitors": 95000},
{"site": "MyBlog", "visitors": 7000},
 {"site": "LocalShop", "visitors": 800}
 ]

print("--------------------------")
print("VISITOR BEFORE FILTER : ")
print("--------------------------")

for i in traffic:
    print(i)
else:
    print("-----------------------")
    print("VISITOR AFTER FILTER ! ")
    print("-----------------------")
result = list(filter(lambda v:v['visitors']>10000,traffic))
for i in result:
    print(i)
else:
    print("-----------------------------")
    print("VISITORS AFTER FILTERATION ! ") 
    print("-----------------------------")

