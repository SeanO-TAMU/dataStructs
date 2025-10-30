class Node:
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        print("Inserting: ", word)
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                print("Creating new node: ", c)
                node.children[c] = Node()
                node = node.children[c]

        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        
        return node.is_end_of_word #only returns true if it is actual word in dict

    def delete(self, word):
        #only want to remove characters that don't belong to other words
        self._delete(self.root, word, 0)

    def has_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
    
        return True #just returns true if prefix exists

    def start_with(self, prefix):
        #gives all words that start with a prefix
        words = []
        node = self.root

        #get to whrere prefix ends
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return words
            
        #now here is where we do dfs only resetting when we get to char with no children
        def _dfs(current_node, path):
            if current_node.is_end_of_word:
                words.append(''.join(path))
                
            for c in current_node.children:
                node = current_node.children[c]
                _dfs(node, path + [c])
        
        _dfs(node, list(prefix))
        
        return words

    def list_words(self):
        #list all words in dictionary
        words = []

        def _dfs(current_node, path):
            if current_node.is_end_of_word:
                words.append(path)
                
            for c in current_node.children:
                node = current_node.children[c]
                _dfs(node, path + c)
        
        _dfs(self.root, '')

        return words
        

    def _delete(self, current_node, word, index):
        if index == len(word):
            if not current_node.is_end_of_word:
                return False #if we end up in a place that isn't a word don't need to worry about upper leves since we don't need to delete
            
            current_node.is_end_of_word = False #removing word from dictionary

            return len(current_node.children) == 0
        
        c = word[index]
        node = current_node.children[c]

        if node is None:
            return False

        delete_current_node = self._delete(node, word, index + 1)

        if delete_current_node:
            del current_node.children[c]
            return len(current_node.children) == 0 and not current_node.is_end_of_word

        return False


dictionary = Trie()
dictionary.insert("hello")
dictionary.insert("help")
dictionary.insert("hell")
dictionary.insert("heck")
dictionary.insert("he")
dictionary.insert('cat')
dictionary.insert('call')
dictionary.insert('carp')
dictionary.insert('car')



#search test
print("Search test")
print(dictionary.search("car"))
print(dictionary.search("cars"))

#has prefix test
print("Prefix test")
print(dictionary.has_prefix("cal"))

#delete test
print("Deleting he")
dictionary.delete("he")

#start_with test
myDict = dictionary.start_with("he")
print("Printing all words starting with he")
for i in myDict:
    print (i)

#list_words test
myDict = dictionary.list_words()
print("Printing all words in dictionary")
for i in myDict:
    print (i)