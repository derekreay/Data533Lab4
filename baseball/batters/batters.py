#!/usr/bin/env python
# coding: utf-8

# In[12]:


class personnel:
    """ Allows instances of baseball persons to be created

    Args:
    Name: Name of person
    Age: Age of person
    Team: Team person belongs to
    Role: Role in organization
    Salary: Salary of person

    Returns:
    Instance of baseball person
    """
    def __init__(self, name, age, team, role, salary):
        self.name = name
        self.age = age
        self.team = team
        self.role = role
        self.__salary = salary
        
    def display(self):
        print("Name:", self.name, "Age:", self.age, "Team:", self.team, "Role:", self.role)
        
    def getSalary(self):
        print("Salary:", self.__salary)
        
class batter(personnel):
    """ Allows instances of batter type personnel to be created

    Args:
    Name: Name of person
    Age: Age of person
    Team: Team person belongs to
    Role: Role in organization
    Salary: Salary of person
    Atbats: number of at bats in a given period
    Hits: number of hits in a given period
    Doubles: number of doubles in a given period
    Triples: number of triples in a given period
    HR: number of home runs in a given period
    walks: number of walks in a given period

    Returns:
    Instance of batter type baseball person
    """
    def __init__(self, name, age, team, role, salary, atbats, hits, doubles, triples, HR, walks):
        personnel.__init__(self, name, age, team, role, salary)
        self.atbats = atbats
        self.hits = hits
        self.doubles = doubles
        self.triples = triples
        self.hr = HR
        self.walks = walks
        
    
    def batavg(self):
        if self.atbats == 0:
            print("Cannot calculate batting average with no atbats")
        elif self.atbats < self.hits:
            print("Incorrect input cannot have an average higher than 1 or more hits than atbats")
        else:
            return self.hits/self.atbats
    
    def slugging(self):
        try:
            if self.atbats == 0:
                print("Cannot calculated slugging percentage with no atbats")
            elif self.hits > self.atbats:
                print("Cannot have more hits than atbats")
            else:
                return (self.totalbase())/(self.atbats)
        except:
            pass
    
    def totalbase(self):
        return (self.singles() + 2*self.doubles+3*self.triples+4*self.hr)

    def onbase(self):
        if self.atbats+self.walks == 0:
            print("Cannot calculate onbase with no plate appearances or walks")
        elif self.hits > self.atbats:
            print("Incorrect input cannot have an average higher than 1 or more hits than atbats")
        else:
            return (self.hits+self.walks)/(self.atbats+self.walks)
    
    def obps(self):
        try:
            return self.slugging()+self.onbase()
        except:
            pass
    
    def walkrate(self):
        if self.atbats+self.walks == 0:
            print("Cannot calculate walkrate with no plate appearances or walks")
        else:
            return self.walks/(self.walks+self.atbats)
    
    def singles(self):
        if self.doubles+self.triples+self.hr > self.hits:
            print("Incorrect input cannot have more extra base hits than hits")
        else:
            return (self.hits-self.doubles-self.triples-self.hr)
    
    def display(self):
        personnel.display(self)
        print("At bats:", self.atbats, "Hits:", self.hits, "Doubles:", self.doubles, "Triples:", self.triples, "Home Runs:", self.hr, "Walks:", self.walks)
    
    def simplateappearances(self, plateappearances):
        """ Simulates n plate appearance outcomes given a player object

        Args:
        plateappearances: number of plate appearances to simulate

        Returns:
        Vector of batter plate appearance outcomes.

        """
        #simulates plate appearances based on RNG from numpy
        import numpy as np
        outcome = []
        j=np.random.rand(10)

        for i in range(0,len(j)):
            if j[i] < self.batavg():
                #if number generated between 0 and 1 less than batting average returns 1 for hit
                outcome.append(1)
            else:
                #if number greater than average returns 0 for out
                outcome.append(0)
        
        for i in range(0, len(outcome)):
            if outcome[i] == 1:
                #disributes hits as 1 single 2 double 3 triple or 4 homerun based on proportion of hits batter has
                test = np.random.rand(1)
                if test < self.singles()/self.hits:
                    outcome[i] = 1
                elif test < (self.singles()+self.doubles)/self.hits:
                    outcome[i] = 2
                elif test < (self.singles()+self.doubles+self.triples)/self.hits:
                    outcome[i] = 3
                else:
                    outcome[i] = 4
        
        return outcome
    
    def count(self, x):
        """ Helps user understand simulated plate appearance outcomes

        Args:
        A vector of outcomes

        Returns:
        Standard baseball nomenclature given a vector of outcomes

        """
        #counts outcome of simpulated at bats and returns it in standatd baseball format
        #of atbats, hits, doubles, triples, homeruns in a list
        singles = 0
        doubles = 0
        triples = 0
        homeruns = 0
        hits = 0
        for i in x:
            if i == 1:
                singles += 1
                hits += 1
            elif i == 2:
                doubles += 1
                hits += 1
            elif i == 3:
                triples += 1
                hits += 1
            elif i == 4:
                homeruns +=1
                hits += 1
        print("In", len(x), "at bats:", singles, "singles,", doubles, "doubles,", triples, "triples,", homeruns, "homeruns, for", hits, "total hits")
        y=[len(x), hits, doubles ,triples, homeruns]
        return y

