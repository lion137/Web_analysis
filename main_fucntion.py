# crawler 
import urllib.request
from parse_tree import *
import re
url = 'http://www.example.com/'
s = set()
List = []
def f_go(List, s, url, iter_cnt):
    try:
        if iter_cnt > 200:
            return
        if url in s:
            return
        s.add(url)
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print("here", url)
        h = html.decode("utf-8")
        lst0 = prepare_expression(list(h))
        ntr = buildNaryParseTree(lst0)
        lst1 = []
        lst2 = nary_tree_tolist(ntr, lst1)
        List.append(lst2)
        f1 = re.finditer(str_regex, h)
        l1 = []
        for tok in f1:
            ind1 = tok.span()
            l1.append(h[ind1[0]:ind1[1]])
        for exp in l1:
            f_go(List, s, exp, iter_cnt + 1)
    except:
        return
