set_element = {10,12,11,10,12,9,8,14}
print(set_element)
set_compre = {i for i in set_element if i%2 ==0}
print(set_compre)

set_str = {'rohit','ajay','atul','mahesh','sachin','rohit'}
print(set_str)
set_str_comp = {a for a in set_str if a in 'sachin'}
print(set_str_comp)
