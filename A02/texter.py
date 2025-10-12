import sys

# check command line argument count
if len(sys.argv) > 1:
    # assign file_name
    file_name = sys.argv[1]
# the parameter (file name) is not specified, print help on how to use the script
else:
    print("usage: python3 texter.py <file_name>")
    exit(1)

# definition of a Texter class
class Texter:
    # definition of a run method
    def run(file_name):
        # opening a text file 'test.txt' for reading
        # ensuring the automatic closing of the file (with)
        with open(file_name, "r") as f: 
            # reading the entire content into the variable text
            text = f.read() 
                
        # a) Count paragraphs
        # spliting text into paragraphs and storing in a list
        paragraphs = text.split('\n\n')
        # counting the number of paragraphs
        num_paragraphs = len(paragraphs) 
        # printing the number of paragraphs
        print("Number of paragraphs:", num_paragraphs) 
                
        # b) Count spaces after dot
        # assigning the number of ". " to the variable num_spaces_after_dot
        num_spaces_after_dot = text.count('. ')
        # printing the number of spaces after dot
        print("Number of spaces after dot:", num_spaces_after_dot)

# call the run method
Texter.run(file_name)