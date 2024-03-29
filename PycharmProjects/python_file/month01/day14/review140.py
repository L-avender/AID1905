"""
    复习
        面向对象：考虑问题从对象的角度出发
        抽象：从多个事物中，舍弃个别的、非本质的特征（不重要）抽出共性的本质（重要的）过程
        三大特征：
            封装：将每个变化点单独分解到不同的类中
            继承：重用现有类的功能和概念，并在此基础上进行扩展
                  严禁代码复用；主要用于统一概念
            多态：调用父类“抽象的”方法，执行子类“具体的”方法
        设计原则
            开闭原则：允许增加新功能，不允许修改客户端代码
            单一职责：有且只有一个改变的原因
            依赖倒置：调用抽象（父类），不要调用具体（子类）：
                    抽象不要依赖具体
            组合复用：如果仅仅是代码上的复用，优先使用组合
        类与类关系
            泛化（继承）
            关联（做成成员变量）
            依赖（做成方法参数）
"""