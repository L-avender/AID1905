"""
rerex1.py re 模块　功能函数
生成ｍａｔｃｈ对象的函数
"""
import  re
s="今年是２０１９年，建国７０周年"
pattern=r"\d+"
a=re.finditer(pattern,s)
for i in a:
    print(i.group())#获取ｍａｔｃｈ对象对应内容
try:
   m=re.fullmatch(r"[\w,，]+",s)
   print(m.group())
except:
    print("未匹配到")
m=re.match(r"[\w,，]+",s)
print(m.group())
m=re.search(r"\w+",s)
print(m.group())