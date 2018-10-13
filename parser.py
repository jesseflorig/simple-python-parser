# 1. Import regex module

# 2. Create regex pattern
with open("sample-data/auth.log", "r") as input_file:
    for line in input_file:
        #3. Only print line if it matches regex pattern
        print line      
