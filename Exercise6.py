from datetime import date

Day = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
Month = ["January","February","March","April","May","June","July","August","September","Octomber","November","December"]
Length = [31,28,31,30,31,30,31,31,30,31,30,31]

#I know that the 10th of February 2018 was Saturday aka Day[6]

d0=input("Insert Date... \n")
d01=d0.split(" ")

count=0
m=0

for i in Month:
    if d01[0]==i:
        m=count
    count+=1

m+=1
y=int(d01[1])
print (m,y)

d1 = date(2018, 2, 10)
d2 = date(y, m, 1) # the first of the requested month

delta=d1-d2
dif=delta.days
print(dif)

d=dif%7
first=Day[6-d] #I now know the first day of the requested month
print(first)
l=Length[m-1]

if m==2: #check if this is a leap year for February
    if (y%4==0):
        l=29
print ("========================")
print ("========================")
print ("")
print ("")
print ("------- ",d0," ------- \n \n")
print ("S  M  T  W  T  F  S \n")


count=0

while(True):
    if first==Day[count]:
        break
    count+=1

final=[] 
for i in range (0,count):
    final.append(" _")  #putting a gap in the begging of the month
for i in range (0,l):
    if i+1<10:
        final.append(" "+ str(i+1))
    else:    
        final.append(str(i+1))

week=""
count=0
for i in final:    
    week+=i+(" ")
    if (count==6 or count==13 or count == 20 or count == 27 or count == 34):
        print (week)
        week=""
    count+=1    
if week!="":
    print (week)




