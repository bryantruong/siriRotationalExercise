"""
Bryan Truong
2/23/2020
Completed for Siri Rotational Engineer Program Interview(s)
"""
from nltk.corpus import words

dictionary = words.words()
# All possible words that are 3 characters or greater
dictionary = [w for w in dictionary if len(w) >= 3]
board = [
    ["r", "a", "e", "l"],
    ["m", "o", "f", "s"],
    ["t", "e", "o", "k"],
    ["n", "a", "t", "i"],
]
deltas = [(-1, -1),  # Top left neighbor
          (-1, 0),  # Move up
          (-1, 1),  # Top right neighbor
          (0, 1),  # Move right
          (1, 1),  # Bottom right neighbor
          (1, 0),  # Move down
          (1, -1),  # Bottom left neighbor
          (0, -1)  # Move left
          ]


class Trie:  # Use nested dictionaries to implement a trie
    root = {}  # The dict will store the neighbors

    def add(self, wordToAdd):
        current = self.root
        for character in wordToAdd:
            if character not in current:  # search the keys of the dict
                current[character] = {}  # initialize that new node's dictionary
            current = current[character]  # Move the pointer to the prefix
        current['*'] = True  # Use '*' to represent the end of a word

    def search(self, queryWord):
        current = self.root
        for character in queryWord:
            if character not in current:
                return False
            current = current[character]
        # After moving to the last character node, check if it terminates with the '*'
        if '*' in current:
            return True
        else:
            return False


def dfs(startingCell, currentWord, visited, trieNode):
    if startingCell in visited:
        return
    letter = board[startingCell[0]][startingCell[1]]
    visited.append(startingCell)

    if letter in trieNode:
        currentWord += letter
        if '*' in trieNode[letter]:  # Signifies that this was the end of a word
            print(currentWord)
        neighbors = getNeighbors(startingCell)
        for neighbor in neighbors:
            # Recurse with the neighboring coordinates and the corresponding trie node
            dfs(neighbor, currentWord, visited, trieNode[letter])


def getNeighbors(startingCoordinates):
    neighboringCoordinates = []
    for delta in deltas:
        newRowCoord = startingCoordinates[0] + delta[0]
        newColCoord = startingCoordinates[1] + delta[1]
        if newRowCoord < 0 or newRowCoord > 3:
            continue
        if newColCoord < 0 or newColCoord > 3:
            continue
        neighboringCoordinates.append((newRowCoord, newColCoord))
    return neighboringCoordinates


if __name__ == '__main__':
    root = Trie()
    # Create trie
    for word in dictionary:
        root.add(word)
    # Begin DFS on each cell
    print("Found Words:")
    for row in range(4):
        for col in range(4):
            currentLetterCoords = (row, col)
            dfs(currentLetterCoords, "", [], root.root)