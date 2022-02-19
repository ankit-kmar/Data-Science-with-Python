# a ---> array to be sorted
# p,r ---> segment of array (sub array) being sorted
# q -----> index of the partition

def divide(a,p,r):
	k=a[r]
	q=p
	for i in range(p,r):
		if a[i]<=k:
			a[i],a[q]=a[q],a[i]
			q+=1
	
	a[q],a[r]=a[r],a[q]
	return q

def quick_sort(a,p,r):
	if p>=r:
		return
	
	q=divide(a,p,r)
	
	quick_sort(a,p,q-1)     # recurse on left sub-array
	quick_sort(a,q+1,r)     # recurse on right sub-array

n=int(input())
a=list(map(int,input().split()))

quick_sort(a,0,n-1)
print(*a)