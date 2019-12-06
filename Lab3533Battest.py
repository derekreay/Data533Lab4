#!/usr/bin/env python
# coding: utf-8

# In[1]:


import baseball.batters.batters as b
import unittest


# In[9]:


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
        
        
    def testbatter(self):
        self.assertEqual(self.b1.name, 'a')
        self.assertEqual(self.b1.team, 'Yankees')
        self.assertEqual(self.b1.hits,140)
        self.b1.name = "Jay"
        self.assertEqual(self.b1.name, 'Jay')
        self.assertEqual(self.b1.totalbase(), 264)
        
    def testbatter2(self):
        self.assertEqual(self.b2.name, 'J')
        self.assertEqual(self.b2.team, 'Houston')
        self.assertEqual(self.b2.hits,100)
        self.assertEqual(self.b2.batavg(), 0.25)
        self.assertEqual(self.b2.singles(), 64)
        
        
unittest.main(argv =[''], verbosity=2, exit=False)


# In[ ]:




