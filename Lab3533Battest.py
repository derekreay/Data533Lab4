#!/usr/bin/env python
# coding: utf-8

# In[1]:


import baseball.batters.batters as b
import unittest
#import numpy as np


# In[10]:


class TestBatters(unittest.TestCase):
    
    def setUp(self):
        self.b1 = b.batter("a", 25, "Yankees", "player", 85000, 400, 140, 25, 6, 29, 90)
        self.b2 = b.batter("J", 25, "Houston", "player", 85000, 400, 100, 20, 6, 10, 80)
        print("SetUp has run")
        
    def tearDown(self):
        self.b1 = None
        self.b2 = None
        print("tearDown has run")
        
    @classmethod    
    def setUpClass(cls):
        print("setupClass")
    
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        
        
    def test_batter(self):
        self.assertEqual(self.b1.name, 'a')
        self.assertEqual(self.b1.team, 'Yankees')
        self.assertEqual(self.b1.hits,140)
        self.b1.name = "Jay"
        self.assertEqual(self.b1.name, 'Jay')
        self.assertEqual(self.b1.totalbase(), 264)
        self.assertEqual(self.b1.getSalary(), None)
        self.assertEqual(self.b1.display(), None)
        
    def test_batter2(self):
        self.assertEqual(self.b2.name, 'J')
        self.assertEqual(self.b2.team, 'Houston')
        self.assertEqual(self.b2.hits,100)
        self.assertEqual(self.b2.batavg(), 0.25)
        self.assertEqual(self.b2.singles(), 64)
        #np.random.seed(35)
        self.assertEqual(self.b2.slugging(), 0.405)
        self.assertEqual(self.b2.onbase(), 0.375)
        self.assertEqual(self.b2.obps(), 0.78)
        #self.assertEqual(self.b2.simplateappearances(1), [0])
        self.assertEqual(self.b2.count([0,1,2,3,4]), [5,4,1,1,1])
        


unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




