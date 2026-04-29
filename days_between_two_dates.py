from datetime import date
#write your code here...
d3=input()
d4=input()
d1=date.fromisoformat(d3)
d2=date.fromisoformat(d4)
d5=d2-d1
print(d5.days)
