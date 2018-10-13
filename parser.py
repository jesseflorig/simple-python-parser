import re

regex_break_in = re.compile(r"POSSIBLE\sBREAK\-IN\sATTEMPT")
break_in_count = 0

with open("sample-data/auth.log", "r") as input_file:
    for line in input_file:
        if regex_break_in.search(line):
            break_in_count+=1
            print line      

print 'Detected {count} attempted break-ins!'.format(count=break_in_count)
