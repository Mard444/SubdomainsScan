import sys
import subprocess


filename = sys.argv[1]

# Read file an do for ,for every line  in the file
with open(filename) as f:
    for line in f:
        string = line.strip() 
        subprocess.run(["dirb",string])

    
    
    
