#!/usr/bin/env python
# coding: utf-8

# In[41]:


import unittest
from baseball.pitcher.starter import personnel
from baseball.pitcher.starter import starter
    
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
    def test_everything_else(self):
        self.assertEqual(self.p1.age, 25)
        self.assertEqual(self.p1.team, "Yankees")
        self.assertEqual(self.p1.role, "Player")
        self.assertEqual(self.p1.inningspitched, 180)
        self.assertEqual(self.p1.strikeouts, 180)
        self.assertEqual(self.p1.walks, 90)
        self.assertEqual(self.p1.earnedruns, 45)
        self.assertEqual(self.p1.hits, 90)
        self.assertEqual(self.p1.gamesstarted, 10)
        self.assertEqual(self.p1.ERA(),2.25)
        self.assertEqual(self.p1.WHIP(),1)
        self.assertEqual(self.p1.Kp9(),9)
        self.assertEqual(self.p1.BBp9(),4.5)
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

