#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
l=[]
l1=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(n):
    num=int(input("Enter %d number:" %(i+1)))
    l.append(num)
for j in l:
    sq=j**2
    l1.append(sq)
print("Squared list={}".format(l1))
