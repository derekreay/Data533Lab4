#!/usr/bin/env python
# coding: utf-8

# In[70]:


import unittest
from baseball.pitcher.reliever import personnel
from baseball.pitcher.reliever import reliever

class TestPersonnel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #something
        print("setUpClass")
    def setUp(self):
        self.p1 = personnel("Mike Trout", 25, "Yankees", "Player", 500000)
        self.p2 = personnel("Mike Schmidt", 59, "Phillies", "Player", 20000)
        print("setUp")
    def test_name(self):   
        self.assertEqual(self.p1.name, "Mike Trout")
        self.assertEqual(self.p2.name, "Mike Schmidt")
        print("name")
    def test_set_age(self):
        self.assertEqual(self.p1.age,25)
        self.assertEqual(self.p2.age,59)
        print("age")
    def tearDown(self):
        self.p1 = None
        self.p2 = None
        print("tearDown")
    @classmethod
    def tearDownClass(cls):
        #something
        print("tearDownClass")
    unittest.main(argv=[''], verbosity=2, exit=False)

class TestReliever(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #something
        print("setUpClass")
    def setUp(self):
        self.p1 = reliever("Gerrit Cole", 25, "Yankees", "Player", 500000,180,180,90,45,90,10,10,20)
        self.p2 = reliever("Madison Bumgarner", 30, "Braves", "Player", 500000,180,180,90,45,90,10,0,10)
        print("setUp")
    def test_name(self):   
        self.assertEqual(self.p1.name, "Gerrit Cole")
        self.assertEqual(self.p2.name, "Madison Bumgarner")
        print("name")
    def test_SVper(self):
        self.assertEqual(self.p1.SVper(),0.5)
        self.assertEqual(self.p2.SVper(),1)
    def test_team(self):
        self.assertEqual(self.p1.team,"Yankees")
        self.assertEqual(self.p2.team,"Braves")
    def test_everything_else(self):
        self.assertEqual(self.p1.role, "Player")
        self.assertEqual(self.p1.inningspitched, 180)
        self.assertEqual(self.p1.strikeouts, 180)
        self.assertEqual(self.p1.walks, 90)
        self.assertEqual(self.p1.earnedruns, 45)
        self.assertEqual(self.p1.hits, 90)
        self.assertEqual(self.p1.saves, 10)
        self.assertEqual(self.p1.holds, 10)
        self.assertEqual(self.p1.chances, 20)
        self.assertEqual(self.p1.SVper(), 0.5)
        self.assertEqual(self.p1.ERA(),2.25)
        self.assertEqual(self.p1.WHIP(),1)
        self.assertEqual(self.p1.Kp9(),9)
        self.assertEqual(self.p1.BBp9(),4.5)
        self.assertEqual(self.p1.HDper(), 0.5)
        self.assertIsNone(self.p1.getSalary())
        self.assertIsNone(self.p1.display())
    def tearDown(self):
        self.p1 = None
        self.p2 = None
        print("tearDown")
    @classmethod
    def tearDownClass(cls):
        #something
        print("tearDownClass")
    unittest.main(argv=[''], verbosity=2, exit=False)

