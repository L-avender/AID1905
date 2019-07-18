class Student:
    def __init__(self,name,age,score,sex):
        self.name=name
        self.age=age
        self.score=score
        self.sex=sex
    def print_self_info(self):
        input_student_info()
        print_student_info()

def print_student_info():
    input_student_info()
    for dict_info in list_student_info:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              % (dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))
    # 获取第一个学生信息
    dict_info = list_student_info[0]
    print("第一个录入的是：%s,年龄是%d,成绩是%d,性别是%s" % (
            dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))


def input_student_info():
        list_student_info = []
        while True:
            name = input("请输入姓名：")
            if name == "":
                break
            age = int(input("请输入年龄："))
            score = int(input("请输入成绩："))
            sex = input("请输入性别：")
            dict_info = {"name": name, "age": age, "score": score, "sex": sex}
            list_student_info.append(dict_info)
        return list_student_info
