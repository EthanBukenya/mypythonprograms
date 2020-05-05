print("please fill in the details below! ")

customer_name = input("Enter your customer_name : ")
address = input("Enter address : ")
food_ordered = input("Enter your food choice : ")

def say_hello():
    print("Hi, " + customer_name + ", " + address + " , and your food ordered is "
          + food_ordered + " Thank you, and hope to serve you again ")

say_hello()
