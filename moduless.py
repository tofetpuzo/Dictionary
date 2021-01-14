import time
import os
import pandas as pd

while True:
    if os.path.exists("/Users/femitemiola/Desktop/programs/temps_today.csv"):
        data = pd.read_csv("temps_today.csv")
        print(data.mean())#["st1"])
        # with open('/Users/femitemiola/Desktop/programs/vegetables.txt') as myfile:
            
        # print(myfile.read())
    else:
        print("File does not exist")
    time.sleep(10)

# import modules
# dir(time) or help(time.sleep)
# if for example, you wrote a script and it gets deleted , you will still want your code to still be running 
# you have to use a module called os 


# This code tells if the path exists
# os.path.exists("/Users/femitemiola/Desktop/programs/vegetables.txt")
# True
