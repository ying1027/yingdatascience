#problem 1
f=open('IMDB-Movie-Data.csv',"rt")
k=f.readlines()
f.close()

#print(k)


list1=[]
for i in k:
    A=i.split(',')
    list1.append(A)
list1.remove(['Rank', 'Title', 'Genre', 'Director', 'Actors', 'Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore\n'])
#print(list1)
   


# QUESTION1:

dict1={}   
for i in list1 :
    if '2016' in i :
        dict1.setdefault(i[7],i[1])        
list2=list(dict1.keys())

#print(list1)
a=max(list2)
list2.remove(a)
b=max(list2)
list2.remove(b)
c=max(list2)
print('Top 3 ranking moive:' ,dict1[a],'%s' %('/'),dict1[b],' %s' %('/'), dict1[c])

#QUESTION2 :         
list21=[]
for i in range(len(list1)) :
    list18=list1[i][4].split('|')
    
   # print(list18)
    for actors in list18 :
        list20=[]
        if list1[i][9] != '' :
            list20.append(actors)
            list20.append((list1[i][9]))
            list21.append(list20)
            
#print(list21)   

list22=[]   
for i in range(len(list21)) :
    for l in range(len(list21)): 
        if i != l :
            if list21[i][0] == list21 [l][0] :
                list21[i].append(list21[l][1])
                list22.append(list21[i])
#print(list22) 
dict7={}
var1=0  
for i in list22 :
    dict7[i[0]]=[]
    dict7[i[0]].append(list22[var1][1:])
    var1=var1+1  

list24=list(dict7.keys())    
list23=list(dict7.values())
print(list23)
print(list24)

ave=[]
float2=[]
for i in list23 :
    float1=[]
    for idx in i:
        for m in idx :
            n=float(m)
            float1.append(n)
            if float1 not in float2 :
                float2.append(float1)
#print(float2)                
ave=[]
sum2=[]
sum1=0
for i in float2 :
    n=0
    for m in i :
        sum1=sum(i)
        n=n+1
    aves=sum1/n
    ave.append(aves)

      
dict8={}
for i in range(len(list24)) :
    for i in range(len(ave)):
        dict8.setdefault(ave[i],list24[i])       
ave1=list(dict8.keys())
ave1.sort(reverse=True) 

#print(dict8)

n=ave1[0] 

print('The actor generating the highest average revenue? ',dict8[n])#用key對應value值

#Question 3 :
    
list6=[]
for i in list1 :
    list6.append(i[4])
    list6.append(i[7])

dict5={}
for i in list1 :
    for index in i :
        x=i[4]
        y=i[7]
        dict5.setdefault(x,y)
    
list8=list(dict5.keys())
list9=list(dict5.values())

list10=[]
for i in list8:
    i=i.split('|')
    list10.append(i)


list11=[]
for i in list10:
    for idx in i:
        if ' Emma Watson' in i :
            g='|'.join(i)
            list11.append(g)

list13=[]
for i in list11 :
    if i not in list13 :
        list13.append(i)
    
list12=[]
for i in list13 :
    for keys in dict5 :
        if i in keys :
            list12.append(dict5[keys])
     
list14=[]
for i in list12 :
    i=float(i)
    list14.append(i)

sum1=0
for i in list14 :
    sum1 += i
ave=sum1/len(list14)
print('The average rating of Emma Watson’s movies?',float(ave))
                       
#print(dict5)
#print(list9)
#print(list8)    
#print(g)  
#print(list11) 
#print(len(list11))
#print(list12)  
#print(k)

#QUESTION4

list24=[]
for i in range(len(list1)) :
    directors=list1[i][3]
    actors=list1[i][4].split('|')
    #print(directors)
    directors_ =[]
    directors_.append(directors)
    directors_.append(actors)
    list24.append(directors_)
    
#print(list24)

dict5={}    
list25=[]
for i in range(len(list24)) :
    actors=[]
    for l in range(len(list24)) :
        if list24[l][0]==list24[i][0] :
            actors.append(list24[l][1])
        actor=[]
        for m in actors :
            for n in m :
                if n not in actor :
                    actor.append(n)
            
    dict5.setdefault(list24[i][0],actor)

list26=list(dict5.values())
print(list26)
list27=[]
for i in list26 :
    num1=len(i)
    list27.append(num1)
    
print(list27)

dict6={}
for i in range(len(list24)) :
    for i in range(len(list27)) :
        dict6.setdefault(list24[i][0],list27[i])
        
print(dict6)    

list28=list(dict6.values())
print(list28)
list29=list28.sort(reverse=True)
print(list28)

'''
list29=[]
for i in list28 :
    no=max(list28)
    if i =no :
'''        
str5=max(list28)
list28.remove(str5)
str6=max(list28)
list28.remove(str6)

str7=max(list28)
new_dict6={v:k for k,v in dict6.items()}
#print(dict6)
print('Top-3 directors who collaborate with the most actors?')
print('top1:',new_dict6[str5] )
print('top2:',new_dict6[str6] )
print('top3:',new_dict6[str7])



        
    

    
        

    







        
        

        

    




        
        
        
        



       



    


    

    


    
