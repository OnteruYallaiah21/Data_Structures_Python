#1) ash is used for comments
print("Hello world")
#2)variables
# In pyhon no Need to decara varible as implicitly It is automatoically taken
x=4;#Int data type(Int)
y="Yallesh Onteru"#string Data type(str)
print(x);
print(y);
#3)type casting=>process of converting one data type to another data type
x1=str(x)
print(type(x))#int class
print(type(x1))#string class in this way we can convert one data typoe to anothe data type
#Remember that variable names are case-sensitive.it know the deffernce of small 'a' and 'A'
X =4.4664;
print(x)
print(X)
#multiple values are printed by , operator in pyton
print("**********Varibles Section************")
myVarible1="Pyton";
myVarible2="is"
myVarible3="Good Lanhage";
print(myVarible1,myVarible2,myVarible3);#multi[le values printing
print(myVarible3+myVarible1)#+ conactionoperator 2) for number it can works as mathamatical operator


#4)global vs local varibles
print("******global vs local varibles*******")

globalVarible=4;
def loacl_Varible():
    localVarible=1;
    print(localVarible)
    print(globalVarible)
loacl_Varible()#function calling
#print(localVarible)# it gives an error because it is declarade in nside function

#pyton operators
print("******Operators*******")

print("**Aethamatic Operator***")
print(2+4)#plus operator
print(4-2)#minus operator
print(4*2)#multiplicaton operator
print(4/2)#divison operator
print(4%2)#modulas operator which gives remainder
print(4**3)#power operator
print(7//3)# floor divison opereator which will give nearset whole number
print("**Assignmenet Opertaors**")
assignment1=2;#assigning value to the varible
print(assignment1);
assignment1+=2;# this is equals to (assignment1+2)
print(assignment1)
assignment1-=2;#(assignment1-2)
print(assignment1)
print("like wise all arthamatic operations are being evaluted");
print("**Comaprision Operators**")
print("Comaprision equals",2==8);
print("Comaprision not equal",2!=8);
print("Comaprision grater then",2>8);
print("Comaprision grater the oe equals",8>=2);
print("Comaprision less then ",2<8)
print("Comaprision less the or equlas to",2<=8);

print("***Logical operators*")
def logical_conditions():
    if(2<4&2<7):
        print("this statement is true");
    else:
        print("obsevrve the above logical operator")
    if(2<1|2<4):
        print("thois is logic or any one statement is true this will return the true condition")
    else:
        print("this is logical OR operator plz observe carefully")
logical_conditions();

print("this is some idea about te deffernet operators in python and also some operators are still there but we not discussed at this momment");
print("Welcome to Avinys Solutions.....!!!!!")


#there are more operators are there but not reaquired this time when situvation comes i will explain
