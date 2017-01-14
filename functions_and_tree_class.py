# html crawling functions and tree class

class NaryTree:
    """n ary tree, Python list as an array of children"""	
    def __init__(self, rootObj):
        self.key = rootObj
        self.parent = None
        self.kids = None

    def insert(self, newNode):
        if self.kids:
            t = NaryTree(newNode)
            self.kids.append(t)
            t.parent = self
        else:
            t = NaryTree(newNode)
            self.kids = []
            self.kids.append(t)
            t.parent = self

    def setRootVal(self, obj):
        self.key.append(obj)

    def getRootVal(self):
        return self.key

    def getParent(self):
        return self.parent

    def getNthKid(self, i=-1): # return a child index i, the first from right if i not specified
        return self.kids[i]


def buildNaryParseTree(lexp):
    e_tree = NaryTree([])
    cur = e_tree
    ctr = 0
    ctr1 = 0
    for token in lexp:
        if token == '<p>':
            cur.insert([])
            cur = cur.getNthKid()
            ctr += 1
            #if ctr1 is not 0:
             #   ctr1 -= 1
        elif token == '<title>':
            cur.insert([])
            cur = cur.getNthKid()
            ctr1 += 1
        elif not token in ['<p>', '</p>', '<title>', '</title>'] and (ctr is not 0 or ctr1 is not 0):
            cur.setRootVal(token)
        elif token == '</p>':
            ctr -= 1
            cur = cur.getParent()
        elif token == '</title>':
            ctr1 -= 1
            cur = cur.getParent()
    return e_tree	

def traverse(tree): # dfs over tree
    if tree:
        stk = []
        stk.append(tree)
        while len(stk) > 0:
            top = stk.pop()
            if top.kids:
                for child in top.kids:
                    stk.append(child)
            print(top.getRootVal())
    else:
        return None

def nary_tree_tolist(tree, lst): # convert tree to a list
    if tree:
        stk = []
        stk.append(tree)
        while len(stk) > 0:
            top = stk.pop()
            if top.kids:
                for child in top.kids:
                    stk.append(child)
            lst.append(top.getRootVal())
        return lst
    else:
        return None

def prepare_expression(exp):
    """takes a page as a list and make tags visible"""
    del_list = []
    l = len(exp)
    for i in range(l):
        if exp[i] == '<' and exp[i + 1] == 'p' and exp[i + 2] == '>':
            exp[i] = '<p>'
            exp[i + 1] = []
            exp[i + 2] = []
        if exp[i] == '<' and exp[i + 1] == '/' and exp[i + 2] == 'p' and exp[i + 3] == '>':
            exp[i] = '</p>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
        if exp[i] == '<' and exp[i + 1] == 't' and exp[i + 2] == 'i' and exp[i + 3] == 't' and exp[i + 4] == 'l' and \
                        exp[i + 5] == 'e' and exp[i + 6] == '>':
            exp[i] = '<title>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
            exp[i + 5] = []
            exp[i + 6] = []
        if exp[i] == '<' and exp[i + 1] == '/' and exp[i + 2] == 't' and exp[i + 3] == 'i' and exp[i + 4] == 't' and \
                        exp[i + 5] == 'l' and exp[i + 6] == 'e' and exp[i + 7] == '>':
            exp[i] = '</title>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
            exp[i + 5] = []
            exp[i + 6] = []
            exp[i + 7] = []
    for t in range(len(exp) - 1, -1, -1):
        if isinstance(exp[t], list):
            del (exp[t])
    return exp


