# def div(a,b) :
#     print('1')
#     print(a/b)

# def smart_div(fucn):
#     print('2')
#     def inner(a,b):
#         print('3')
#         if a < b :
#             a,b = b,a
#         return fucn(a,b)
#     return inner

# div = smart_div(div)
# div(2,4)

# def div(a,b):
#     print(a/b)

# def calculate(fun, a,b):
#     if a < b:
#         a,b = b,a
#         return fun(a,b)

# calculate(div,2,4)

# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "root",
#     database = "join"
# )
# cursor = mydb.cursor()
# cursor.execute("select o.OrderID , c.Country from \
#                orders as o inner join customers as c \
#                on \
#                o.CustomerID = c.CustomerID")
# data = cursor.fetchall()
# for i in data:
#     print('data : ', i)

# t = ([1, 2, 3], ['a', 'b', 'c'])
# t[0][1] = 9
# print(t)

# from flask import Flask #-------- imports the Flask class from the Flask framework 

# # Create a Flask web application
# app = Flask(__name__) #-------- __name__ argument is used to determine the root path

# @app.route('/') #--------  route is defined  root URL
# def hello(): # -------- function
#     return "Hello, World!"

# if __name__ == '__main__': #-------- Flask application is only run if the script is executed
#     # Run the application in development mode
#     app.run(debug=True)

# Python program for demonstrating multilevel inheritance  
  
# Here, we will create the Base class   
# class Grandfather1:  
  
#     def __init__(self, grandfathername1):  
#         self.grandfathername1 = grandfathername1  
  
# # here, we will create the Intermediate class  
# class Father1(Grandfather1):  
#     def __init__(self, fathername1, grandfathername1):  
#         self.fathername1 = fathername1  
  
#         # here, we will invoke the constructor of Grandfather class  
#         Grandfather1.__init__(self, grandfathername1)  
  
# # here, we will create the Derived class  
# class Son1(Father1):  
#     def __init__(self,sonname1, fathername1, grandfathername1):  
#         self.sonname1 = sonname1  
  
#         # here, we will invoke the constructor of Father class  
#         Father1.__init__(self, fathername1, grandfathername1)  
  
#     def print_name(self):  
#         print('Grandfather name is :', self.grandfathername1)  
#         print("Father name is :", self.fathername1)  
#         print("Son name is :", self.sonname1)  
  
# # Driver code  
# s1 = Son1('John', 'John Jr', 'John Jr Jr')   
# s1.print_name()  

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict['name'] = 'kalpesh'
# thisdict.pop()
# print(thisdict)
sorted_dict_by_keys = {key: thisdict[key] for key in sorted(thisdict)}

# print(sorted_dict_by_keys)
# print(type(thisdict))


list1=["apple","banana","grapes","strawberry", "orange"]
# list1.append("strawberry")   # strawberry is added to the list
# print(list1)
# list1.pop(2)
# print(list1)
list1.sort(reverse=True)
# print(list1)

list1=[1,5,3,9,"apple"]
print(list1.index(9)) # returns the index value of the particular element
list2=[2,7,8,7]
print(list2.index(7)) # returns the index value of the element at its first occurence
print(list2.index(7,1))