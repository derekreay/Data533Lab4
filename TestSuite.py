#!/usr/bin/env python
# coding: utf-8

# In[4]:


import unittest
from Lab3533Battest import TestBatters
from Lab3533caltest import TestCalculator
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestBatters))
    suite.addTest(unittest.makeSuite(TestCalculator))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()


# In[ ]:




