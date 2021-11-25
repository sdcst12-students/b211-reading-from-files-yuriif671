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
* 
### XX Tasks

##### Task 1
(x points) 

