import array
def remove_duplicates(nums_Array):
    i=0;
    for x in nums_Array:
        if(x[i]==x[i+1]):
            print(x[i])
        i+1;
remove_duplicates([1,1,2,3,4,4,4,4,4,5,6,78]) 