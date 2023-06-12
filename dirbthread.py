import subprocess
from concurrent.futures import ThreadPoolExecutor
import sys

# Function to run command dirb
def run_dirb(subdomain):
    subprocess.run(["dirb", subdomain])

# write filename as argument 
filename = sys.argv[1]

# Read the file with subdomains
with open(filename) as f:
    subdomains = [line.strip() for line in f]

# Create a thread pool with  max_workers=   threads
with ThreadPoolExecutor(max_workers=5) as executor:
    # Submit tasks to the thread pool for execution
    executor.map(run_dirb, subdomains)

