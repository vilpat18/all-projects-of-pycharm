""" Python list comprehension support is great for
 creating readable but compact code for representing mathematical ideas """

A = [a for a in range(20) if a%2==0]
B = [b for b in range(20) if b%3==0]
C = [c for c in range(20) if c in A and c in B]

print(A,'\n',B,'\n',C)

# simple example
square = []
for i in range(20):
    square.append(i*i)
print(square)

# with list comprehensions
square = [i*i for i in range(20)]
print(square)

""" for different data types for. example strings """
verbs = ['eat','sleep','walk','talk']
ing = [verb + 'ing' for verb in verbs ]
print(ing)

sentence = "india is my country"
vow = [i for i in sentence if i in 'aeiou']
print(vow)