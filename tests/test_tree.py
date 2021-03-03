from algorithms.tree.traversal import (
    preorder,
    preorder_rec,
    postorder,
    postorder_rec,
    inorder,
    inorder_rec
)
from algorithms.tree.b_tree import BTree

from algorithms.tree import construct_tree_postorder_preorder as ctpp

from algorithms.tree.fenwick_tree.fenwick_tree import Fenwick_Tree

from algorithms.tree.bst import (bst)

from algorithms.tree.bst.count_left_node import count_left_node
from algorithms.tree.bst.depth_sum import depth_sum
from algorithms.tree.bst.height import height
from algorithms.tree.bst.num_empty import num_empty
from algorithms.tree.bst.delete_node import delete_node
from algorithms.tree.bst.kth_smallest import kth_smallest
from algorithms.tree.bst.kth_smallest import Solution as sol_ks
from algorithms.tree.bst.is_bst import is_bst
from algorithms.tree.bst.unique_bst import num_trees
from algorithms.tree.bst.BSTIterator import BSTIterator 
from algorithms.tree.bst.array_to_bst import array_to_bst 
from algorithms.tree.bst.bst_closest_value import closest_value 
from algorithms.tree.bst.predecessor import predecessor 
from algorithms.tree.bst.lowest_common_ancestor import lowest_common_ancestor

import unittest


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestTraversal(unittest.TestCase):

    def test_preorder(self):
        tree = create_tree()
        self.assertEqual([100, 50, 25, 75, 150, 125, 175], preorder(tree))
        self.assertEqual([100, 50, 25, 75, 150, 125, 175], preorder_rec(tree))

    def test_postorder(self):
        tree = create_tree()
        self.assertEqual([25, 75, 50, 125, 175, 150, 100], postorder(tree))
        self.assertEqual([25, 75, 50, 125, 175, 150, 100], postorder_rec(tree))

    def test_inorder(self):
        tree = create_tree()
        self.assertEqual([25, 50, 75, 100, 125, 150, 175], inorder(tree))
        self.assertEqual([25, 50, 75, 100, 125, 150, 175], inorder_rec(tree))


def create_tree():
    n1 = Node(100)
    n2 = Node(50)
    n3 = Node(150)
    n4 = Node(25)
    n5 = Node(75)
    n6 = Node(125)
    n7 = Node(175)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    return n1


class TestBTree(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        import random
        random.seed(18719)
        cls.random = random
        cls.range = 10000

    def setUp(self):
        self.keys_to_insert = [self.random.randrange(-self.range, self.range) for i in range(self.range)]

    def test_insertion_and_find_even_degree(self):
        btree = BTree(4)
        for i in self.keys_to_insert:
            btree.insert_key(i)

        for i in range(100):
            key = self.random.choice(self.keys_to_insert)
            self.assertTrue(btree.find(key))

    def test_insertion_and_find_odd_degree(self):
        btree = BTree(3)
        for i in self.keys_to_insert:
            btree.insert_key(i)

        for i in range(100):
            key = self.random.choice(self.keys_to_insert)
            self.assertTrue(btree.find(key))

    def test_deletion_even_degree(self):
        btree = BTree(4)
        key_list = set(self.keys_to_insert)
        for i in key_list:
            btree.insert_key(i)

        for key in key_list:
            btree.remove_key(key)
            self.assertFalse(btree.find(key))

        self.assertEqual(btree.root.keys, [])
        self.assertEqual(btree.root.children, [])

    def test_deletion_odd_degree(self):
        btree = BTree(3)
        key_list = set(self.keys_to_insert)
        for i in key_list:
            btree.insert_key(i)

        for key in key_list:
            btree.remove_key(key)
            self.assertFalse(btree.find(key))

        self.assertEqual(btree.root.keys, [])
        self.assertEqual(btree.root.children, [])

class TestConstructTreePreorderPostorder(unittest.TestCase):
    def test_construct_tree(self):
        
        # Test 1
        ctpp.pre_index = 0
        pre1 = [1, 2, 4, 8, 9, 5, 3, 6, 7]
        post1 = [8, 9, 4, 5, 2, 6, 7, 3, 1]
        size1 = len(pre1)

        self.assertEqual(ctpp.construct_tree(pre1, post1, size1), [8,4,9,2,5,1,6,3,7])

        # Test 2
        ctpp.pre_index = 0
        pre2 = [1, 2, 4, 5, 3, 6, 7]
        post2 = [4, 5, 2, 6, 7, 3, 1]
        size2 = len(pre2)

        self.assertEqual(ctpp.construct_tree(pre2, post2, size2), [4,2,5,1,6,3,7])

        # Test 3
        ctpp.pre_index = 0
        pre3 = [12, 7, 16, 21, 5, 1, 9]
        post3 = [16, 21, 7, 1, 9, 5, 12]
        size3 = len(pre3)

        self.assertEqual(ctpp.construct_tree(pre3, post3, size3), [16,7,21,12,1,5,9])


class TestFenwickTree(unittest.TestCase):
    def test_construct_tree_with_update_1(self):
        freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
        ft = Fenwick_Tree(freq)
        bit_tree = ft.construct()
        self.assertEqual(12, ft.get_sum(bit_tree, 5))

        freq[3] += 6
        ft.update_bit(bit_tree, 3, 6)
        self.assertEqual(18, ft.get_sum(bit_tree, 5))

    def test_construct_tree_with_update_2(self):
        freq = [1, 2, 3, 4, 5]
        ft = Fenwick_Tree(freq)
        bit_tree = ft.construct()
        self.assertEqual(10, ft.get_sum(bit_tree, 3))

        freq[3] -= 5
        ft.update_bit(bit_tree, 3, -5)
        self.assertEqual(5, ft.get_sum(bit_tree, 3))

    def test_construct_tree_with_update_3(self):
        freq = [2, 1, 4, 6, -1, 5, -32, 0, 1]
        ft = Fenwick_Tree(freq)
        bit_tree = ft.construct()
        self.assertEqual(12, ft.get_sum(bit_tree, 4))

        freq[2] += 11
        ft.update_bit(bit_tree, 2, 11)
        self.assertEqual(23, ft.get_sum(bit_tree, 4))


class TestBST(unittest.TestCase):
    def setUp(self):
        self.tree = bst.BST()
        self.tree.insert(9)
        self.tree.insert(6)
        self.tree.insert(12)
        self.tree.insert(3)
        self.tree.insert(8)
        self.tree.insert(10)
        self.tree.insert(15)
        self.tree.insert(7)
        self.tree.insert(18)

    def test_search(self):
        self.assertTrue(self.tree.search(12))
        self.assertFalse(self.tree.search(20))

    def test_size(self):
        self.assertEqual(9, self.tree.size())

    def test_count_left_node(self):
        self.assertEqual(4, count_left_node(self.tree.root))

    def test_depth_sum(self):
        self.assertEqual(253, depth_sum(self.tree.root, 4))

    def test_height(self):
        self.assertEqual(4, height(self.tree.root))

    def test_num_empty(self):
        self.assertEqual(10, num_empty(self.tree.root))  

    def test_delete_node(self):
        self.assertEqual(True, self.tree.search(18))
        delete_node(self.tree.get_root(), 18)
        self.assertEqual(False, self.tree.search(18))
        self.setUp()

    def test_kth_smallest(self):
        self.assertEqual(6, kth_smallest(self.tree.get_root(), 2))
        sol = sol_ks()
        self.assertEqual(6, sol.kth_smallest(self.tree.get_root(), 2))

    def test_is_bst(self):
        good_bst = bst.Node(2)
        good_bst.left = bst.Node(1)
        good_bst.right = bst.Node(3)
        self.assertTrue(is_bst(good_bst))

        bad_bst = bst.Node(1)
        bad_bst.left = bst.Node(2)
        bad_bst.right = bst.Node(3)   
        self.assertFalse(is_bst(bad_bst))        

    def test_unique_bst(self):
        self.assertEqual(num_trees(3), 5)

    def test_bst_iterator(self):
        iterator = BSTIterator(self.tree.get_root())
        found_nodes = []
        while(iterator.has_next()):
            found_nodes.append(iterator.next())
        self.assertEqual([3, 6, 7, 8, 9, 10, 12, 15, 18], found_nodes)
    
    def test_array_to_bst(self):
        values = [3, 6, 7, 8, 9]
        root_node = array_to_bst(values)

        # Check that all nodes exist
        iterator = BSTIterator(root_node)
        found_nodes = []
        while(iterator.has_next()):
            found_nodes.append(iterator.next())
        self.assertEqual(values, found_nodes)

        # Check balanced height
        self.assertEqual(height(root_node), 3)

    def test_bst_closest_value(self):
        self.assertEqual(closest_value(self.tree.get_root(), 10.9), 10)
        self.assertEqual(closest_value(self.tree.get_root(), 4.4), 3)
        self.assertEqual(closest_value(self.tree.get_root(), 4.5), 6)
        self.assertEqual(closest_value(self.tree.get_root(), 4.6), 6)

    def test_predecessor(self):
        self.assertEqual(predecessor(self.tree.get_root(), bst.Node(9)).val, 8)
        self.assertEqual(predecessor(self.tree.get_root(), bst.Node(12)).val, 10)
        self.assertEqual(predecessor(self.tree.get_root(), bst.Node(8)).val, 7)
        self.assertEqual(predecessor(self.tree.get_root(), bst.Node(6)).val, 3)
    
    def test_lowest_common_ancestor(self):
        self.assertEqual(lowest_common_ancestor(self.tree.get_root(), bst.Node(7), bst.Node(18)).val, 9)
        self.assertEqual(lowest_common_ancestor(self.tree.get_root(), bst.Node(10), bst.Node(18)).val, 12)
        self.assertEqual(lowest_common_ancestor(self.tree.get_root(), bst.Node(3), bst.Node(7)).val, 6)
        

        

if __name__ == '__main__':
    unittest.main()
