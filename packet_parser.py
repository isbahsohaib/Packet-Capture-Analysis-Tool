
# Define a function 'parse' that takes a file path ('afile') and a list ('data') as arguments
def parse(afile, data):
    # Open the file in read ('r') mode
    infile = open(afile, 'r')

    # Read the first line from the file and remove leading/trailing whitespace
    line = infile.readline().strip()

    # Continue reading lines until there are no more lines in the file
    while line:
        # Remove extra spaces and join the words in the line with single spaces
        test = ' '.join(line.split())
        
        # Split the cleaned line into words and append them to the 'data' list
        data.append(test.split(' '))    

        # Read the next line and remove leading/trailing whitespace
        line = infile.readline().strip()

    # Close the file
    infile.close()

# Example usage
data = []  # Create an empty list to store the parsed data
parse('Node1_filtered.txt', data)  # Call the 'parse' function with the file path and data list

# Iterate through the 'data' list and print each line
for line in data:
    print(line)
