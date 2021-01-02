
lis1 = [10,12,11,13,14,15]

print([i%2 != 0 for i in range(len(lis1))])


odd_nums = [num for num in lis1 if num%2 != 0]
print(odd_nums)