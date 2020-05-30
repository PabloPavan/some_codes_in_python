"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        check = self.lookup(string)
        if check != -1:
            self.table[check].append(string)
        else:
            self.table[self.calculate_hash_value(string)] = [string]

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value] is None:
            return -1
        else:
            return hash_value

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        #ord() para obter o valor ASCII de uma letra, e chr()
        return ord(string[0]) *100 + ord(string[1])
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')