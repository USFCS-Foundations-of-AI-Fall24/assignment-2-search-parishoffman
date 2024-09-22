from unittest import TestCase
from mars_planner import *


class TestRoverState(TestCase):
    pass


class Test(TestCase):
    def test_move_to_sample(self):
        s = RoverState(loc="battery")
        move_to_sample(s)
        self.assertEqual(s.loc, "sample")

    def test_eq(self):
        s = RoverState(loc="battery")
        s2 = RoverState(loc="battery")
        self.assertEqual(s,s2)
        s3 = RoverState(loc="station")
        self.assertNotEqual(s, s3)

    def test_move_to_station(self):
        s = RoverState(loc="battery")
        move_to_station(s)
        self.assertEqual(s.loc, "station")

    def test_move_to_battery(self):
        s = RoverState(loc="sample")
        move_to_station(s)
        self.assertEqual(s.loc, "battery")

    def test_pick_up_tool(self):
        s = RoverState(loc="sample")
        pick_up_sample(s)
        self.assertEqual(s.holding_tool, True)

    def test_extract_tool(self):
        s = RoverState(loc="sample", holding_tool=True)
        extract_sample(s)
        self.assertEqual(s.sample_extracted, True)

    def test_drop_sample(self):
        s = RoverState(loc="station", sample_holding=True, sample_extracted=True)
        drop_sample(s)
        self.assertEqual(s.holding_tool, False)


class TestRoverState(TestCase):
    def test_successors(self):
        s=RoverState()
        slist = s.successors(action_list)
        print(slist)
