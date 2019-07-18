import re
s='''hello is isbeijing'''
pattern=r'(l)|i'
l= re.findall(pattern,s)
print(l)
