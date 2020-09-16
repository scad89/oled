a = int(input()) 
b = int(input())
b2 = b*2
b3 = b*3
countb = 0
countb2 = 0
countb3 = 0
while a >= b:
   if b3 >= a and a != 0:
      a = a - b3
      countb3 =+1
   if b2 >= a and a != 0:
      a = a - b2
      countb2 +=1
   if a != 0 and a >= b:   
      a = a - b
      countb = countb + 1
print(countb + countb2*2 + countb3*3, a)

# комментарии