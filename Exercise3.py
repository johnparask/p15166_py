import string

sentence=input("Insert Sentence and prepare for ROT_13! >> ")
S=list(sentence)

U="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Upper=list(U)
L="abcdefghijklmnopqrstuvwxyz"
Lower=list(L)

def out_range(c):
    c=c+13
    if c>25:
        c=c-26
    return c    

new_s = ""

for i in S:
    a=0 
    c_x=0
    for x in Upper:
        if (i==x):
            new_s+=Upper[out_range(c_x)]
            a+=1
        c_x+=1
        
    c_y=0        
    for y in Lower:
        if i==y:
            new_s+=Lower[out_range(c_y)]
            a+=1
        c_y+=1     

    if a==0:    #if a stays zero, 'i' is not an upper nor a lower case letter...we leave it as it is...
        new_s+=i


print ("Excuse me?!Did you just say?")  
print (new_s) 

