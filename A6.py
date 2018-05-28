''' Q.6- Print the following patterns: 
*
**
***
****
'''
for i in range(5):
    for j in range(i):
        print('*',end='')
    print()
