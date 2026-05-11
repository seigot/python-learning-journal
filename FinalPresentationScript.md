### Introduction
Hi everyone.
Today, I'm going to talk about my project, the Weekend Library Closing Time Finder Version 2.0.  

First of all, I will briefly talk about my project background.  
This project aims to helps students find libraries that match their weekend schedule efficiently.  
In real life, library hours are different on Saturday and Sunday and also, some university libraries have access restrictions, such as ID requirements.  
Additionally, Showing estimated travel time helps users choose the most practical library.  

### Problem Statement
About the Problem Statement.  
Some libraries remain open as late as 7:00 PM, allowing students to plan their study sessions flexibly.  
However, studying with too much concentration can cause students to lose track of time and miss their next scheduled activities.  
In addition, The system version 1.0 didn't show the distance or travel time to each library.  
The key solution of this system is to find libraries whose closing time is closest to but not later than the user’s preferred time, and also displaying the estimated travel time to each library.  
I believe This solution allows students to stay focused on studying while still managing their schedule effectively.  

### Graph Structure
About the Graph Structure.  
Modeling real-world transportation networks as a graph Accurately is essential for calculating travel time.  
For this project, I manually created a graph of roads and libraries in the San Jose area.  
Each nodes represent libraries or major road intersections.  
Each edges represent road connections.  
Edge costs represent estimated driving time.  
To find the shortest travel time and route, I used Dijkstra’s algorithm, which is one of the most efficient algorithms for solving shortest path problems.  

### Solution(Class)  
Now, I will explain how the system architecture for this system.  
The system consists of four main components.  
The base Library class manages base library data PublicLibrary and UniversityLibrary classes.  
The Library finder system classes is used to search for the optimal closing time based on user input.  
The Library Result Queue Class display three recommended libraries, estimated time, and shortest path to the user.  
In this project, TravelMapGraph has the graph and search algorithm function to get the estimated time, and shortest path.  

### Solution(Process)  
Let me explain about diagram which shows the overall process of the system.  
There are three main steps in the overall process.  
First, all library data is loaded into memory before user input, and graph is initialized.  
Second, the system waits for the user to enter a preferred day and closing time.  
Third, based on the user's input, the system search preferred libraries and displays up to three preferred libraries, estimated time and shortest path.   
From a graph algorithm perspective, Dijkstra’s algorithm is used to get the estimated time and shortest path to each library.  

### Code Demo
Next, I will briefly explain how the code works.  

The first class is the Library class.  
The Library class has get_opening_time and get_closing_time methods to get the library's opening and closing hours.  
The Library class is a base class for the PublicLibrary and UniversityLibrary.  

The LibraryFinderSystem class finds the best matching libraries by sorting and searching the data.  
The load_libraries method loads and prepares the data.  
The binary_search_closest method finds the best match library from user request efficiently with time complexity O(log n).  
The run method controls the main flow of the program, including user input, validation, searching, and displaying results.  

The LibraryResultQueue class manages and displays the search results using a queue and display results in order.  
The utility functions support the system by converting time strings into minutes and validating day and time inputs.  

And The most important update is the TravelMapGraph.  
The TravelMapGraph class manages the graph and algorithms and calculates estimated time and shortest path to the library.  
Basic Workflow is 3steps.  
First, Build the graph by connecting roads, intersections, and libraries.  
Second, alculate the shortest travel time from the current location to each library.  
Third, Return the estimated travel time and shortest path for the selected library.   

The add_node method adds a new location node, such as a road intersection or library.  
The add_edge connects two locations and stores the travel cost between them.  
The add_edge_with_list adds multiple road connections efficiently using predefined edge data.  
The InitializeMapdata builds the San Jose road network and connects all libraries to the graph.  
The SetCurrentLocationtoMapdata sets the user’s current location and starts route calculation.  
The dijkstra method finds the shortest travel time from the current location to all libraries.  
The get_distance method returns the estimated travel time to a selected library.  
The get_path method returns the estimated travel time to a selected library.  

### Demo(2)

Now, let me run the program.  

First, I enter "sat" for Saturday and "19:00" as the desired time.  
The system searches for libraries using binary search.  
Here is the result.  
You can see that Milpitas Library is recommended, with a closing time of 19:00 and Estimated Time is 28 minutes.  
  
Next, I will try another example.  
I enter "sun" and "22:00".  
Again, the system finds the closest valid closing time, Estimated Time, shortest path.  
The result shows Santa Clara University Library and Estimated Time is 25 minutes.  

### Challenge
About the challenges. there were two challenges in this project.  
The first challenge was building accurate map data.  
I converted real-world map into graph nodes manually, however mathmatical convertion is more accurate and efficient.  
The second challenge was smoothly adding Dijkstra’s algorithm to the existing system.  
In the system version 1.0, The code size was already large. So to minimize the error of system integration,  
I tested the graph algorithm separately before integrating it into the entire system.  

### Conclusion
In conclusion, I designed and developed the Weekend Library Closing Time Finder system.  
This system not only recommends suitable library options but also provides the estimated travel time and the shortest path to each library.  
To improve system performance, I applied appropriate data structures and algorithms such as graph structures and Dijkstra’s algorithm.  
These well-designed data structures also enabled smoother feature expansion during development.  
For future improvements, the system could incorporate real-time traffic updates, multiple transportation options such as public transit or walking, and ethical considerations such as accessibility support and multilingual features.  
  
Thank you for listening.  
