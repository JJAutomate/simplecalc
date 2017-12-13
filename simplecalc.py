
def add(one,two):
    return one+two
def sub(one, two):
    return one-two
def mult(one, two):
    return one*two
def div(one, two):
    return one/two

print("enter 1,2,3, or 4 for addition,subtraction,multiplication or division.")


#try:
option =input("To exit enter 0,Else enter an option:")
#if option!='1'or'2'or'3'or'4':
#    print("Check your number and try again.")

#if (option <0 or option>4):
#    print("Check your number and try again.")
#    exit()

while (option!='0'):
    a= int(input("enter first number:"))
    b=int(input("enter second number:"))

    if option=='1':
        print(a,"+",b,"=" ,add(a,b))
    elif option=='2':
        print(a,"-",b,"=",sub(a,b))
    elif option=='3':
        print(a,"*",b,"=",mult(a,b))
    elif option=='4':
        print(a,"/",b,"=",div(a,b))
    print("enter 1,2,3, or 4 for addition,subtraction,multiplication or division.")
    option =input("To exit enter 0,Else enter an option:")
#except:
#    print("Check your number again.")
