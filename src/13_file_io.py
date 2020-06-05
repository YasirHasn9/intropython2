"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
try:
    with open("foo.txt") as files:
        lines = files.read()
        print(lines)

finally:
    files.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
with open("bar.txt", "w") as newFile:
    newFile.write("first line \n")
    newFile.write("second line \n")
    newFile.write("third line")

# YOUR CODE HERE
