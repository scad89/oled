a = int(input()) 
b = int(input())
b2 = b*2
b3 = b*3
countb = 0
countb2 = 0
countb3 = 0
while a >= b:
   if b3 >= a:
       a = a - b3
       countb3 = countb3 +1
   if b2 >= a:
       a = a - b2
       countb2 = countb2 +1
    a = a - b
    countb = count +1
print(countb + countb2*2 + countb3*3)

# изменения