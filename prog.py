# OPENING THE SOURCE FILE
integers_file = open("integers.txt", "r")
# CREATING AND OPENING THE NEW FILES
square = open("double.txt", "a")
cube = open("triple.txt", "a")

for line in integers_file: #READING THE SOURCE FILE LINE BY LINE
    if int(line)%2 == 0: #IF THE NUMBER IS EVEN, WRITE ITS SQUARE ON THE double.txt
        square.write(f"{int(line)**2}\n")
    elif int(line)%2 != 0: #IF THE NUMBER IS ODD, WRITE ITS CUBE ON THE triple.txt
        cube.write(f"{int(line)**3}\n")

# CLOSING THE FILE TO AVOID CORRUPTION
integers_file.close()
square.close()
cube.close()