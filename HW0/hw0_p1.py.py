#(x+2*y)(x^3+3*y)(x+55*y)
#(x-2*y)(2356*x^33+3*y)(235*x+55*y)
#(2*x+3*y+4*z)
#(2*x+3*y+4*z)(xy2)

a=input('input the polynomials:')
list1=list(a)

list2=[]
for i in list1 :
    b=list1.index('(')
    c=list1.index(')')
    list2.append(list1[b+1:c])
    list1.remove('(')
    list1.remove(')')
    if  '(' not in list1 :
        break

print(list2)


for i in list2:
    for idx in i :
        if idx.isdigit() is True :
            m=i.index(idx)
            if i[m].isdigit() is True :
                i[m-1] = i[m] + i[m+1]+i[m-1]
            elif i[m].isdigit() is True :
                i[m] = i[m] + i[m]
                i.pop(m)
            
            
                
print(list2)

for i in list2:
    if '-' in i :
        n=i.index('-')
        i[n]=i[n]+i[n+1]
        i.pop(n+1)
        
for i in list2:
    for idx in i :
        if '*' in i :
            y=i.index('*')
            i[y-1]=i[y-1] + i[y] + i[y+1]
            i.pop(y+1)
            i.pop(y)
    
for i in list2:
    for idx in i :
        if '+' in  i :
            i.remove('+')
            



for i in list2:
    for idx in i :
        if '^' in i :
            z=i.index('^')
            i[z-1]=i[z-1] + i[z] + i[z+1]
            i.pop(z+1)
            i.pop(z)
            

    

           
        
        



        

        
    
    
    
    







    
