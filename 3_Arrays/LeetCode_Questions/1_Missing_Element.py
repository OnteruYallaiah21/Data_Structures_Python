#sum of number by find the n((n+1)/2)

def missing_Number(n):
    ageofYou=int(input("Enter You age is=>"))
    myList=[];
    for n in range(1,n+1):
      myList.append(n);
    sum1=n*(n+1)/2;
    myList.remove(ageofYou+1);
    sum2=sum(myList);
    print("The missing number is =>",(sum1-sum2));
missing_Number(100);