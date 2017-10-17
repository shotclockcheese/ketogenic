# ketogenic

The Python script takes as input your daily log of food intake (i.e. 1012.txt) and outputs stats for macros, calories and carb breakdown.

By default, it retrieves nutrition facts from a Google Spreadsheet I've compiled throughout the duration of my keto diet (now about a month), but you have the option of using your own. Either create your own Google Spreadsheet and paste the link in for SPREADSHEET_PATH, or read in an excel file using pandas. I recommend using Google Spreadsheet since it's easier to update without hassle.

The script takes as input a tab-delimited text file with the following format:

item  portion
food1 1
food2 100
food3 54

and so on. Notice the gap between the columns are tabs, not spaces.
See 1012.txt for example (that's my 10/12 diet log). It has to be in the same directory as ketogenic.py, unless you want to make changes to code.

To run:

Step 1
Open terminal (I use MacOS, but you can figure out how to run scripts easily on other OS)
Go to directory containing ketogenic.py and your daily log (date.txt)
Type in: python ketogenic.py
Then you'll be prompted to enter the file name of your log.

An example output looks like this:

user$ python ketogenic.py

input daily log text file
->1012.txt

######################################
MACROS BREAKDOWN
fat: 161.8
protein: 130.8
carb: 12.0
CALORIES: 2103.1

######################################
CARB BREAKDOWN: TOTAL = 11.9728571429
carrot :  4.08
avocado :  4.0
keto_chow :  2.2
spinach :  0.8
pumpkin_seeds :  0.535714285714
pecan :  0.357142857143
######################################

If you have questions, shoot me a message on reddit.
Feel free to modify code if you got the ideas and the skills!
