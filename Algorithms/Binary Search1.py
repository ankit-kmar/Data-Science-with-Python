#Binary Search algorithms works on sorted elements. This is because it follows a Divide and Conquer approach where the list is continuously being divided and sub-divided, 
#based on the possibility of the searched element being present in any one of the sub-parts. If item is lesser than the middle element, it is searched in one part, otherwise in the other half.
#A sorting function is not being written as it would hamper the location of the item being searched.
#Time complexity of this algorithm is O(log n).
#Input provided has to be sorted.

n=int(input("Enter number of elements:"))
List=[]
print("Enter the elements-")
for i in range (0,n):
    e=int(input())
    List.append(e)
item=int(input("Enter the element to be searched:"))	
beg=0
end=n-1
flag=0
while (beg<=end):
    mid=(beg+end)//2
    if (List[mid]==item):
        loc=mid+1
        flag=1
        break
    elif (List[mid]<item):
        beg=mid+1
    else:
        end=mid-1
if (flag==1):
    print(item,"present at location",loc)
else:
    print(item,"not present.")
