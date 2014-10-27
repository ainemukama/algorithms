class Stack(object):

    def __init__(self):
        self.arr = list()

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        del self.arr[-1]

    def peek(self):
        return self.arr[-1]

    def size(self):
        return len(self.arr)

def is_balanced(s):
    stack = Stack()
    for c in s:
        if c == '(':
            stack.push(c)
        elif c == ')':
            if stack.size() == 0:
                return False
            else:
                stack.pop()
    if stack.size() > 0:
        return False
    else:
        return True

print is_balanced('')
print is_balanced('()')
print is_balanced('(())')
print is_balanced('(')
print is_balanced(')')
print is_balanced('(()')
print is_balanced('())')
