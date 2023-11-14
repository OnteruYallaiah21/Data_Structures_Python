numDyas=int(input("How any dayas temparture yoiu need=>"));
totaldayas=0;
list1=[];

for i in range(1,numDyas+1):
     nextday=int(input("Day"+str(i)+"'s High temparature=>"))
     totaldayas+=nextday;
     list1.append(totaldayas);
     print(totaldayas)
avrage=round(totaldayas/numDyas,2);
print("\n Avarage ",avrage)
print("The size of List=>",len(list1)) 
for i in list1:
    print(i)
    if(i>avrage):
        print("The Day temparature is more then avarage temparature=>",i)
