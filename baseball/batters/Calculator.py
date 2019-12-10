#!/usr/bin/env python
# coding: utf-8

# In[38]:


def batavg(atbats, hits):
    if atbats == 0:
        print("Cannot calculate batting average with no atbats")
    elif atbats < hits:
        print("Incorrect input cannot have an average higher than 1 or more hits than atbats")
    else:
        return hits/atbats
    
def singles(hits, doubles, triples, HR):
    try:
        if doubles+triples+HR > hits:
            raise BaseBallError
        else:
            return (hits-doubles-triples-HR)
    except:
        pass
    
def onbase(atbats, hits, walks):
    if atbats+walks == 0:
        print("Cannot calculate onbase with no plate appearances or walks")
    elif hits > atbats:
        print("Incorrect input cannot have an average higher than 1 or more hits than atbats")
    else:
        return (hits+walks)/(atbats+walks)

def totalbase(hits, doubles, triples, HR):
    try:
        return (singles(hits, doubles, triples, HR)+ 2*doubles + 3*triples + 4*HR)
    except:
        pass
       
    
def krate(atbats, K):
    try:
        if atbats < 0 or K < 0:
            raise negativeNum
        else:
            return K/atbats
    except negativeNum:
        pass
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Must input number, cannot accepts letters")
    else:
        pass


def slugging(atbats, hits, doubles, triples, hr):
    try:
        return (totalbase(hits, doubles, triples, hr))/(atbats)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Must input number, cannot accepts letters")
    else:
        pass
    
 
def obps(atbats, hits, doubles, triples, hr, walks):
    try:
        return slugging(atbats, hits, doubles, triples, hr)+onbase(atbats, hits, walks)
    except:
        pass
    
def walkrate(atbats, walks):
    if atbats+walks == 0:
        print("Cannot calculate walkrate with no plate appearances or walks")
    else:
        return walks/(walks+atbats)

class BaseBallError(Exception):
    def __init__(self):
        print("Incorrect input cannot have more extra base hits than hits")
          
class negativeNum(Exception):
    def __init__(self):
        print("Incorrect input cannot have negative values")

