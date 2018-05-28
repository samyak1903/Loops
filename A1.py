#Q.1- Take 10 integers from user and print it on screen.
l=[]
for i in range(10):
    n=int(input("Enter %d number:" %(i+1)))
    l.append(n)
for j in l:
    print("Numbers are: ",j)
