# node.py - 08/01/2025

# copied over from my tower of hanoi project. 

# will be used to create and access nodes for the linked list in main.py
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_next_node(self, link_node):
    self.link_node = link_node
    
  def get_next_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value
  
  
# github.com/tobias-sava