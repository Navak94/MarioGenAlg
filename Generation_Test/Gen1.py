import random

for x in range(0,10000):

    file = open("C:\\Users\\Nate Hindman\\Desktop\\Emulators\\NES\\MarioNN\\Generation_Test\\Gen0\\" + str(x) + ".txt", "w") 

    for y in range(0,6000): # 6000 key presses
        intGen = random.randint(0, 5)

        if intGen == 0:
            file.write("q")
        if intGen == 1:
            file.write("w")
        if intGen == 2:
            file.write("e")
        if intGen == 3:
            file.write("a")
        if intGen == 4:
            file.write("s")
        if intGen == 5:
            file.write("d")

        file.write("\n")
    file.close() 
