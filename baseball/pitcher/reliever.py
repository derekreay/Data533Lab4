#!/usr/bin/env python
# coding: utf-8

# In[6]:


class SavesError(Exception): 
    def __init__(self):
        print("saves can't be greater than chances you numpty")
        
class HoldsError(Exception): 
    def __init__(self):
        print("holds can't be greater than chances bruh")
        


# In[5]:


class personnel:
    """creates baseball personnel object
    
    
    Args
    Name: string name of person
    Age: int age of person
    Team: string name of team affiliation
    Role: string role of person with the organization
    salary: number salary of person
    
    Returns
    object of class personnel with all agruments saved within as an instance variable
    """
    def __init__(self, name, age, team, role, salary):
        self.name = name
        self.age = age
        self.team = team
        self.role = role
        self.__salary = salary
        
    def display(self):
        print("Name:", self.name, "Age:", self.age, "Team:", self.team, "Position:", self.role)
        
    def getSalary(self):
        print("Salary:", self.__salary)


# In[22]:


class reliever(personnel):
    """creates baseball reliever class object
    
    
    Args
    Name: string name of person
    Age: int age of person
    Team: string name of team affiliation
    Role: string role of person with the organization
    salary: number salary of person
    innings pitched: number of innings pitched
    strikeouts: int number of strikeouts
    walks: int number of walks
    earnedruns: int number of earned runs
    hits: int number of hits
    saves: int number of saves
    holds: int number of holds
    chances: int number of times used in game
    
    Returns
    object of reliever class with all agruments saved within as an instance variable
    """
    def __init__(self, name, age, team, role, salary,inningspitched, strikeouts, walks, earnedruns, hits,saves, holds, chances):
        personnel.__init__(self, name, age, team, role, salary)
        self.saves = saves
        self.holds = holds
        self.chances = chances
        self.inningspitched = inningspitched
        self.strikeouts = strikeouts
        self.hits = hits
        self.walks = walks
        self.earnedruns = earnedruns
    
    def display(self):
        personnel.display(self)
        print("IP:", self.inningspitched, "K:", self.strikeouts,
        "BB:", self.walks, "ER:", self.earnedruns, "Hits:", self.hits,
               "SV:", self.saves, "HD:", self.holds, "CH:", self.chances)
        
    def SVper(self):
        try: 
            if self.saves - self.chances >0:
                raise SavesError
            else:
                return self.saves/self.chances
        except:
            pass
    
    def HDper(self):
        try: 
            if self.holds - self.chances >0:
                raise HoldsError
            else:
                return self.saves/self.chances
        except:
            pass
        
    def ERA(self):
        """creates baseball personnel object
        
        Args
        None all calculations use previously defined instance variables
    
        Returns
        float value which represents the calculated ERA for this starter.  
        """
        if self.inningspitched <= 0:
            print("Needs inningspitched > 0 to calculate")
        else:
            return self.earnedruns*9/self.inningspitched            
    
    def WHIP(self):
        if self.inningspitched <= 0:
            print("Needs inningspitched > 0 to calculate")
        else:
            return (self.walks+self.hits)/self.inningspitched
    
    def Kp9(self):
        if self.inningspitched <= 0:
            print("Needs inningspitched > 0 to calculate")
        else:
            return self.strikeouts/self.inningspitched*9
    
    def BBp9(self):
        if self.inningspitched <= 0:
            print("Needs inningspitched > 0 to calculate")
        else:
            return self.walks/self.inningspitched*9

