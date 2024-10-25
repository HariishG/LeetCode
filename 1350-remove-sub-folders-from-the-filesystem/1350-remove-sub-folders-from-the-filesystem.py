class TrieNode:
    def __init__(self, val, isLeaf=False):
        self.val=val
        self.isLeaf=isLeaf
        self.children={}

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root=TrieNode('')
        for path in folder:
            l=path[1:].split('/')
            start=root
            for f in l:
                if f in start.children:
                    start=start.children[f]
                else:
                    start.children[f]=TrieNode(f)
                    start=start.children[f]
            start.isLeaf=True
            
        def func(root, path):
            if root.isLeaf==True:
                self.res.append(path)
                return
            for child in root.children:
                func(root.children[child], path+'/'+root.children[child].val)
        self.res=[]       
        func(root, '')
        return self.res