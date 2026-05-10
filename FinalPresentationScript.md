Target
- BackGround/Data Structure: 4 min  
- Code Demo: 4 min
- Conclusion:	1.5–2 min  

Detail  
- BackGround/Data Structure

Slide 1: Title  
Hello everyone.  
Today, I will present my final project, Weekend Library Closing Time Finder Version 2.0.  

Slide 2: Introduction  
This project helps students find libraries that match their weekend schedule.  
The system includes both public libraries and university libraries.  
In real life, library hours are different on Saturday and Sunday.  
Also, some university libraries have access restrictions, such as ID requirements.  
In version 2.0, I added estimated travel time, so users can choose a more practical library based on both schedule and location.  

Slide 3: Problem Statement
The main problem is that students may want to study at a library, but they also need to manage their next schedule.  
For example, if a student wants to leave before 7 PM, the system should find a library that closes closest to that time, but not later than that time.  
However, closing time alone is not enough.  
A library may close at a good time, but it may be too far away.  
So my system solves this by considering both closing time and travel time.  

Slide 4: Graph Structure
To estimate travel time, I created a graph structure.  
In this graph:  
nodes represent libraries or road intersections  
edges represent road connections  edge costs represent estimated driving time  
Then I use Dijkstra’s algorithm to find the shortest travel time and path from the current location to each library.  
  
I used Dijkstra instead of BFS because the graph has different edge weights.  
For example, some roads take 5 minutes, while others take 10 or 25 minutes.  

Slide 5: UML Class Diagram  
This is the class structure of my system.  
The base class is Library.  
PublicLibrary and UniversityLibrary inherit from the Library class.  
  
The LibraryFinderSystem manages the main search process.  
The new class in version 2.0 is TravelMapGraph, which stores the graph and calculates shortest paths using Dijkstra’s algorithm.  
I also use LibraryResultQueue to display recommended libraries in order.  

Slide 6: Activity Diagram  
This diagram shows the overall process.  
First, the system loads library data and initializes map data.  
Then it sorts library closing times using merge sort.  
After the user enters a preferred time, the system uses binary search to find the closest closing time.  
  
After that, the system calculates the shortest travel time and path using the graph.  
Finally, it displays recommended libraries to the user.  

2. Code Demo：約4分  
Start Demo  
Now I will show the code and run the program.  
Step 1: Main function  
First, the program starts here:  

```
if __name__ == "__main__":
    system = LibraryFinderSystem()
    system.run()
```

This creates the main system object and starts the interactive program.  

Step 2: Load libraries  
Next, the system loads library data in load_libraries().  
This includes public libraries and university libraries.  
Each library has opening time, closing time, address, and access information.  
For university libraries, the system can also show whether visitors are allowed and whether ID is required.  

Step 3: Sort and search
The system sorts libraries by closing time using merge sort.  
Then, when the user enters a preferred time, the system uses binary search to quickly find the library whose closing time is closest to the user’s preferred time, but not later than it.  
This makes the search more efficient than checking every library manually.  

Step 4: Graph and Dijkstra
The most important update in version 2.0 is the graph search.  
The TravelMapGraph class stores road connections.  
The dijkstra() function calculates the shortest travel time from the current location to each library.  
The system also reconstructs the shortest path, so the output can show not only the time, but also the route.  

Step 5: Run normal case  
Now I will run the program.  

```
Example input:  
sat
19:00
```

This means the user wants to find libraries on Saturday that close at or before 7 PM.  
The system displays recommended libraries, their closing times, addresses, access information, shortest travel time, and shortest path.  
This shows that the system considers both schedule and travel distance.  

Step 6: Run university library case
Another example is:  

```
sun
22:00
```

This can show a university library result, such as Santa Clara University Library.  
The system also displays access information, such as whether ID is required.  
This is useful because university libraries may have different access rules from public libraries.  

Step 7: Error handling  
Finally, I will show error handling.  
For example, if the user enters an invalid day or invalid time format, the system shows an error message.  
Also, if no library matches the requested time, the system tells the user that no libraries match.  
This makes the program more reliable and user-friendly.  

3. Conclusion：1.5〜2分  
Slide 8: Technical Challenge  
There were two main technical challenges.  
The first challenge was building accurate map data.  
I manually converted real-world locations into graph nodes and estimated driving times as edge costs.  
The second challenge was safely adding Dijkstra’s algorithm to the existing system.  
To reduce integration risk, I tested the graph algorithm separately before integrating it into the full system.  

Slide 9: Conclusion
In conclusion, I developed the Weekend Library Closing Time Finder System to help students find libraries that match their weekend schedule.  
The system uses several data structures and algorithms, including inheritance, merge sort, binary search, graph, Dijkstra’s algorithm, queue, and hash table.  
The main improvement in version 2.0 is that the system can estimate travel time and shortest paths, not only closing time.  
For future improvements, I would like to support real-time library updates, public transportation, walking routes, and accessibility features.  
These improvements would make the system more inclusive and practical for more users.  

Slide 10: Thank you
Thank you for listening.  
