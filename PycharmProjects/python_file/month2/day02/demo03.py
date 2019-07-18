"""
squeue.py 队列的顺序存储
思路分析：
1. 基于列表完成数据存储
2. 通过封装规定数据操作
3. 先确定列表的哪一段作为队头
"""
# 自定义队列异常
class QueueError(Exception):
    pass

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

# 队列操作
class SQueue:
    # 初始化
    def __init__(self):
        self._elems = []

    # 判断队列是否为空
    def is_empty(self):
        return self._elems ==[]

    # 入队
    def enqueue(self,val):
        self._elems.append(val)

    # 出队
    def dequeue(self):
        if not self._elems:
            raise QueueError("Stack is empty")
        # 弹出并返回
        return self._elems.pop(0)
