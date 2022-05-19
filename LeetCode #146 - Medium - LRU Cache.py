'''
    1. What is a cache?
        - allows fast access to specific data
        - has limited capacity
        
    2. Problem Overview
        - implementing class (more like OOP)
    
        - get O(1)
        - put O(1)
        - has a finite capacity
        
    3. How would we build this cache
        - hashMap (dictionary)
        
        - ordering: arrays, linked lists
        - doubly linked list
        
        {k1, k2, k3}
        
        [v1] <--> [v2] <--> [v3]
        [v3] <--> [v1] <--> [v2]
        
        Why these data structures
        - dictionary O(1) get and put
        - doubly linked list: remove, insert nodes O(1)
        
        Why not array?
        - O(n) for reordering the array
        
        Why not singly linked list?
        - cannot delete in O(1) w/o access the previous node
        
    4. Implementation Overview
        a. get ---
        
        if item in cache:
            1. update list
            2. return item
        else:
            return -1
            
        b. put ---
        
        if item in cache:
            1. update list
            2. update value
        else:
            if we're at max capacity:
                remove last item from the list
                remove last item from our dictionary
            update dictionary with new item
            update our list with new item
            
    5. Corner cases
        capacity = 0, 1
        
    6. Time and space
        time --
        O(1) get and put
        
        space --
        O(n)
        
'''

class Node(object):
    def __init__(self, key = None, value = None, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.lib = {}
        self.head = Node()
        self.tail = Node()
        
        self.head.right = self.tail
        self.tail.left = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.lib:
            node = self.lib[key]
            self._removeNode(node)
            self._insertAfter(self.head, node)
            return node.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.lib:
            node = self.lib[key]
            self._removeNode(node)
            self._insertAfter(self.head, node)
            node.value = value
            return
        if len(self.lib) == self.capacity:
            remove = self.tail.left
            self._removeNode(remove)
            del self.lib[remove.key]
        node = Node(key, value)
        self._insertAfter(self.head, node)
        self.lib[key] = node
        
    def _removeNode(self, node):
        '''  [a] <--> [b] <--> [c] '''
        node.right.left = node.left
        node.left.right = node.right
    
    def _insertAfter(self, prev, node):
        ''' [a] <--> [c] '''
        node.left = prev
        node.right = prev.right
        
        node.left.right = node
        node.right.left = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
