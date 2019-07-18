# 导入方式1
# 本质：使用变量名module01关联模块地址
import module01
module01.fun01()
my02 = module01.MyClass02()
my02.fun02()

# as 为导入的成员其另外一个名称
import module01 as m01
m01.fun01()
my02 = m01.MyClass02()
my02.fun02()
