#!/usr/bin/python
'''
Created on 13/01/2013

@author: moisesguimaraes
'''
import unittest, random
from avl import AvlNode, AvlTree


class NodeTestCase(unittest.TestCase):
    
    def test001(self):
        node = AvlNode(42)
        
        self.assertIsNotNone(node)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)
        self.assertEqual(node.height, 0)
        self.assertEqual(node.factor, 0)
        

class AVLTestCase(unittest.TestCase):

    def setUp(self):
        self.avl = AvlTree()

    def test001(self):
        # teste de criacao
        self.assertIsNotNone(self.avl)
        self.assertIsNone(self.avl.root)

    def test002(self):
        # teste de insercao
        self.avl.insert(42)
        self.assertEqual(self.avl.root.data, 42)
        
        self.avl.insert(25)
        self.assertEqual(self.avl.root.left.data, 25)
        
        self.avl.insert(777)
        self.assertEqual(self.avl.root.right.data, 777)
        
    def test003(self):
        # teste de tamanho
        for i in range(1, 10):
            self.avl.insert(i)
            self.assertEqual(i, len(self.avl))
        
    def test004(self):
        #teste de iteradores
        self.avl.insert(range(1, 10))
            
        self.assertEqual([4, 2, 1, 3, 6, 5, 8, 7, 9], [n.data for n in self.avl.preorder()])    
        self.assertEqual([1, 3, 2, 5, 7, 9, 8, 6, 4], [n.data for n in self.avl.posorder()])
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], [n.data for n in self.avl.inorder()])
            
    def test005(self):
        # teste de altura
        self.assertEqual(self.avl.height, -1)
        
        numbers = [42, 25, 777, 12]
        results = [ 0,  1,   1,  2]
        
        for i in range(len(numbers)):
            self.avl.insert(numbers[i])
            self.assertEqual(self.avl.height, results[i])
        
    def test006(self):
        # teste de remocao simples
        self.avl.insert([42, 25, 777])
        
        self.avl.remove(0)
        self.assertEqual(len(self.avl), 3)
        
        self.avl.remove(777)
        self.assertEqual(len(self.avl), 2)
        
        self.assertEqual([42, 25], [n.data for n in self.avl.preorder()])
            
        self.avl.insert(12)
        self.assertEqual(len(self.avl), 3)

        self.avl.remove(25)
        self.assertEqual(len(self.avl), 2)
        
        self.assertEqual([42, 12], [n.data for n in self.avl.preorder()])
        
    def test007(self):
        # teste de remocao complexa
        self.avl.insert([42, 25, 777, 12, 36, 555, 999, 600])
            
        self.avl.remove(42)
        self.assertEqual(self.avl.root.data, 555)
        
        self.avl.remove(555)
        self.assertEqual(self.avl.root.data, 600)
            
    def test008(self):
        # teste de balanceamento durante insercao
        data_set = [
        [7, 5, 3], #ll
        [7, 3, 5], #lr
        [3, 5, 7], #rr
        [3, 7, 5]  #rl
        ]
        
        for data in data_set:
            avl = AvlTree(data)
            
            self.assertEqual([5, 3, 7], [n.data for n in avl.preorder()])
    
    def test009(self):
        # teste de balanceamento durante remocao
        data_set = [
        [7, 9, 5, 3], #ll
        [7, 9, 3, 5], #lr
        [3, 1, 5, 7], #rr
        [3, 1, 7, 5]  #rl
        ]

        for data in data_set:
            avl = AvlTree(data)
            
            avl.remove(data[1])
            data.remove(data[1])
            
            self.assertEqual([5, 3, 7], [n.data for n in avl.preorder()])

    def test010(self):
        data = range(10, 100)
        random.shuffle(data)
        
        avl = AvlTree(data)
        self.assertEqual(len(avl), len(data))
        
        random.shuffle(data)
        
        for d in data:
            avl.remove(d)
            
        self.assertEqual(len(avl), 0)
        
    def test011(self):
        data = range(1, 300)
        random.shuffle(data)

        avl = AvlTree(data)
        self.assertEqual(len(avl), len(data))

        print data
        print avl
        random.shuffle(data)
        print data
        for d in data:
            avl.remove(d)

        self.assertEqual(len(avl), 0)
        
if __name__ == '__main__':
    unittest.main()