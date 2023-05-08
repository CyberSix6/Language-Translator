# Description: Remove all whitespace from a file
import re

filename = ''

# Read the file contents
with open(filename, 'r') as f:
    contents = f.read()

# Remove whitespace
contents = re.sub(r'\s+', '', contents)

# Write the modified contents back to the file
with open(filename, 'w') as f:
    f.write(contents)
