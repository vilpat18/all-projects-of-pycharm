d = {i:i**2 for i in range(10)}
print(d)

org_dict = {'a':10,'b':19,'c':40,'d':50}

dict_comp = {key:value for (key,value) in org_dict.items() if value % 2 == 0}
print(dict_comp)

dict_comp_odd = {k:v for (k,v) in org_dict.items() if v % 2 != 0}
print(dict_comp_odd)