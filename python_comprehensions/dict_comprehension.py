# using for loop

list_cube = [1,2,3,4,5,6,7,8,9,10]
output_dict = {}
for i in list_cube:
    if i%3 == 0:
        output_dict[i] = i**3

print(output_dict)

# for using dict compehensions

out_dict = {i:i**3 for i in list_cube if i%3==0}
print(out_dict)