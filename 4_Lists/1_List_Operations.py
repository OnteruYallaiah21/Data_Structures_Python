
listCraetion=["Yallesh","Ganesh","Khadar","Rudra Reddy"];
print("**List Creation is demo Here**")
print(listCraetion);
#printing length of list we have to use len() method in list
print("Printing Length Or size of python list using the len method",len(listCraetion));
print("**Accesing the list element in list by indexing**")
print(listCraetion[1]);
print("**list Can save deffent data type at a same time**")

mydefferentDatTypeList=["Yallesh",4,'y',7.89];

print("Printing all ements in the list**",mydefferentDatTypeList)

print("Printing the bdata type index element in List",type(mydefferentDatTypeList[0]),"\n",type(mydefferentDatTypeList[1]),"\n",type(mydefferentDatTypeList[2]))

print("**Accesing the element from Last indexing**");

print(mydefferentDatTypeList[-1]);

print("**We can specify the range of indexing values meand Between the values**");

print(mydefferentDatTypeList[0:9]);

print("*** Change The List Elements ***")

mydefferentDatTypeList[0]="Yallaiah Is doing the master now";

print("Printing the List After changing the i adding the value to the index is replace with another\n",mydefferentDatTypeList)

print("**In python we have chance to Add the multiple range of elements in beteen the List Index**")

mydefferentDatTypeList[1:4]=["changed Elemet","new Element",9.45];
print("printing the elements after adding new elemnts by replacing before elemnts in list collection**=>",mydefferentDatTypeList)
print("***Adding another List element with Oud distrubing the previos elemnt with insert() method****");
mydefferentDatTypeList.insert(0,"Insertion Of new Elemnt");
print(mydefferentDatTypeList)
print("******Adding Elemets in the Last index of List with another methods*******")
print("In this section we are going to explose some methods \nappend()\ninsert()\nextend()")
mydefferentDatTypeList.append("Append The Last elemnt in List")
print(mydefferentDatTypeList)
mydefferentDatTypeList.insert(1,"second Element Inserting")#this method uses the index values to addd any element in List collection
print("after inserting List=>",mydefferentDatTypeList)
myIntergeraList=[2,3,4,5,6,7,8,5,43]
myStringList=["Apple","samsung","motorolo"]
myStringList.extend(myIntergeraList);
print("After using the Ectend Method to club another Itera ble Object Like List,Set,Dictonaries",myStringList)
print("*****Removing the Elemet from the List*******")
#REMOVING SPECIFIC ELEMENT
myStringList.remove("Apple");
print("Printing the Combining List after remove the element",myStringList)
#IF LIST CONTAINS DUPLICATE VALUES IT WILL REMOVE THE FIRST ELEMENT FROM lIST
myStringList[0:2]=["Apple","Apple"];
print("After adding the multiple duplicate values using thr range concept",myStringList)
myStringList.remove("Apple");
print("after removing the value from List",myStringList)
