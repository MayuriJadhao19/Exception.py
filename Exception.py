#Error which comes at run timme is called
#Keyword used in python for Exception handling are try,except,else,finally,and raise statement.
'''
print("1.#Accept bill details:try,except ")
try:
    cust_name = input("Enter your Name :")
    amount = float(input("Enter bill amount :"))
except ValueError as e:
    print(f"error :{e}")
    amount = float(input("Enter bill amount :"))
    
print("--------Details----------")
print(f"Customer Name :{cust_name}")
print(f"Bill Amount :{amount}")
print("----------Thank you for Purchaing-------")

print("------------------------------------------------")
print("1.#Accept bill details:try,except,else")

try:
    cust_name = input("Enter your name :")
    amount = float(input("Enter Bill Amount :"))
except ValueError as e:
    print(f"error :{e}")
    amount = float(input("Enter bill amount :"))
except Exception as e:
    print(f"error :{e}")
else:
    print("--------Details----------")
    print(f"Customer Name :{cust_name}")
    print(f"Bill Amount :{amount}")
    print("----------Thank you for Purchaing-------")
    
print("1.#Accept bill details:try,except,else,Finally")

try:
    cust_name = input("Enter your name :")
    amount = float(input("Enter Bill Amount :"))
except ValueError as e:
    print(f"error :{e}")
    amount = float(input("Enter bill amount :"))
except Exception as e:
    print(f"error :{e}")
else:
    print("--------Details----------")
    print(f"Customer Name :{cust_name}")
    print(f"Bill Amount :{amount}")
    
finally:
    print("----------Thank you for Purchaing-------")
    
print("---------------------------------------------")
print("4.#Discount bill program :")

try:
    cust_name = input("Enter your name :")
    amount = float(input("Enter Bill Amount :"))
    discount = "20"
    amount = amount - discount
except ValueError as e:
    print(f"error :{e}")
    amount = float(input("Enter bill amount :"))
except Exception as e:
    print(f"error :{e}")
    amount = amount - float(discount)
else:
    print("Else block")
    
finally:
    print("--------Details----------")
    print(f"Customer Name :{cust_name}")
    print(f"Bill Amount :{amount}")

print("5.#Raise")
try:
    cust_name = input("Enter your name :")
    amount = float(input("Enter Bill Amount :"))
    if amount < 0:
        raise Exception("amount can not be less than (0)/Zero")
   
except ValueError as e:
    print(f"error :{e}")
    
except Exception as e:
    print(f"error :{e}")
    amount=float(input("Enter Bill Amount :"))
else:
    print("Else block")
    
    
finally:
    print("--------Details----------")
    print(f"Customer Name :{cust_name}")
    print(f"Bill Amount :{amount}")
    print("-----------Thank You---------")
'''
print("6.Devide By zero Error")
print("Write a script that safely divides two numbers provided by the user")
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide a number by zero!")

print("Program continues running smoothly...")




    



    
    

