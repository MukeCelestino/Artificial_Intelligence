class Student:
    def __init__(self, name, id, gpa=0.0):
        self.name = name
        self.id = id
        self.gpa = gpa

    def __str__(self):
        return f"{self.name} has id {self.id} with a GPA of {self.gpa}"

x = Student("John", 900123456, 3.8)
y = Student(42, 9000000584, 3.2)
z = Student("Freshman", 900123156)
print(x.name)
print(x)
print(y)
print(z)



from collections import deque
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.popleft()
print(q)
s = deque()
s.append(5)
s.append(6)
s.append(7)
print(s)
s.pop()
print(s)

x = [1, 2, 3]
x.pop(0)
print(x)
