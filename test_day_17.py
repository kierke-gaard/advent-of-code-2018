import unittest
from day_17 import *

class TestFlow(unittest.TestCase):

    def test_column(self):
        self.assertEqual(column(P(0,0), 3),
                         tuple(P(0,y) for y in (0,1,2,3)))
        self.assertEqual(column(P(0,0), 0), (P(0,0),))

    def test_row(self):
        self.assertEqual(row(P(0,0), 2),
                         (P(0,0), P(1,0), P(2,0)))
        self.assertEqual(row(P(0,0), -1),
                         (P(-1,0), P(0,0)))
        self.assertEqual(row(P(0,0), 0),
                         (P(0,0),))

    def test_horizontal_endpoint(self):
        g = grid_1()
        self.assertEqual(
            horizontal_endpoint(P(1,3), 'right', g, tuple()),
            (P(3,3), False))
        self.assertEqual(
            horizontal_endpoint(P(1,3), 'left', g, tuple()),
            (P(1,3), False))
        self.assertEqual(
            horizontal_endpoint(P(1,2), 'right', g, (P(1,3),P(2,3),P(3,3))),
            (P(5,2), True))
        self.assertEqual(
            horizontal_endpoint(P(1,2), 'left', g, (P(1,3),)),
            (P(1,2), False))
        h = grid_1()
        h.clay.remove(P(4,3))
        self.assertEqual(
            horizontal_endpoint(P(1,3), 'right', h, tuple()),
            (P(5,3), True))
    
    def test_horizontal_flow(self):
        g = grid_1()
        water = set()
        horizontal_flow(P(1,3), g, water)
        self.assertEqual(
            water,
            {P(x=1, y=2), P(x=5, y=9), P(x=3, y=2), P(x=1, y=3), P(x=5, y=4), P(x=3, y=3), P(x=5, y=5), P(x=5, y=6), P(x=5, y=7), P(x=2, y=3), P(x=2, y=2), P(x=4, y=2), P(x=5, y=2), P(x=5, y=8), P(x=5, y=3)})

    def test_vertical_flow(self):
        g = grid_1()
        water = set()
        vertical_flow(P(1,0), g, water)
        self.assertEqual(
            water,
            {P(x=1, y=2), P(x=5, y=9), P(x=3, y=2), P(x=1, y=3), P(x=5, y=4), P(x=3, y=3), P(x=5, y=5), P(x=5, y=6), P(x=5, y=7), P(x=2, y=3), P(x=2, y=2), P(x=4, y=2), P(x=1, y=0), P(x=5, y=2), P(x=1, y=1), P(x=5, y=8), P(x=5, y=3)})