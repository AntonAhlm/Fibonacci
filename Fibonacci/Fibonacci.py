a=0
tal1=1
tal2=0

while a<40:
    while a<9: 
       a+=1
       if a % 2 == 0:
           if tal2>2 or tal1>2: 
               print("Tal",a," :",tal1, "\t\t Kvot:",tal1/tal2 )
               tal2+=tal1 
           else: 
               print("Tal",a," :",tal1 )
               tal2+=tal1 

       else :
           if tal2>2 or tal1>2: 
               print("Tal",a," :",tal2, "\t\t Kvot:",tal2/tal1)  
               tal1+=tal2
           else:
               print("Tal",a," :",tal2,) 
               tal1+=tal2
           


    while a>=9 and a<26:
         a+=1
         if a % 2 == 0:
            print("Tal",a,":",tal1, "\t\t Kvot:",tal1/tal2  )
            tal2+=tal1
         else :
            print("Tal",a,":",tal2, "\t\t Kvot:",tal2/tal1 )
            tal1+=tal2


    a+=1
    if a % 2 == 0:
        print("Tal",a,":",tal1, "\t Kvot:",tal1/tal2  )
        tal2+=tal1
    else :
        print("Tal",a,":",tal2, "\t Kvot:",tal2/tal1 )
        tal1+=tal2
