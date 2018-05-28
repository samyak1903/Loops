#Q.8- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
l=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(n):
    element=input("Enter %d element:" %(i+1))
    l.append(element)
num=input("Enter the element to be deleted:")
for j in l:
    if j==num:
        l.remove(j)
print("Resulting list={}".format(l))
