#Q.4- From a list containing ints, strings and floats, make three lists to store them separately 
li,lf,ls=[],[],[]
l=['samyak',12.5,10,23,'ajay',89.0,'akash',45,21,'sanjay',9.8]
for j in l:
    if type(j)==int:
        li.append(j)
    elif type(j)==float:
        lf.append(j)
    elif type(j)==str:
        ls.append(j)
print("Integer list={}".format(li))
print("Floated list={}".format(lf))
print("String list={}".format(ls))
