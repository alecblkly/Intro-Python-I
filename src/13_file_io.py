"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

with open('foo.txt', 'r') as f:
    print(f.read())

if f.closed == True:
    print("-----------------------")
    print("File 'foo.txt' has been closed.")
else:
    print("-----------------------")
    print("File 'foo.txt' remains open.")


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open("bar.txt", "w") as f1:
    f1.write("words, words, words\n")
    f1.write("-------------------\n")
    f1.write("Llamas are neat.\n")
    f1.write("Hello, world!")

if f1.closed == True:
    print("-----------------------")
    print("File 'bar.txt' has been successfully written and has been closed.")
else:
    print("-----------------------")
    print("File 'bar.txt' was not successfully written and remains open.")
