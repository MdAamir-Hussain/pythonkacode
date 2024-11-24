def binarysearch(arr, target, low , high):
	if low > high:
		return -1


	mid = (low + high)//2  #find the middle element

	if arr[mid] == target:
		return mid 
	elif arr[mid] > target:
		return binarysearch(arr, target, low ,mid-1)
	else:
		return binarysearch(arr,target, mid+1,high)



#example usage

arr = [1,3,5,7,9,11,13,15]

target = 7 
result = binarysearch(arr, target, 0, len(arr) -1)

if result !=-1:
	print(f"Element {target} is at index {result}")
else: 
	print(f"Element {target} not found in the array")