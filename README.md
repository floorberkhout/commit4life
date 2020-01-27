# Commit4life - Rush Hour
Programmeertheorie

Rush hour is a sliding block logic game. You have to battle the gridlock as you slide the blocking vehicles out of the way for the red car to exit. In this repository you'll find 4 algorithms that will generate a solution for this game. 
Our goal was to solve 7 boards using different sorts of algorithms to come as near as possible to an optimal solution in which we take the amount of moves, runtime of the algorithm and memory use in account. 
Waiting to be solved in this assignment are three 6x6 boards, three 9x9 boards and one 12x12 board.
The advanced assignment, which is optional, reads as follows: generate a random Rush Hour board and try to solve them with the algorithms. Find out the difference between a 'difficult' board and an equally large 'easy' board. 

Example board:
<img src="doc/Rushhour6x6_1.jpg" width="50%">

### Getting Started

##### Prerequisites
This code is completely written in Python3.6.3. In requirements.txt are all the required packages to run this code succesfully. You can install these easily via pip, by running the next command:

pip install -r requirements.txt

##### Structure
Files:
	main.py
		> 
Folders:
	code
		> In this folder all the python scripts are found <
		algoritmes
			> In this folder three python files are found which contain our algorithms <
			X_first.py
			random_algo.py
			improved_random.py
		classes
			> In this folder all of our classes to set up the game and run the algorithms are found <
			board.py
			car.py
			csvwriter.py
			node.py
		data_visualisation
			> In this folder all the code that tests the algorithms is found, it also contains the < matplotlib visualisation code
			- board_visualisation.py
			- comparison.py
			- test_random.py
			- tree.py
			- treetest.py
	data
		> This folder contains the boards and their information to set up each individual game <
		Rushhour6x6_1.csv
		Rushhour6x6_2.csv
		Rushhour6x6_3.csv
		Rushhour9x9_4.csv
		Rushhour9x9_5.csv
		Rushhour9x9_6.csv
		Rushhour12x12_7.csv
	doc
		> This folder contains all images needed for the README.md and PROCESS.md <
	ppt
		> This folder contains the powerpoint for our presentation about this case <
	resultaten
		> This folder contains the csv files in which the solution of the game stated in the name can be found <
	screenshots
		> This folder contains the screenshot of the game stated in the name, but visualized with matplotlib <

##### Algorithms
	1. main.py loads car objects 
	2. main.py loads board object
	
	- Randomize
			Image!?
		3. It chooses random car object
		4. It chooses random move [1, -1]
		5. It sees if making the move is possible 
			> It makes the move if it is possible
		6. It checks if the winning(red/ X) car is in front of the exit, this means it has won
		   If this is not the case
		7. repeat

	- Improved random
			 Image?!
		3. It chooses random car object from the moveable cars
		4. It chooses random move [1, -1]
		5. It sees if making the move is possible 
			> It makes the move if it is possible
		6. It checks if another car is preventing the winning(red/ X) car from getting out, this means it has won
		   If this is not the case
		7. repeat
		   If this is the case
		7. It iterates over the solution and prunes all the duplicated boards to find the fastest way to the winning board within this solution

	- x_first
		> Depth-first 
			3. It takes the node that was last put in the queue (Last In, First Out)
			
			4. It identifies a possible move
			5. It creates the corresponding node
			6. It compares the new node with nodes earlier up the tree
			7. It checks if another car is preventing the winning(red/ X) car from getting out, this means it has won
			   If this is not the case
			8. It shut of nodes that represent a board state that was achieved before
			9. repeat
			   
		> Breadth-first
			3. It takes the node that is in front of the queue (First In, First Out)
			
			4. It identifies all possible moves
			5. It creates the corresponding nodes
			6. It compares the new nodes with nodes earlier up the tree
			7. It checks if another car is preventing the winning(red/ X) car from getting out, this means it has won
			   If this is not the case
			8. It shut of nodes that represent a board state that was achieved before
			9. repeat


##### Testing
!!! main.py uitleggen, hoe reproduceer je resultaten (uitleggen wat er in de commandline moet staan) !!!
To run the code with the standard configuration use the command:

python main.py

##### Authors
Paloma van Moerkerken
Bart Zeeuw van der Laan
Floor Berkhout

##### Acknowledgments
StackOverflow
minor programmeren van de UvA
