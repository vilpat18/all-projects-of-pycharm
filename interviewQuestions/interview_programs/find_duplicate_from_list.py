# list1 = [10,10,22,22,14,14,78,99]
#
# dup = []
# for i in list1:
#     if i not in dup:
#         dup.append(i)
#
# print(dup)


def my_func(a,*b):
    # print('first argument: ',a)
    # print('variable arguments: ',*b)
    return a*b


res = my_func(5,20,30,40)
print(res)