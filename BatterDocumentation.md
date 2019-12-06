

# Package information

This package was built in order to enable users to easily calculate baseball rate stats by entering count data into each function.

# General folder structure

The Baseball package contains two subpackages: pitcher and batters.

### Documentation for Derek Reay's modules

### Modules

The batters subpackage contains two modules: batters.py and Calculator.py.

The purpose of the batters module is to store a batter's stats as an object in order to operate on them. This module also contains a batting simulator, simulating outcomes for a given number of plate appearances.

The purpose of the Calculator module is to avoid having to store the entire breadth of a batter's count stats in order to calculate rate stats. Instead, this allows the user to enter the only specific relevant parameters to calculate a rate metric.

### Functions and Classes

###### Batters module:

The first class is: personnel, which is a general category of baseball person with general attributes.

This class has a display function and a getSalary function in order to view the hidden attribute Salary.

The next class is: batter, which inherits personnel's attributes and adds batter-specific attributes

This class contains the basic functions to help evaluate batter talent: batavg (hits per at bat), slugging (bases per at bat), totalbase (bases over a period of time), onbase (ratio of outs made vs total chances), obps (sum of slugging and onbase), singles (number of singles hit) and display.

This module also includes a method to simulate plate appearances (simplateappearances). This allows the user to simulate the outcome of a given number of plate appearances based on an RNG. The RNG returns an n length vector of values in {0,1}. For value in the vector, the function determines whether the batter is out or not based on his batting average vs the vector value. If the batter is not out, the function determines what type of hit the plate appearance results in, again based on the RNG vector value. This result vector is then returned. The count function translates this outcome vector into an easy to read summary of the outcome vector.

###### Calculator module:

This module has many of the same functions as the Batters module, but with more refined input capability for the user to calculate statistics on the fly. A personnel object does not need to be created in this case, rather each function is called with only its relevant parameters entered by the user. Also included in this module are Krate (strikeouts per atbats) and walkrate (walks per plate appearance).

If you would like to read any more about the metrics used in this package, please visit http://m.mlb.com/glossary/standard-stats for more information.
