## SDSS Computing Studies Python Assignment
### Assignment #8b Input/Output from Files (Total Marks 10)

Objectives:
* Read data from a file
* Store data to a file
* Use string.split() to separate the contents of a file into a list
* Develop an understanding of javascript object notation (json)
* Use the json library to retrieve or store complex data structures

We sometimes refer to volatile memory as memory stores where information is impermanent - when you turn off your computer, or when you close the program, the data stored in memory is gone.  There are several ways to deal with volatile memory that you want to keep:
1. We can save it to a file
2. We can store it in a database (which is really saving it to a file in a database)

Old methods would store the value of one variable per line in a text file, but these are very limited in their use.  It also doesn't really work well for more complex data structures like lists or tuples.  

##### Javascript Object Notation (JSON) #####
https://en.wikipedia.org/wiki/JSON
JSON is a way of storing complex data into text.  It is so useful that it has become quite standard to pass complex data between different applications using JSON.  A web page which uses Javascript to run its applications might send a request to a server that runs on Python or PHP.  That site will send data as JSON to the web page, where it is decoded and utilized in the Javascript environment.  JSON is very useful as a cross platform way of communicating! 

Today we will be reading and writing data from files.  There are many ways to read data from a file:
* You can read a whole file into a single variable
* You can read a file one line at a time, and store each line as an element of a list

### 2 Tasks

##### Task 1
Read the data from the file task01.txt
Create a function called find().
Find will require 1 input parameter that is a string literal.
The return value is the line number (starting at 0) that the parameter to be found is on.

Example:
assert find('apple') == 0
assert find('fish') == 5

(2 points) 

##### Task 2
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches

(2 points)
