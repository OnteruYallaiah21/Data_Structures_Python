import array 
my_Array1=array.array('i',[2,4,5,6,7,8,6,5,64,5,64,54])
my_Array2=array.array('d',[1.2,3.4,5.676,3,9876])
print(my_Array1)
print(my_Array2)
def traversalArry(array):
    for i in array:
        print(i)
        
traversalArry(my_Array1)
