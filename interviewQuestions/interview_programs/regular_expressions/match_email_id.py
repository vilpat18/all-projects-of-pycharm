import re

emails = "abc@gmail.com hanmant@gmail.com ABCgmail.com abc.125@yahoo.com abc@yahoo.in"


print('matching patterns: ',len(re.findall("\w[a-zA-z0-9.$]{1,50}@[a-z]{1,10}.\w[a-z]{2,3}",emails)))