# Using 'with' to open a file
with open('sample_txt1.txt', 'r') as file:
    # Reading the file line by line
    for line in file:
        print(line.strip())  # Using strip() to remove trailing newline characters

# The file is automatically closed after the 'with' block
# strip() removes the whitespace both from the beginning and ending side.