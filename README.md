# Programmeertheorie - Rush Hour
###### Commit4life

Rush hour is a sliding block logic game. You have to battle the gridlock as you slide the blocking vehicles out of the way for the red car to exit. In this repository you'll find 4 algorithms that will generate a solution for this game.

Our goal was to solve 7 boards using different sorts of algorithms to come as near as possible to an optimal solution in which we take the amount of moves, runtime of the algorithm and memory use in account.

Waiting to be solved in this assignment are three 6x6 boards, three 9x9 boards and one 12x12 board.

The advanced assignment, which is optional, reads as follows: generate a random Rush Hour board and try to solve it with the algorithms. Find out the difference between a 'difficult' board and an equally large 'easy' board.

Example board:
<img src="doc/Rushhour6x6_1.jpg" width="30%">

### Getting Started


#### Prerequisites
This code is completely written in Python3.6.3. In requirements.txt are all the required packages to run this code succesfully. You can install these easily via pip, by running the next command:

pip install -r requirements.txt


#### Structure
##### Files:
- main.py
- creator.py
- PROCESS.md
- requierements.txt
- README.md

##### Folders:
- code
	> In this folder all the python scripts are found
	- algoritmes
		> In this folder three python files are found which contain our 	
		- algorithms
		- X_first.py
		- random_algo.py
		- improved_random.py
		- randomize_check_generated.py
	- classes
		> In this folder all of our classes to set up the game and run the 	algorithms are found
		- board.py
		- car.py
		- csvwriter.py
		- node.py
		- boardcreator.py
	- data_visualisation
		> In this folder all the code that tests the algorithms is found, it also contains the matplotlib visualisation code
		- board_visualisation.py
		- comparison.py
		- test_random.py
		- tree.py
		- treetest.py
- data
	> This folder contains the boards and their information to set up each individual game
	- Rushhour6x6_1.csv
	- Rushhour6x6_2.csv
	- Rushhour6x6_3.csv
	- Rushhour9x9_4.csv
	- Rushhour9x9_5.csv
	- Rushhour9x9_6.csv
	- Rushhour12x12_7.csv
	- [The newly generated boards]
- doc
	> This folder contains all information needed for the presentation, README.md and PROCESS.md
	- ppt
		> This folder contains the powerpoint for our presentation about this case
- results
	> This folder contains the csv files in which the solution of the game stated in the name can be found


#### Algorithms
##### Randomize
This algorithm makes use of car.py (car objects) and board.py (board object).
1. main.py loads car objects
2. main.py loads board object
3. It chooses random car object from all the car objects on the board
4. It chooses random move [1, -1]
5. It sees if making the move is possible
	 - It makes the move if it is possible
6. It checks if the winning(red/ X) car is in front of the exit, this means it has won.
7. It repeats this if it isn't won

##### Improved random
This algorithm makes use of car.py (car objects) and board.py (board object).
1. main.py loads car objects
2. main.py loads board object
3. It chooses random car object from the moveable cars
4. It chooses random move [1, -1]
5. It sees if making the move is possible
	 - It makes the move if it is possible
6. It checks if another car is preventing the winning(red/ X) car from getting out, this means it has won
7. It repeats this if it isn't won
/
7. It iterates over the solution and prunes all the duplicated boards to find the fastest way to the winning board within this solution if it is won

##### x_first
Depth and breadth first look in many ways like eachother. Therefore we created the file "x_first". The file sees whether the command line stated depth or breadth first and will use this
information to either pick a random node from the queue (Depth-first) or a node that is in the front of the queue (Breadth-first), this determines the path to the solution.

These algorithms make use of car.py (car objects), board.py (board object) and node.py (node object). In theory, the Node class can be merged into the Board class but because Node contains functions that are not needed for the random algorithms we seperated it into two classes.
- Depth-first
	1. main.py loads car objects
	2. main.py loads board object
	3. It takes a random node from the queue (Random pick of branch)
	4. It identifies a possible move
	5. It creates the corresponding node
	6. It compares the new node with nodes earlier up the tree
	7. It checks if another car is preventing the winning(red/ X) car from getting out, this means it has won
	8. It shut of nodes that represent a board state that was achieved before and repeats if it isn't won
- Breadth-first
	1. main.py loads car objects
	2. main.py loads board object
	3. It takes the node that is in the front of the queue (First In, First Out)		
	4. It identifies all possible moves
	5. It creates the corresponding nodes
	6. It compares the new nodes with nodes earlier up the tree
	7. It checks if another car is preventing the winning(red/ X) car from getting out, this means it has won
	8. It shut of nodes that represent a board state that was achieved before and repeats if it isn't won


#### Testing
To run the code with the standard configuration use the command: python main.py [algorithm] [board].

Algorithm = "randomize" or "improved_random" or "breadth_first" or "depth_first".

Board = "6x6_1" or "6x6_2" or "6x6_3" or "9x9_4" or "9x9_5" or "9x9_6" or "12x12_7"

When user chooses depth_first or breadth_first, user gets the question whether they want memory_clearer on or off.
Type: "on" or "off". Put the memory clearer on to save objects as strings in order to save memory.  

The output of running each algorithm has the following format:
>> {begin board}
>> {end board}
>> Congratulations you've won the game!
>> Move count
>> Time elapsed


#### ADVCANCED - creator
This program creates new with the help of the class BoardCreator. The user has the option to determine the size of the board, the amount of cars and a treshold for the number of moves the board should as least take to be solved.
The program works as follows:
	1. Create a board with the help of the class BoardCreator
		a. Place the X car
		b. Keep on placing the other cars randomly until all cars are placed
		c. If a new car can't be placed anymore restart the procedure
	2. Load in the newly created board
	3. Check if the new board can be solved by a random algorithm in less than 100.000 steps, else create a new board and start over
	4. If the new board can be solved randomly it's a valid board. Now let's see how many steps the optimal solution is by using the breadth_first algorithm
	5. If the optimal solution takes more steps than the treshold the board is a proper board

The ability to create new boards has given us further insights. The difficulty of solving a board optimally is a function of the amount of nodes in the breadth_first graph. Less cars with more space on the board doesn't neccesarily make the board easier to solve for a pc. Since it gives a lot of children for every node. Which can even make the board more difficult to solve. We've seen examples that take a human only 5 sec to solve that take way more computing time than it needs for solving a board that can keep a human occupied for minutes

#### Authors
Paloma van Moerkerken
Bart Zeeuw van der Laan
Floor Berkhout


#### Acknowledgments
StackOverflow
minor programmeren van de UvA
