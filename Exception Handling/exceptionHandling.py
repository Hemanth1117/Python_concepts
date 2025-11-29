# exception = An event that interrputs the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try  2. except 3.finally


# 1/0  # ZeroDivisionError

# 1+"1" # TypeError


# int("pizza") # ValueError



try:
    number = int(input("enter a number to divide:"))
    print(1/number)


    # these are particular exception 
except ZeroDivisionError:
    print("you cannot divide by zero Idiot!")
except ValueError:
    print("enter only number")


except Exception:
    print("something went wrong!")
finally:
    print("do some cleanup here")




# for further we can refer to python official document