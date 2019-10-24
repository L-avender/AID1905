import xlsxwriter
import xlrd
from selenium import webdriver
import time
#####自动写入excel文件
#准备数据
data='张三'
#打开excel文件
workbook=xlsxwriter.Workbook('ex01.xlsx')
#打开一个sheet表
worksheet=workbook.add_worksheet()
#设置单元格初始行与列
row,col=0,0
#将数据写入目标单元格
worksheet.write(row,col,data)
#保存并关闭excel文档
workbook.close()

#####读取excel文档内容
#打开excel文件
workbook=xlrd.open_workbook('ex01.xlsx')
#获取第一张表格对象
sheet_name=workbook.sheet_by_index(0)
#读取目标单元格数据
data=sheet_name.cell_value(0,0)


#####selenium自动测试框架
####配置chrome文件
#创建Chrome测试
driver=webdriver.Chrome()
#目标网页
url='https://docs.qq.com/desktop/'
#进入目标网页
driver.get(url)
#存在iframe框架,必须先切换到iframe框架下
#切换到iframe框架下
login_frame = driver.find_element_by_id('login_frame')
driver.switch_to.frame(login_frame)
#根据id等进行元素定位
driver.find_element_by_id("switcher_plogin").click()
driver.find_element_by_id('u').send_keys('登录账号')
driver.find_element_by_id('p').send_keys('账号密码')
driver.find_element_by_id('login_button').click()
time.sleep(3)
#当前窗口,页面刷新后,需要重新切换句柄
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_xpath('//*[@id="pages"]/div/div/div/div[2]/div/div[2]/button').click()
driver.find_element_by_xpath('//*[@id="pages"]/div/div/div/div[2]/div/div[2]/div/div/ul[1]/li[2]').click()
time.sleep(3)
#新建窗口,跳转后,需切换到新窗口
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath('//*[@id="thumb-20001"]').click()
time.sleep(3)
#当前窗口,页面刷新后,需要重新切换到当前窗口句柄
driver.switch_to.window(driver.current_window_handle)
time.sleep(10)
#定位元素,并填入目标值
driver.find_element_by_xpath('//*[@id="alloy-rich-text-editor"]').send_keys(data)







