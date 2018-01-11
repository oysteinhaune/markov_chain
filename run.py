"""
Run.py includes the code that ties the flow of the application together.
It will be started from the command line.
"""

# Importing the modules needed.
from markov_python.cc_markov import MarkovChain

# Makes a new object.
mc = MarkovChain()

# Adds the text file.
mc.add_file('quotes.json')

# Generates some word in a list.
generatedWords = mc.generate_text(10)

# Prints out the word with the first letter uppercase,
# in a numbered list.
i = 0
for word in generatedWords:
    i += 1
    print ("%s. %s." % (i, word.title()))
