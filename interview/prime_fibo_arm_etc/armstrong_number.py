num = 153

sum = 0
temp = num

while temp>0:
    digit = temp%10
    sum+= digit**3
    temp //= 10

if sum == num :
    print('YESSSSSSS ITS ARMSTRONG NUMBER')