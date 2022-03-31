"""
CTEC 121
date: <ex: mm/dd/yyyy>
<your name>
"""

# The comment block below is the specification. If you don't understand
# something ask questions in Slack to get clarification.

'''
Write a function to generate a date string given numeric values for month, 
day, and year, and a language. The valid languages are "US English", 
"British English", "French", and "German".

If US English is specified the returned string should be in the format of
month day, year. For all other languages the returned string should use the
European standard of day month year.

In this problem we are going to rework the internal data representation.
Instead of using lists for the months, use a dictionary with the following
specification:
keys 1-12 return a tuple containing the month strings for each language.
An example tuple ("January", "Janvier", "Januar")
Use a key for each language. The value associate with the language key should
be the index to use with the month tuple. Given the example tuple above
the "German" key should return a value of 2.

You can assume that the numeric inputs to the function are valid. 

Example outputs:
January 25, 2022
25 Januar 2022

Write a test function to test your date function. Test January, December,
and some month in the middle. 
'''

