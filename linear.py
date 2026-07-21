arr = [10,20,30,40,50]
key = int(input("Enter The Number to search?"))
for i in range(len(arr)):
    if arr[i]==key:
        print("Element fount at index",i)
        break
else:
    print("Element Not Found")
    