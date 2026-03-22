--- Midterm Project Code and Report (Advanced Python, March 2026) ---
This README explains how to (1)set up, (2)run, and (3)test my project.  

# 1. How to set up.
Open a terminal in your environment. If you are using VS Code, you can open the terminal from the menu bar.

```bash
# ex. Make sure Python 3 is installed and working properly.
$ python --version
Python 3.12.5
```

# 2. How to run.
Run the following command in your terminal:

```bash
$ python 202603_WeekendLibraryClosingTimeFinder.py 
```

# 3. How to test my project.
After running the program, input the day (Sat or Sun) and the desired time.

TestCase1. [Success] Search for libraries that close at or before 19:00 on Saturday.

```bash
$ python 202603_WeekendLibraryClosingTimeFinder.py 
====== Weekend Library Closing Time Finder ======
Day (Sat/Sun): sat
Time HH:MM: 19:00

--> ex. result
== Result:1. Milpitas Library ==
   - Opening: 10:00 - Closing: 19:00
   - Address: 160 N Main St, Milpitas, CA
...
```

TestCase2. [Success] Search for libraries that close at or after 22:00 on Sunday.

```
$ python 202603_WeekendLibraryClosingTimeFinder.py 
===== Weekend Library Closing Time Finder ======
Day (Sat/Sun): sun
Time HH:MM: 22:00

--> ex. result
== Result:1. Santa Clara University Library ==
   - Opening: 9:00 - Closing: 22:00
   - Address: 500 El Camino Real Santa Clara, CA
```

TestCase3. [ErrorCase] Invalid day input (e.g., "aaa" instead of Sat/Sun).

```
====== Weekend Library Closing Time Finder ======
Day (Sat/Sun): aaa
Time HH:MM: aaa
Error: Day must be Saturday or Sunday
```

TestCase4. [ErrorCase] Valid time input, but no libraries match the requested time.

```
====== Weekend Library Closing Time Finder ======
Day (Sat/Sun): sat
Time HH:MM: 03:00
Error: No libraries match the requested time.
```
