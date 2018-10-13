# 1. Import the operating system module
import os
import re

regex_break_in = re.compile(r"POSSIBLE\sBREAK\-IN\sATTEMPT")
break_in_count = 0

# 2. Set the output file path
output_path = os.path.normpath("parsed_output.log")
# 3. Clear the contents of the output file
with open(output_path, "w") as clear_file:
    clear_file.write("")


# 4. Open the output file for appending
with open(output_path, "a") as output_file:
    with open("sample-data/auth.log", "r") as input_file:
        for line in input_file:
            if regex_break_in.search(line):
                break_in_count+=1
                # 5. Append matched line to the output file
                output_file.write(line)     

print 'Detected {count} attempted break-ins!'.format(count=break_in_count)
print 'Results written to "{path}".'.format(path=output_path)
