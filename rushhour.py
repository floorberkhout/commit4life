################################
#   rushhour.py
#   Prints boardgame rush hour
################################


n = 6
a = (1,2,3)

# Prints board

for i in range(n):
    for j in range(n):
        if i == a[0] and j == a[1]:
            for x in range (a[2]):
                print("a", end="")
            j =+ a[2]
            
        else:
            print(".", end="")
            j =+ 1
    print("")
    i =+ 1
