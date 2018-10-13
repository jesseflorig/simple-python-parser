# 1. Import the operating system module
import re

regex_break_in = re.compile(r"POSSIBLE\sBREAK\-IN\sATTEMPT")
break_in_count = 0

# 2. Set the output file path
# 3. Clear the contents of the output file
# 4. Open the output file for appending
with open("sample-data/auth.log", "r") as input_file:
    for line in input_file:
        if regex_break_in.search(line):
            break_in_count+=1
            # 5. Append matched line to the output file
            print line      

print 'Detected {count} attempted break-ins!'.format(count=break_in_count)
