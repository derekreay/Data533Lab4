#!/usr/bin/env python
# coding: utf-8

# In[9]:


import unittest
from baseball.pitcher.starter import personnel
from baseball.pitcher.starter import starter

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
    
class TestStarter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #something
        print("setUpClass")
    def setUp(self):
        self.p1 = starter("Gerrit Cole", 25, "Yankees", "Player", 500000,180,180,90,45,90,10)
        self.p2 = starter("Madison Bumgarner", 30, "Braves", "Player", 500000,180,180,90,45,90,20)
        print("setUp")
    def test_name(self):   
        self.assertEqual(self.p1.name, "Gerrit Cole")
        self.assertEqual(self.p2.name, "Madison Bumgarner")
        print("name")
    def test_Kp9(self):
        self.assertEqual(self.p1.Kp9(),180/180*9)
        self.assertEqual(self.p2.Kp9(),180/180*9)
    def test_IPpG(self):
        self.assertEqual(self.p1.IPpG(),18)
        self.assertEqual(self.p2.IPpG(),9)
    def tearDown(self):
        self.p1 = None
        self.p2 = None
        print("tearDown")
    @classmethod
    def tearDownClass(cls):
        #something
        print("tearDownClass")
    unittest.main(argv=[''], verbosity=2, exit=False)

