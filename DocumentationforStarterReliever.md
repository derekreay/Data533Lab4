## Documentation for Starter and Reliever Modules

### Derek Reay

#### Starter Module

#### Class personnel
The starter module can create the class personnel which is a general class of baseball persons.  It accepts the parameters Name, Age, Team, role and salary.  Salary is hidden.  

##### Functions
none of the functions require passing in additional parameters.  All are calculations from the data provided during initialization of the starter class.

###### display
Displays all information excepts salary

###### getSalary
returns the salary of the personnel class

##### Class Starter
A second class in this module is the starter class.  This class inherits from the personnel class and requires input of the same information but several additional pieces of information.  The additional information in order are: Innings pitched, strikeouts, walks, earned runs, hits and games started.  

The starter class can call all the function of the personnel class and has an additional six functions.

##### Functions
none of the functions require passing in additional parameters.  All are calculations from the data provided during initialization of the starter class.

###### function IPpG
Calculates the average number of innings pitched per start based on the initial inputs when initializing the starter class.  Higher values are preferred for starting pitchers.  

###### function ERA
Calculates the earned run average of the pitcher which is the number of expected runs to be scored by the pitcher over 9 innings of pitching.  This is the most common stat for comparison of pitchers.  It is calculated by multiplying the number of runs scored by nine and dividing by innings pitched.  The lower the better.

###### WHIP
WHIP or walk plus hits per innings pitched is a metric for expected number of baserunners per inning pitched.  This is a common pitching statistic.  The lower the better.

###### Kp9
Strikeouts per nine innings.  This returns the pitchers expected number of strikeout in 9 innings pitched.  This transforms two counting statistics strikeouts and innings pitched into a rate estimation of the pitchers ability to strikeout batters.  Typically the higher the better.

###### BBp9
Walks per nine innings.  This returns the pitchers expected number of walks in 9 innings pitched.  This transforms two counting statistics walks and innings pitched into a rate estimation of the pitcher walks.  Typically the lower the better.

###### display
Prints out the pitchers statistics.  Inherits from the display function of the personnel class to display some information.  


#### Reliever Module

The reliever module has two classes.

#### Class personnel
The starter module can create the class personnel which is a general class of baseball persons.  It accepts the parameters Name, Age, Team, role and salary.  Salary is hidden.  

##### Functions
none of the functions require passing in additional parameters.  All are calculations from the data provided during initialization of the starter class.

###### display
Displays all information excepts salary

###### getSalary
returns the salary of the personnel class

##### Class Reliever
A second class in this module is the reliever class.  This class inherits from the personnel class and requires input of the same information but several additional pieces of information.  The additional information in order are: Innings pitched, strikeouts, walks, earned runs, hits, saves, holds and chances.  

The reliever class can call all the function of the personnel class and has an additional six functions.

##### Functions
none of the functions require passing in additional parameters.  All are calculations from the data provided during initialization of the starter class.

###### function SVper
Calculates the number of saves per appearance.  This creates a rate stat which can be analyzed to determine if the relief pitcher is being used in save situations or is failing to get the save in those situations.  The higher the rate indicates more success in save situations.

###### function HDper
Calculates the number of holds per appearance.  This creates a rate stat which can be analyzed to determine if the relief pitcher is being used in hold situations or is failing to get the hold in those situations. The higher the rate indicates success and use in hold situations.   

###### function ERA
Calculates the earned run average of the pitcher which is the number of expected runs to be scored by the pitcher over 9 innings of pitching.  This is the most common stat for comparison of pitchers.  It is calculated by multiplying the number of runs scored by nine and dividing by innings pitched.  The lower the better.

###### WHIP
WHIP or walk plus hits per innings pitched is a metric for expected number of baserunners per inning pitched.  This is a common pitching statistic.  The lower the better.

###### Kp9
Strikeouts per nine innings.  This returns the pitchers expected number of strikeout in 9 innings pitched.  This transforms two counting statistics strikeouts and innings pitched into a rate estimation of the pitchers ability to strikeout batters.  Typically the higher the better especially for relievers who enter high leverage situations.  

###### BBp9
Walks per nine innings.  This returns the pitchers expected number of walks in 9 innings pitched.  This transforms two counting statistics walks and innings pitched into a rate estimation of the pitcher walks.  Typically the lower the better.  Not the most useful statistic for relievers as they can be less efficient with their pitches due to their lower inning utilization.  

###### display
Prints out the pitchers statistics.  Inherits from the display function of the personnel class to display some information.  
