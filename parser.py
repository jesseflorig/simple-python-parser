# 1. Import regex module
import re

# 2. Create regex pattern
regex_break_in = re.compile(r"POSSIBLE\sBREAK\-IN\sATTEMPT")

with open("sample-data/auth.log", "r") as input_file:
    for line in input_file:
        #3. Only print line if it matches regex pattern
        if regex_break_in.search(line):
            print line      
