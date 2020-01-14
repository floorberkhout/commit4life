# Lectures



## Lecture 1: Soorten problemen

##### Probleemtypes
	1. Constraint satisfaction problem (CSP)
		Oplossing moet voldoen aan constraints
		Alle oplossingen zijn even goed
		Voorbeeld: sudoku
	
	2. Constrained optimization problem (COP)
		Oplossing: zo goed mogelijk
		Objective function (scorefunctie, fitnessfunctie)
		Óók constraints aan variabelen 
	
	3. Free optimization problem (FOP)
		Oplossing: zo goed mogelijk
		Objective function (scorefunctie, fitnessfunctie)
		Geen contstraints aan variabelen
	
	Toestandsruimte: het aantal mogelijkheden tot de oplossing 
					voorbeeld: aantal koninginnen en aantal bordposities
	
	skiena: can make short work of very hard work
		

## Lecture 2: Random oplossingen

wat doet from .class import ..
 

## Lecture 3: Constructieve Algortimen
constructief
	breadth first
	depth first
	iterative deepening
		- optimaal prunen
			Early constraint checking
			Archief
			Branch and Bound
			Dijkstra, A
			Domein specifiek prunen
		- niet-optimaal prunen
			Beam Search
			Greedy Lookahead
			Heuristieken

branching factor is niet constant (upperbound is bij ons onbepaald)


breadth first:
--------------------
	queue als datastructuur
	fifo karakter
	bovenste state zet je in een queue 
	<img src="doc/UNADJUSTEDNONRAW_thumb_1460.png" width="50%">
	<img src="doc/UNADJUSTEDNONRAW_thumb_1461.png" width="50%">
	<img src="doc/UNADJUSTEDNONRAW_thumb_1462.png" width="50%">
	<img src="doc/UNADJUSTEDNONRAW_thumb_1463.png" width="50%">
	<img src="doc/UNADJUSTEDNONRAW_thumb_1464.png" width="50%">
	probleem:
		geheugen
		iterative deepening. depth first
		dictionary als datastructuur
	pruning bij breadth:
	<img src="doc/UNADJUSTEDNONRAW_thumb_1467.png" width="50%">
	checken om elke keer je constraints te checken > is het dezelfde stap als de vorige stap maar dan omgekeerd?

	beam search:
	Alleen de N beste Nodes 
	niet voor ons


depth first:
--------------------
	een stack aka lijst als datastructuur
	<img src="doc/UNADJUSTEDNONRAW_thumb_1465.png" width="50%">
	pruning bij depth:
	<img src="doc/UNADJUSTEDNONRAW_thumb_1469.png" width="50%">


dijkstra kortste pad algoritme:
--------------------
	voor kortste pad in een graaf

A* pruning:
--------------------
	routeplanners en tomtoms gebruiken allemaal a*


domein specifiek prunen:
--------------------
	<img src="doc/UNADJUSTEDNONRAW_thumb_146d.png" width="50%">
