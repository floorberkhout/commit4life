# Proces Commit4life
#### Programmeertheorie Paloma, Bart en Floor


##### Planning

week 1 - interpratie van de case
	wat is mijn case?
	welk (sub)probleem moet ik oplossen? Wat is de oplossing en hoe ziet tie eruit?
	hoe kan ik die (digitaal) presenteren? -> datastructuur
	hoe genereeer ik random een oplossing

week 2 - eerste resultaten
	random is af. resultaten laten zien
	hoe generee ik betere oplossingen dan random?
	waarom zou dit beter zijn

week 3 - exploratie resultaten en verfijning
	vergelijk je nieuwe manier(en) van oplossingen maken met random

week 4 - slotstuk

##### Process
###### maandag 06-01-20
	Github opstarten:
		3 branches
		floor is master
		2 forks van bart en paloma
		> gebruiken alleen de masterbranch op aanraden van Quinten

	Start programmeren
		- Simpele versie voor uitlezen autos van CSV
		- simpele grid versie op autos te laten zien
		- Randen rond spelbord aangebracht

	Probleem omschrijving
		rush hour
		creëer grid met blokjes (auto's) die kunnen schuiven in de juiste richting
		bedenk een algoritme wat een rush hour bord kan oplossen (de rode auto naar de uitgang leiden zonder te botsen)

		oplossing: start bij de auto wat de uitgang blokkeert, check elke auto die vanaf dan de mogelijkheid tot het verschuiven blokkeert
					zoveel mogelijk blokjes verschuiven tot het rode autootje stappen naar rechts kan zetten om uiteindelijk de uitgang te vinden
		repo weergeven op de manier van classes zoals bij adventure

<img src="doc/umlrushhour.png" width="50%">

	Complicaties:
		het rode blokje moet soms terug

###### dinsdag 07-01-20
	- Bart werkt aan load grid
	- Paloma werkt aan load cars
	- Floor werkt aan objects voor load cars car.py	
		
	- Vragen voor presentatiesessie:
		voortgangsgesprek tijdens college
		waar is het college?


	- Eerste borden opgelost met de hand ter vergelijking 
<img src="doc/bord6x61" width="50%">
<img src="doc/bord6x62" width="50%">



###### woensdag 08-01-20
	Bart is bezig met de resultaten omzetten in een csv bestand
	Floor en Paloma hebben barts screenprint omgezet in de goede structuur	

	Verbeterpunten:
		Onnodig power verbruiken tijdens het itereren
		+2 / +12 stappen 

###### vrijdag 10-01-20
	> apart de functies voor algoritmes >> verwerken in board.py


###### maandag 13-01-20

	state space:
		36 faculteit =  3.7199333e+41

		36 × 34 × 32 × 30 × 28 × 26 × 24 × 22 × 20 × 18 × 16 × 14 × 12 × 10 × 8 × 6 × 4 × 2 =  1.6783439e+21
	
		36 × 33 × 30 × 27 × 24 × 21 × 18 × 15 × 12 × 9 × 6 × 3 = 2.5456109e+14

		per bord state space berekenen want die zit per bord ergens hier tussen in > lege plekken zijn niet elkaar gebonden lengte van de auto's wel.
		
		6x6_1
			2 x 2 x 3 x 3 x 5 x 3 x 3 x 5 x 5 x 4 x 3 x 3 x 5 =  7290000

		
	voortgangsgesprek:
		win move (naar buiten rijden) telt als 1 stap
		een move van meerdere stappen telt als maar 1 move (checken of er meerdere moves achter elkaar zijn en dan dat van het totaal moves aftrekken)
		optimalisatie zit hem in het geheugenprobleem (het archief optimaliseren) (pruning)
		verschillende manier vergelijken (waarom gebeurt wat er gebeurt, beargumenteren, waarom is het ene beter dan het ander)
		write_move, check_for_win, move functions in board.py

###### dinsdag 14-01-20
				Write_move_csv, check_for_win, move functions in board.py
				Verder met advanced algoritme door Bart
		CHECK	win functie verbeteren 
		CHECK 	zorgen dat de vorige stap niet wordt teruggedraait in een nieuwe move (pruning)
		CHECK	zorgen dat moves in dezelfde richting met de dezelfde auto die achterelkaar worden uitgevoerd niet een 'nieuwe' move is
		CHECK	visualisation

###### woensdag 15-01-20
	random algo > testen 1000 keer geeft een maximum en minimum in aantal zetten en duur
					verbeteren:
								Geen mogelijkheid om aantal unieke states te checken (in een verder algoritme zorg je dat de vorige stap niet terug gedraait kan worden)
						CHECK	Hij zou invalid stappen niet als stap moeten zien
								Random alleen maar loslaten op lijst movable_cars						


	Presentatie:
		staafdiagrammen om de gemiddelde te vergelijken van verschillende algoritmes
		uitleggen waarom greedy en hillclimber niet geschikt zijn
		random, advanced random, breadth first en deep first vergelijken
		betere uml
		beaming past neit bij rush hour omdat nodes geen score kunnen dragen

###### donderdag 16-01-20
	random
	improved random
		+ reversed geen stappen
		+ kiest random uit movable_cars
	breadth first
		> hij write de csv nog niet kan nog niet
		> netter
		> afmaken wat betreft printen enzo
		> 12x12 super veel geheugen nodig > optimaliseren 
	breadth first met iterative pruning
		+ Minder goede uitslag maar wel sneller en minde geheugen opnemend
	depth first
		+ 185 moves
		> print nog niet het laatste bord in de end_game functie

	iteratief algoritme > random oplossing optimalisere (eerst alle tussenstukken) (iteratief kijken of je tussen alle notes sneller kan zijn)

	doen:
		depth first
		grafiek van breadth first
		12 proberen
		1000 iteraties van random 


###### maandag 20-01-20	
	Voortgangsgesprek:
		optimalisatie breadth first
			beam search > langere oplossing zonder dat dat misschien nodig zou zijn
			nodes met de meeste zetten

		imshow() visualisatie van het bord
		
		Zo min mogelijk code presenteren	
		Size() check size of object
			
		random 
			doet alles
		
		improved random
			doet alles
		
		breadth first 
			alles 6x6's
			zo efficient mogelijkheid opslaan 
		
		depth first
			testen
			pruned op oplossingen 
			
		bord visualisatie & grafiekjes

###### dinsdag 21-01-20	
		breadth first optimalisatie
		depth first nog prunen op oplossingen als bart de nette versie klaar heeft
		bord visualisatie afmaken met lijst vanuit breadth first
		improved random af		

		Hoe presenteren we alle verschillende data
			alle algoritmes loslaten op 6x6_1
			alle algoritmes loslaten op 12x12
			move_count, time_elapsed en geheugen vergelijken
			
###### vrijdag 24-01-20	
		depth first is nu random
		dubbele borden van improved random worden er tussen uit gefilterd
		main.py is compatible met alle algortimes

###### maandag 27-01-20	
	code:
		- Bart verder met random bord genereren 
		- repo cleanen
		- code cleanen en commenten
		- moveable cars naar board.py halen
		
		

		Benodigdheden:
		> Uitermate goed gestructureerde code en repository, met uitgebreide uitleg over implementatiedetails en de structuur van de code
		> Duidelijke README
		    - De case waar de studenten mee bezig geweest zijn is duidelijk geïntroduceerd in de README.
		    - De aanpak van de verschillende algoritmen is duidelijk beschreven in de README.
		    !! - Het is na lezen van de README duidelijk hoe de resultaten te reproduceren zijn, via een interface (command line), argumenten die meegegeven kunnen worden voor de verschillende functionaliteiten/algoritmen, of bijvoorbeeld een duidelijke uitleg welke file te runnen om welk resultaat te krijgen.
		> Duidelijke repo
		    - Zit geen rommel in de repository (pycache, .DS_Store, algoritmeA, algoritmeA2, algoritmeA2Final, etc.)
		    - De repository heeft een duidelijke en overzichtelijke indeling die ervoor zorgt dat files makkelijk te vinden zijn.
		    - Er is een nette hoeveelheid commits.
		> Duidelijke code
		    - Stijl van de code is consistent.
		    - De code is modulair geschreven, met korte functies, duidelijk ordening van files, en geen duplicate code.
		    - Abstractie is aangebracht waar nodig; alleen relevante data over een object is beschikbaar om complexiteit laag te houden en onderhoud aan code simpel te maken.
		    - Code bevat alleen magic numbers, * imports, while True, of try-excepts waar uiterst noodzakelijk
		    - Code heeft duidelijke control flow; e.g. geen ellenlange if-statements midden in al grote functies.
		    - De code is duidelijk in functionaliteit; docstrings, comments en variabelenamen zijn nuttig/beschrijven wat functies doen.
		    - De code is intuitief en direct te gebruiken voor soortgelijke projecten.
			
	presentatie:
		> Depth first random uitleggen
		> minder tekst in ppt
		
	vragen voor voortgangsgesprek:
	- wat is een nette hoeveelheid commits?
	- data visualisatie code nodig in repo?

	Doen in het voortgangsgesprek:
    	- Een motivatie schrijven voor het cijferdeel “Exploratie van de case” adhv de studiewijzer.
    	- Een laatste blik werpen op jullie Git repository en code.
    	- Laatste vragen die jullie hebben beantwoorden.
		
	Exploratie:
	- We denken 4, omdat we de algoritmes van college hebben gebruikt en een beetje geoptimaleseerd. 
	- Breadth first, geheugenoptimalisatie
	- Depth first kiest een random beginnode, ipv altijd de eerste node. 
	- Randomalgoritme
	- Improved random, waarbij je random kiest voor de mogelijke auto's. En hij knipt de moves van het bord die overbodig waren.
	- Heuristiek: als er geen auto's meer tussen de rode auto en de uitgang staan, ziet hij dat hij gewonnen heeft. 
		
		
		
