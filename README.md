Copyright (c) 2013 Moisés Guimarães

Implementation of AVL trees (http://en.wikipedia.org/wiki/AVL_tree) in Python.
Class AvlTree supports the following functionalities:
 - insertion of a new entry in the tree
 - removal of any entry in the tree
 - tree traversals:
    - preorder
    - inorder
    - postorder
    
To use run.sh type:
  ./run.sh python tree.py
  
You can use the output to compare to another binary tree implementation like:
  ./run.sh python tree.py    > py.log
  ./run.sh java   Tree.class > java.log
  diff py.log java.log

!!! This code is used only for educational purpose. !!!

This code is available under MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
