"""
    列表助手模块
"""

class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target,func_condition):
        """
            通用的查找某个条件的所有元素方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素,生成器类型.
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(list_target,func_condition):
        """
            通用的查找某个条件的单个元素方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素
        """
        for item in list_target:
            if func_condition(item):
                return item

    @staticmethod
    def find_count(list_target, func_condition):
        count=0
        """
            通用的查找满足某个条件的元素的个数
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素的个数
        """
        for item in list_target:
            if func_condition(item):
                count+=1
        return count

    @staticmethod
    def True_Flase(list_target, func_condition):
        """4. 在list_helper中增加判断是否存在某个对象的方法.返回值:true/false
               案例1:判断敌人列表中是否存在"成昆"
               案例2:判断敌人列表中是否攻击力小于5或者防御力小于10的敌人.
        """
        """
            通用的判断列表中是否存在满足条件的元素
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 是否满足，满足返回True，不满足返回Flase
        """
        for item in list_target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def all_sum(list_target, func_condition):
        """4. 在list_helper中增加判断是否存在某个对象的方法.返回值:true/false
               案例1:判断敌人列表中是否存在"成昆"
               案例2:判断敌人列表中是否攻击力小于5或者防御力小于10的敌人.
        """
        """
            通用的求和
        :param list_target: 需要操作列表
        :param func_condition: 需要求和的元素,函数类型
                函数名(参数) --> bool
        :return: 返回求和值
        """
        list=[]
        for item in list_target:
            list.append(func_condition(item))
        return sum(list)

    @staticmethod
    def screen(list_target, func_condition):
        """

        :param list_target:
        :param func_condition:
        :return:
        """
        list=[]
        for item in list_target:
            list.append(func_condition(item))
        return list

    @staticmethod
    def get_biggest(list_target, func_condition):
        """
        通用的取最大值
        :param list_target:目标列表
        :param func_condition:需要取值的项，类型为函数
        :return:返回最大值
        """
        list = []
        for item in list_target:
            list.append(func_condition(item))
        return max(list)

    @staticmethod
    def least(list_target, func_condition):
        """
         取最小值
        :param list_target:
        :param func_condition:
        :return:
        """
        least = list_target[0]
        for item in list_target:
            if func_condition(least) > func_condition(item):
                least = item
        return least

    @staticmethod
    def descending_order(list_target, func_condition):
        """
        降序排列
        :param list_target:
        :param func_condition:
        :return:
        """
        for c in range(len(list_target) - 1):
            for a in range(c + 1, len(list_target)):
                if func_condition(list_target[c])<func_condition(list_target[a]):
                    list_target[c], list_target[a] = list_target[a], list_target[c]
        return list_target

    @staticmethod
    def delete(list_target, func_condition):
        """
        删除满足条件的元素
        :param list_target:
        :param func_condition:
        :return:
        """
        for c in range(len(list_target)):
            for item in list_target:
                if func_condition(item):
                    list_target.remove(item)
        return list_target