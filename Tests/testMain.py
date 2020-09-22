import unittest

from main import Board


class testMain(unittest.TestCase):

    def test_get_live_neighbours(self):
        b = Board([[1]*4]*4)
        self.assertEqual(b.get_live_neighbours(0, 0), 3)
        self.assertEqual(b.get_live_neighbours(0, 1), 4)
        self.assertEqual(b.get_live_neighbours(1, 1), 8)
        self.assertEqual(b.get_live_neighbours(3, 3), 3)
        self.assertEqual(b.get_live_neighbours(3, 2), 4)

    def test_upadate(self):
        b = Board([[1] * 4] * 4)
        b.update()
        print(b.render())
        print()
        b.update()
        print(b.render())
        return