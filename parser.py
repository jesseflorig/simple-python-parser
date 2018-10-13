# 1. Open a file for reading
with open("sample-data/auth.log", "r") as input_file:
    # 2. Loop through the lines in the file
    for line in input_file:
        # 3. Print the lines to the command line
        print line      
