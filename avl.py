#!/usr/bin/python
import sys
from math import log10

class AvlNode(object):

    def __init__(self, data):
        self.data    = data
        self._left   = None
        self._right  = None
        self._height = 0
        self._factor = 0

    @property
    def factor(self):
        return self._factor

    @property         
    def height(self):
        return self._height
                   
    def _update(self):
        l = self.left._height  if self.left  else -1
        r = self.right._height if self.right else -1
        
        self._height = 1 + max(l, r)
        self._factor = r - l
        
    
    @property
    def left(self):
        return self._left

        
    @left.setter
    def left(self, node):
        self._left = node
        self._update()

        
    @property
    def right(self):
        return self._right


    @right.setter
    def right(self, node):
        self._right = node
        self._update()
    
         
    def __str__(self):
        return '{} ({}, {})'.format(str(self.data), self.factor, self.height)

class AvlTree:
    
    def __init__(self, data = None):
        self.root = None
        
        if data:
            self.insert(data)
        
        
    def _insert(self, root, data):
        if not root:
            return AvlNode(data)
        
        if root.data == data:
            return root
            
        if data < root.data:
            root.left = self._insert(root.left, data)
            
        elif data > root.data:
            root.right = self._insert(root.right, data)
            
        return self._balance(root)

        
    def insert(self, data):
        if type(data) == type([]):
            for d in data:
                self.insert(d)
        else:
            self.root = self._insert(self.root, data)
        
            assert not self.root or 1.44 * log10(len(self)) <= self.height
        
        
    def _remove(self, root, data):
        if root:
            if data == root.data:
                if not root.left or not root.right:
                    root = root.left or root.right
                else:
                    next = root.right
                    
                    while next.left:
                        next = next.left
                        
                    root.data = next.data
                    root.right = self._remove(root.right, next.data) 
                    
            elif data < root.data:
                root.left = self._remove(root.left, data)
            
            elif data > root.data:
                root.right = self._remove(root.right, data)
            
        return self._balance(root)

                
    def remove(self, data):
        if type(data) == type([]):
            for d in data:
                self.remove(d)
        else:
            self.root = self._remove(self.root, data)
        
            assert not self.root or 1.44 * log10(len(self)) <= self.height
        
        
    def _ll_rotation(self, root):
        next       = root.left
        root.left  = next.right
        next.right = root
        
        return next


    def _rr_rotation(self, root):
        next       = root.right
        root.right = next.left
        next.left  = root
        
        return next
    
        
    def _lr_rotation(self, root):
        root.left = self._rr_rotation(root.left)
        
        return self._ll_rotation(root)
    
        
    def _rl_rotation(self, root):
        root.right = self._ll_rotation(root.right)
        
        return self._rr_rotation(root)
    
    
    def _balance(self, root):
        if root:
            if root.factor > 1:
                root = self._rr_rotation(root) if root.right.factor >= 0 \
                  else self._rl_rotation(root)
            elif root.factor < -1:
                root = self._ll_rotation(root) if root.left.factor  <= 0 \
                  else self._lr_rotation(root)
                  
            assert root.factor in [-1, 0, 1]
        
        return root;
    
    
    def _preorder(self, root):
        if root:
            yield root
            for l in self._preorder(root.left):  yield l
            for r in self._preorder(root.right): yield r

        
    def preorder(self):
        return self._preorder(self.root)
        
        
    def _posorder(self, root):
        if root:
            for l in self._posorder(root.left):  yield l
            for r in self._posorder(root.right): yield r
            yield root


    def posorder(self):
        return self._posorder(self.root)
        
        
    def _inorder(self, root):
        if root:
            for l in self._inorder(root.left):  yield l
            yield root
            for r in self._inorder(root.right): yield r


    def inorder(self):
        return self._inorder(self.root)
        
    @property
    def height(self):
        return self.root.height if self.root else -1
        
        
    def __len__(self):
        return sum(1 for _ in self.preorder())
        
        
    def __str__(self):
        def add_prefix(prefix, node):
            return add_prefix(prefix + 2, node.right) \
                 + '\n' + '   ' * prefix + str(node)  \
                 + add_prefix(prefix + 2, node.left)  if node else ''
                 
        return add_prefix(0, self.root)
        

def main():
    avl = AvlTree()
    
    for arg in sys.argv[1:]:
        try:
            n = int(arg)
            
            if n > 0:
                avl.insert(n)
            else:
                avl.remove(-n)
        
        except:
            arg = arg.upper()
            
            if arg == 'PRE':
                print ', '.join([str(node.data) for node in avl.preorder()])
                
            elif arg == 'POS':
                print ', '.join([str(node.data) for node in avl.posorder()])
                
            elif arg == 'IN':
                print ', '.join([str(node.data) for node in avl.inorder()])
                
            elif arg == 'GRA':
                print '\n', '-' * 70,
                print avl


if __name__ == '__main__':
    main()
