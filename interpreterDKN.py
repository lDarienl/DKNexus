class Expr:
    def accept(self, visitor):
        pass

class Number(Expr):
    def __init__(self, value):
        self.value = value
    
    def accept(self, visitor):
        return visitor.visit_number(self)

class Add(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def accept(self, visitor):
        return visitor.visit_add(self)

class Visitor:
    def visit_number(self, number):
        pass

    def visit_add(self, add):
        pass

class Interpreter(Visitor):
    def visit_number(self, number):
        return number.value

    def visit_add(self, add):
        return add.left.accept(self) + add.right.accept(self)
