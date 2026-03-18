--- Midterm Project Code and Report, Advanced Python Mar,2026 ---  
This README explains (1.)how to set up, (2.)run, and (3.)test my project.  

# 1. How to set up
1.1 Open the terminal on your environment. If you use VScode, you can open the terminal from the menu var.
1.2 Check if python is installed properly and works with python version 3.

```
# ex. Check if python is installed properly.
$ python --version
Python 3.12.5
```

# 2. How to run
Run code as below on the terminal on your environment.

```
$ python 202603_WeekendLibraryClosingTimeFinder.py 
```

# 3. How to test
Input Sat or Sun, and expected closing time after running the code.  

TestCase1. [SuccessCase] Search the library closing until 19:00 on Saturday.

```
$ python 202603_WeekendLibraryClosingTimeFinder.py 
====== Weekend Library Closing Time Finder ======
Day (Sat/Sun): sat
Time HH:MM: 19:00
--> Check the result
```

TestCase2. [SuccessCase] Search the library closing until 22:00 on Sunday.

```
$ python 202603_WeekendLibraryClosingTimeFinder.py 
===== Weekend Library Closing Time Finder ======
Day (Sat/Sun): sun
Time HH:MM: 22:00
--> Check the result
```

TestCase3. [ErrorCase] Date Error (input "aaa" instead of Sat/Sun).

```
====== Weekend Library Closing Time Finder ======
Day (Sat/Sun): aaa
Time HH:MM: aaa
Error: Day must be Saturday or Sunday
```

TestCase4. [ErrorCase] Time Error (Too early than opening hour).

```
====== Weekend Library Closing Time Finder ======
Day (Sat/Sun): sat
Time HH:MM: 03:00
Error: No libraries match the requested time.
```
