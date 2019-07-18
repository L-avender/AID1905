"""
regex.py re模块　功能函数演示
"""
import re

# 目标字符串
s = "Alex:1994,Sunny:1996"
pattern = r"\w+:\d+"  # 正则表达式

# re 模块调用findall
l = re.findall(pattern, s)
print(l)

print(re.findall(r"\w+:\d+", s))

print(re.split(r"[:,]", s))

print(re.sub(r":", "-", s))
print(re.subn(r":", "-", s, 1))

