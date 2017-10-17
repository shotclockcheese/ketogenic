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

After you've run the script (python ketogenic.py), an example output looks like this:

![alt text](https://github.com/shotclockcheese/ketogenic/blob/master/example%20output.png)

If you have questions, shoot me a message on reddit.
Feel free to modify code if you got the ideas and the skills!
