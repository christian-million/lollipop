import unittest
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):

    def demo_linked_list(self):
        return LinkedList([1, 2, 3, 4, 5])

    def test_create_empty(self):
        """LinkedList without arguments should return instance of LinkedList with None"""
        tst_list = LinkedList()
        self.assertEqual(tst_list.head, None)

    def test_equals(self):
        """Test the equality comparison between two LinkedLists"""
        tst_list1 = self.demo_linked_list()
        tst_list2 = self.demo_linked_list()
        self.assertEqual(tst_list1, tst_list2)
        self.assertEqual(LinkedList(), LinkedList())

        tst_list2.append(5)
        self.assertNotEqual(tst_list1, tst_list2)
        self.assertNotEqual(tst_list1, LinkedList([1, 2, 3, 4]))
        self.assertNotEqual(tst_list1, LinkedList([1, 2, 3, 4, 5, 6]))
        self.assertNotEqual(tst_list1, LinkedList(["1", "2", "3", "4", "5", "6"]))
        self.assertNotEqual(tst_list1, ["1", "2", "3", "4", "5"])
        self.assertNotEqual(["1", "2", "3", "4", "5"], tst_list1)

    def test_append_left(self):
        """Appends to the head of the list"""
        tst_list = LinkedList()
        tst_list.append(5, False)
        tst_list.append(4, False)
        tst_list.append(3, False)
        tst_list.append(2, False)
        tst_list.append(1, False)
        self.assertEqual(tst_list, self.demo_linked_list())

    def test_append_right(self):
        """Appends to the 'tail' of the list"""
        tst_list = LinkedList()
        tst_list.append(1)
        tst_list.append(2)
        tst_list.append(3)
        tst_list.append(4)
        tst_list.append(5)
        self.assertEqual(tst_list, self.demo_linked_list())

    def test_pop_left(self):
        """Removes and returns the head of the list"""
        tst_list = self.demo_linked_list()
        out = tst_list.pop(False)
        self.assertEqual(out, 1)
        self.assertEqual(tst_list, LinkedList([2, 3, 4, 5]))

    def test_pop_right(self):
        """Removes and returns the tail of the list"""
        tst_list = self.demo_linked_list()
        out = tst_list.pop()
        self.assertEqual(out, 5)
        self.assertEqual(tst_list, LinkedList([1, 2, 3, 4]))

    def test_contains(self):
        """"""
        tst_list = self.demo_linked_list()
        self.assertFalse(tst_list.contains(6))
        self.assertTrue(tst_list.contains(5))

    def test_in_operator(self):
        """"""
        tst_list = self.demo_linked_list()
        self.assertFalse(6 in tst_list)
        self.assertTrue(5 in tst_list)

    def test_reverse(self):
        """"""
        tst_list = self.demo_linked_list()
        tst_list.reverse()
        self.assertEqual(tst_list, LinkedList([5, 4, 3, 2, 1]))

    def test_add_operator(self):
        """"""
        tst_list = self.demo_linked_list()
        tst_list + self.demo_linked_list()
        self.assertEqual(tst_list, self.demo_linked_list())

        tst_list = tst_list + self.demo_linked_list()
        self.assertIsInstance(tst_list, LinkedList)
        self.assertEqual(tst_list, LinkedList([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))

    def test_iteration(self):
        """"""
        tst_list = self.demo_linked_list()

        for i, item in enumerate(tst_list):
            self.assertEqual(i+1, item)

    def test_length(self):
        """"""
        tst_list = self.demo_linked_list()
        self.assertEqual(len(tst_list), 5)
        self.assertEqual(len(LinkedList()), 0)
        self.assertTrue(False if LinkedList() else True)


if __name__ == '__main__':

    unittest.main()
