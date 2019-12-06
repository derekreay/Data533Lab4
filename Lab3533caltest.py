#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest
import baseball.batters.Calculator as cl


# In[4]:


class TestCalculator(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpclass has run")
        
    @classmethod
    def tearDownClass(cls):
        print("Teardownclass has run")

    def setUp(self):
        print("Set up has run")
        
    def tearDown(self):
        print("tear down has run")

    def test_battingavg(self):
        self.assertEqual(cl.batavg(10,4),0.4)
        self.assertEqual(cl.batavg(10,3),0.3)
        self.assertEqual(cl.batavg(5,1), 0.2)
        self.assertEqual(cl.batavg(20,4),0.2)
        self.assertEqual(cl.batavg(30,3),0.1)
        
    def test_singles(self):
        self.assertEqual(cl.singles(10,2,1,1),6)
        self.assertEqual(cl.singles(6,1,1,1),3)
        self.assertEqual(cl.singles(5,2,0,3),0)
        self.assertEqual(cl.singles(10,5,0,0),5)
        self.assertEqual(cl.singles(10,0,0,0),10)
        
    
unittest.main(argv =[''], verbosity=2, exit=False)


# In[ ]:




