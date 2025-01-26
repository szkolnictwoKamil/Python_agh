class Aho_corasick:  
    def __init__(self):  
        self.goto = {}
        self.out = []
        self.breaks = None
        
    def __repr__(self):
        p = self.out
        print(p)

def make_tree(words):  
    root = Aho_corasick() 

    for word in words:  #making the tree with each word
        point = root
        for letter in word: 
            point = point.goto.setdefault(letter, Aho_corasick()) 
        point.out.append(word)
    return root

def bfs(words): 
    root = make_tree(words) 
    q = [] # queue
    for point in iter(root.goto.values()): # Iterating through the elements of a dictionary, we create a queue for breadth-first search
        q.append(point)
        point.breaks = root # creating failedlinks

    while q:
        rightpoint = q.pop(0) #We perform a breadth-first search through the nodes.
        for node, unique_point in rightpoint.goto.items():
            q.append(unique_point)
            firstpoint = rightpoint.breaks
            while firstpoint is not None and node not in firstpoint.goto:
                firstpoint = firstpoint.breaks
            unique_point.breaks = firstpoint.goto[node] if firstpoint else root
            unique_point.out = unique_point.out + unique_point.breaks.out
    point = root

def search_pattern(text, call): 
    root = make_tree(words) 
    point = root
    for i,a in enumerate(text): 
        while point is not None and a not in point.goto:
            point = point.breaks
        if point == None:
            point = root
        if a in point.goto:
            point = point.goto[a]
        for word in point.out:
            call(word,i - len(word) + 1)


def found( words, loc):
    print("Wzorzec {} znaleziono na pozycji {}".format(words, loc))

words = ['abb', 'ab','cał']
text = "abbcał"
search_pattern(text, found)