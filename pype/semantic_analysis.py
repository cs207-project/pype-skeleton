from .ast import *

class PrettyPrint(ASTVisitor):
  def __init__(self):
    pass
  def visit(self, node):
    print (node.__class__.__name__)

class CheckSingleAssignment(ASTVisitor):
  def __init__(self):
    pass # TODO
  def visit(self, node):
    pass # TODO
