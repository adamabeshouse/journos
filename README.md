journos - A pro-active journal to help you measure your life
=======

### Installation:

After cloning, navigate to the directory and run 'python setup.py'. 

You will also need PyCrypto and Appdirs, two Python modules. If you don't, setup.py will notify you of that. If that happens, you can install these with PyPI with the following terminal commands:

`sudo pip install pycrypto`

`sudo pip install appdirs`

### Valid commands:

`journos` : starts up and asks you to fill out recent unfilled entries, and to fill out todays entry

`journos <date>` : starts up only for the purpose of filling out an entry for the given date

`journos r` : read todays entry

`journos r <date>` : read that days entry

where <date> is a string of one of the following forms:

• MM/DD/YYYY

• MM/DD (year is taken to be the current year)

• MM/DD/YY (year is taken to be 20YY)


`journos changepw` : change your password

`journos dump` : dump your whole journal into a text file (journos\_dump\_MM\_DD\_YYYY) in the current directory

`journos search <flags> <searchterm>`: search for the given string throughout the journal, where the possible flags are:

• -questions: only search through question text

• -answers: only search through answer text

• -case: have your search be case-sensitive

By default, a case-insensitive search is done throughout all text (questions and answers) in the journal

`journos questions`: modify the questions that are asked in the journal in addition to "What did you do today?"


### To-do:

• ~~Be able to run it from any directory~~

• In 'setup.py', bind the command `journos`

• ~~Easy way to add special questions~~

• Easier install, e.g. perhaps `pip install journos` ?

• Handle bad input from command line
