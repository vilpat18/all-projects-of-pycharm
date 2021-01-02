def even_number(n):
    if n%2 ==0:
        return n
my_list = [10,14,5,14,88,8,77,7,8,8]
result = list(filter(even_number,my_list))
print(result)

old_list = [1,2,55,5,8,8,5,88,8,55,88,55,88,66,55,4,8,8,5,56]
new_list = list(filter(lambda n:n%2==0,old_list))
print(new_list)