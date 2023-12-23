from pair import Pair

class Map:
    def __init__(self):
        self.root = None
    
    def display(self):
        self.root.display()
    
    def lookup(self, key):
        pair = self.root
        while pair is not None:
            if pair.key == key:
                return pair.value
            elif pair.key > key:
                pair = pair.left
            else:
                pair = pair.right
        
        return False

    def set(self, key, value):
        if self.lookup(key):
            print(f"{key} Already Exists")
            return
        
        pair = Pair(key, value)
        p = self.root

        if p is None:
            self.root = pair
            return 

        while True:
            if key == p.key:
                p.value = value
                return # update the value and exit
            elif key < p.key:
                if p.left:
                    p = p.left
                else:
                    p.left = pair
                    return # insert the pair if LEFT DNE
            else:
                if p.right:
                    p = p.right
                else:
                    p.right = pair
                    return # insert the pair if RIGHT DNE
    
    def remove(self, key):
        '''
        Deleting a value from a binary search tree is a bit trickier. 
        It's not hard to find the node to delete: we just walk down the tree, 
        just like when searching or inserting. Once we've found the node N we want to delete, 
        there are several cases.
            If N is a leaf (it has no children), we can just remove it from the tree.

            If N has only a single child, we replace N with its child. For example, 
            we can delete node 15 in the binary tree above by replacing it with 18.

            If N has two children, then we will replace its value by the next highest value in the tree. 
            To do this, we start at N's right child and follow left child pointers for as long as we can. 
            This wil take us to the smallest node in N's right subtree, 
            which must be the next highest node in the tree after N.
            Call this node M. We can easily remove M from the right subtree: 
            M has no left child, so we can remove it following either case (a) or (b) above. 
            Now we set N's value to the value that M had.

            As a concrete example, suppose that we want to delete the root node 
            (with value 10) in the tree above. 
            This node has two children. We start at its right child (20) and follow its 
            left child pointer to 15. That’s as far as we can go in following left child pointers, 
            since 15 has no left child. So now we remove 15 (following case b above), 
            and then replace 10 with 15 at the root.

        We won't give an implementation of this operation here, but writing this yourself is an excellent (and somewhat challenging) exercise.
        '''

