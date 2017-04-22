
import queue


q = queue.Queue()        # 先进先出

# q.put('22')
# print(q.get())
# print(q.get(timeout=3))
# print(q.get_nowait())

q1 = queue.LifoQueue()    # 后进先出
q1.put('a')
q1.put('b')
q1.put('c')
print(q1.get())
print(q1.get())
print(q1.get())


q2 = queue.PriorityQueue() # 设置优先级
q2.put((1, 'ww'))
q2.put((0, 'xx'))

print(q2.get())
print(q2.get())

