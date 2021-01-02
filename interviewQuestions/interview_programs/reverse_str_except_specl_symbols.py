str1 = 'abc@#*d$c'

temp = []

for i in str1:
    if i.isalpha():
        temp.append(i)

print(temp)

# str2 = 'ab@#$BH&*'
# tem = []
# index = -1
# for i in range(len(str2)-1,int(len(str2)/2),-1):
#     if str2[i].isalpha():
#         tem = str2[i]
#         while True:
#             index +=1
#             if str2[index].isalpha():
#                 str2[i]=str2[index]
#                 str2[index]=tem
#                 break
#     print(str2)
def reverseSting(text):
    index = -1

    # Loop from last index untill half of the index
    for i in range(len(text) - 1, int(len(text) / 2), -1):

        # match character is alphabet or not
        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text


# Driver code
string = "a!!!b.c.d,e'f,ghi"
print("Input string: ", string)
string = reverseSting(list(string))
print("Output string: ", "".join(string))

# This code is contributed by shiva9610



