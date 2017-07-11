# PythonForEverybody

Chapt 1: Why should you learn to write programs?
Chapt 2: Variables, expressions and statements
Chapt 3: Conditional Execution
Chapt 4: Functions 
Chapt 5: Iterations
Chapt 6: Strings
Chapt 7: Files
Chapt 8: Lists
Chapt 9: Dictionaries
Chapt 10: Tuples 
Chapt 11: Regular Expressions
Chapt 12: Networked Programs
Chapt 13: Using Web Seevices
Chapt 14: Object-Oriented Programming
Chapt 15: Using databases and SQL
Chapt 16: Visualizing data

Exercise Answers from "Python for Everybody: Exploring Data Using Python 3" by Charles Severance

9.2: Write a program that categorizes each mail message by which day of
the week the commit was done. To do this look for lines that start with “From”,
then look for the third word and keep a running count of each of the days of the
week. At the end of the program print out the contents of your dictionary (order
does not matter).

9.3: Write a program to read through a mail log, build a histogram using
a dictionary to count how many messages have come from each email address, and
print the dictionary.

9.4: Add code to the above program to figure out who has the most
messages in the file.
After all the data has been read and the dictionary has been created, look through
the dictionary using a maximum loop (see Section [maximumloop]) to find who
has the most messages and print how many messages the person has.

9.5: This program records the domain name (instead of the address) where
the message was sent from instead of who the mail came from (i.e., the whole email
address). At the end of the program, print out the contents of your dictionary.

10.1: Revise a previous program as follows: Read and parse the “From”
lines and pull out the addresses from the line. Count the number of messages from
each person using a dictionary.
After all the data has been read, print the person with the most commits by
creating a list of (count, email) tuples from the dictionary. Then sort the list in
reverse order and print out the person who has the most commits.

10.2: This program counts the distribution of the hour of the day for each
of the messages. You can pull the hour from the “From” line by finding the time
string and then splitting that string into parts using the colon character. Once
you have accumulated the counts for each hour, print out the counts, one per line,
sorted by hour as shown below.

10.3: Write a program that reads a file and prints the letters in decreasing
order of frequency. Your program should convert all the input to lower case and
only count the letters a-z. Your program should not count spaces, digits, punctuation,
or anything other than the letters a-z. Find text samples from several different
languages and see how letter frequency varies between languages. Compare your
results with the tables at wikipedia.org/wiki/Letter_frequencies.

13.1: Change either the www.py4e.com/code3/geojson.py or www.py4e.com/code3/geoxml.py
to print out the two-character country code from the retrieved data. Add error
checking so your program does not traceback if the country code is not there.
Once you have it working, search for “Atlantic Ocean” and make sure it can
handle locations that are not in any country.
