
#Introduction To Data Strcutures

#number:integer
x=46
type(x)

#number:float
y=10.6
type(y)

#number:complex

z=2j+1
type(z)

#String
x="Hello AI era"
type(x)

#Boolean

True
False
type(True)
5==4
3==2
3==3

#Lists

x=["btc","eth","xrp"]
type(x)

#Dictionary

x={"name":"peter","Age":36}
type(x)

#Tuple
x=("python","ml","ds")
type(x)

#Set

x={"python","ml","ds"}#the difference from the dictionary is that there is no ":"expression
type(x)

#NUMBERS:INT,FLOAT,COMPLEX

a=5
b=10.5

a*3
a/7
a*b/10
a**2

############################
# Changing Types
############################

a=5
b=10.5
int(b)
float(a)

int(a*b/10)
float(a*b/10)

c=a*b/10
c

#############################
#Strings
#############################

print("John")
"John"

name="aziz"
name='aziz'

#############################
# Multi-Line Strings
#############################

long_str="""boolen,dictionary,complex,
numbers,int,float,List"""

#############################
# Accessing Strings Elements
#############################

name="aziz"
name[1]
name[2]
name[0:2]
name[-1]

data="Data_Slice"
data[0:5]

"data" in data
"Data" in data
"Slice" in data

#############################
#Strings Methods
#############################


dir(str)
######
dir(int)

##########################
# Len
##########################

name="John"
type(name)
type(len)


len(name)
len("azizsimsek")
len("miuul")

#######################
#Upper & Lower methods:
#######################

"miuul".upper()
"MIUUL".lower()
"miuul".title()

type(upper)
type(upper())

###########################
#Replace:changes character
###########################

hi="Hello AI Era"
hi.replace("l","p")

###########################
#Split
###########################

"Hello AI Era".split()

###########################
#strip
###########################

" ofofo ".strip()
"ofofo".strip("o")

###########################
#capitalize
###########################

"foo".capitalize()

dir("foo")

"foo".startswith("f")

