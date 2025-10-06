import sys
import time

# Ensure there are two command line arguments
if len(sys.argv) != 3:
    raise ValueError('Please provide two file names.')

firstFile = sys.argv[1]
secondFile = sys.argv[2]

print("\nThe hash table will be built from:", firstFile)
print("\nThe hash table will be compared to:", secondFile)

# Starts the timer for the program runtime
start = time.time()

# Constants declared
a = 31
tableSize = 29

# Makes an empty list of size 29 to store the data
hashTable = [""] * tableSize

# Opens the first file to build the hash table
infile = open(firstFile, "r")
for line in infile:
    for word in line.split():
        word = word.strip().lower()
        # Holds the calculation before it is entered
        hashCode = 0
        # Holds the number of characters in the word
        wordLen = len(word)
        # Hash calculation
        for i in range(wordLen):
            element = word[i]
            hashCode += ord(element) * (a ** (wordLen - 1 - i))
        # Finds the index in the table that the word should be
        indexInTable = hashCode % tableSize
        # Linear probing for collisions
        while hashTable[indexInTable] != "" and hashTable[indexInTable] != word:
            indexInTable = (indexInTable + 1) % tableSize
        hashTable[indexInTable] = word
infile.close()

# Holders for the total
numLines = 0
numWords = 0
keywords = {}

# Opens the first file again to get the keywords
infile = open(firstFile, "r")
for line in infile:
    for word in line.split():
        word = word.strip().lower()
        # Add word to the keywords dictionary if it's not already there
        if word not in keywords:
            keywords[word] = 0
infile.close()

# Opens the second file to process the contents and count keywords
infile = open(secondFile, "r")
for line in infile:
    # Skips empty lines
    if len(line.strip()) > 0:
        numLines += 1
        lineOfWords = line.split()
        numWords += len(lineOfWords)
        for word in lineOfWords:
            word = word.strip().lower()
            # Holds the calculation before it is entered
            hashCode = 0
            wordLen = len(word)
            # Hash calculation
            for i in range(wordLen):
                element = word[i]
                hashCode += ord(element) * (a ** (wordLen - 1 - i))
            # Finds the index in the table that the word should be
            indexInTable = hashCode % tableSize
            # Linear probing to find the word in the hash table
            index = indexInTable
            found = False
            while hashTable[indexInTable] != "":
                if hashTable[indexInTable] == word:
                    found = True
                    break
                indexInTable = (indexInTable + 1) % tableSize
                # Prevent infinite loop in case of a full loop
                if indexInTable == index:
                    break
            # Only count the word if it was found and is a keyword
            if found and word in keywords:
                keywords[word] += 1
infile.close()

# Print out the statistics
print("**********************")
print("***** Statistics *****")
print("**********************")
print(f"Total lines read: {numLines}")
print(f"Total words read: {numWords}")
print("")
print("Break down by keyword:")
for word in keywords:
    print(f"{keywords[word]} : {word}")

# Stops the timer
end = time.time()

print("\n**********************")

# Calculates the runtime
totalTime = (end - start) * 1000

print("")
# Prints runtime
print(f"Total Time: {totalTime:.10f} milliseconds.")
