class ParseTree(object):

    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def traverse(self):
        if self.left is None and self.right is None:
            return self.value
        else:
            return [self.left.traverse(), self.value, self.right.traverse()]

    def evaluate(self):
        if self.left is None and self.right is None:
            return self.value
        elif self.value == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.value == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.value == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.value == '/':
            return self.left.evaluate() / self.right.evaluate()


def build_parse_tree(tokens):
    root = ParseTree()
    cur = root
    for token in tokens:
        if token == '(':
            cur.left = ParseTree(parent=cur)
            cur = cur.left
        elif token == ')':
            cur = cur.parent
        elif token in ['+', '-', '*', '/']:
            cur.value = token
            cur.right = ParseTree(parent=cur)
            cur = cur.right
        elif isinstance(token, int):
            cur.value = token
            cur = cur.parent
    return root

def tokenize(expr):
    operators = ['(', ')', '+', '-', '*', '/']
    tokens = list()
    i = 0
    while i < len(expr):
        if expr[i] in operators:
            tokens.append(expr[i])
            i += 1
        elif expr[i].isdigit():
            j = i
            while i < len(expr) and expr[i].isdigit():
                i += 1
            tokens.append(int(expr[j:i]))
        else:
            i += 1
    return tokens

def evaluate(expr):
    tokens = tokenize(expr)
    pt = build_parse_tree(tokens)
    print pt.traverse()
    return pt.evaluate()

print evaluate('(300 +400)')
print evaluate('((3+4) * 6)')
print evaluate('(10*(3+7) )')
