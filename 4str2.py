str1="hello"
str2="world"

str3='''
this is a multi line string
this is the second line'''
print(str3)

#Concade two strings
greeting=str1+" "+str2
print(greeting)

#string to print multiple variables
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print(f"The sum of {num1} +{num2} is: {num1+num2}")


#split and join a string
statemnt="This is a sample statement and mu name is chetan"
let_split=statemnt.split()
print(let_split)
print("~".join(let_split))

##seaech
print("lo" in str1)
print(str1.find("lo"))

#string Length
print("Length of str1 is: ",len(str1))

#Change case
print(f'Uppercase : {str1.upper()}')
print(f'Lowercase : {str1.lower()}')

#replace
print(str1.replace("h","M"))
