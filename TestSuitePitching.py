#!/usr/bin/env python
# coding: utf-8

# In[5]:


import unittest

from TestReliever import TestPersonnel
from TestReliever import TestReliever
from TestStarter import TestStarter

# if statements in the code result in <100% coverage

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestPersonnel))
    suite.addTest(unittest.makeSuite(TestReliever))
    suite.addTest(unittest.makeSuite(TestStarter))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()

