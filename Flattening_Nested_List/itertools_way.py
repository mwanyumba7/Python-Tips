# We can also use itertools module to flatten lists

# First we import the itertools module
import itertools

kenyanBands = [["Sarabi", "Le Band", "Wanavokali", "Heart the Band", "Sauti Sol"],["Maroon Commandos", "Wakadinali", "Aluta"]]

# We then use the module to flatten the list

flat_kenyanBands= (list(itertools.chain.from_iterable(kenyanBands)))

# We then print the list and see the changes
print(flat_kenyanBands)

# Output

['Sarabi', 'Le Band', 'Wanavokali', 'Heart the Band', 'Sauti Sol', 'Maroon Commandos', 'Wakadinali', 'Aluta']