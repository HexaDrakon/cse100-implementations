from collections import Counter

class Node:
    def __init__(self, value, label=None, left=None, right=None):
        self.value = value
        self.label = label
        self.left = left
        self.right = right

    def __str__(self):
        if self.label == None:
            return f"Parent node with value {self.value} and children {self.left}, {self.right}."
        else:
            return f"Child node with label {self.label} and value {self.value}"

def combine_nodes(left, right):
    total = left.value + right.value
    return Node(total, left=left, right=right)

def pretty_print_graph(root, mode='labels'): # only keeps layers, not relations (too hard :])
    out = ""
    queue = [(0, root)]
    last_height = 0
    for pair in queue:
        height = pair[0] 
        node = pair[1]
        if node.left:
            queue.append((height + 1, node.left))
        if node.right:
            queue.append((height + 1, node.right))
        if last_height != height:
            out += "\n"
            last_height = height
        if mode == 'labels':
            out += f"({node.label})"
        else:
            out += f"({node.value})"
    return out

def huffman(string):
    count = Counter(string)
    print(count)
    labels = count.keys()

    nodes = []
    
    for label in labels:
        nodes.append(Node(count[label], label))

    nodes.sort(key = lambda x: x.value)

    while len(nodes) > 1:
        left, right = nodes.pop(0), nodes.pop(0)
        nodes.append(combine_nodes(left, right))
        nodes.sort(key = lambda x: x.value) # this is not necessary -- since the list is already sorted, we can insert a new item in O(logn) time but im lazy
        # also im like 90% sure that the python builtin sort will handle this intelligently anyway
    return nodes[0]

def explore(code, node):
    if not node.left and not node.right:
        return [(code, node)]
    nodelist = []
    if node.left:
        nodelist += explore(code + "0", node.left)
    if node.right:
        nodelist += explore(code + "1", node.right)
    return nodelist

def generate_code(root):
    encoding = {}
    decoding = {}
    nodelist = explore("", root)
    for code, node in nodelist:
        encoding[node.label] = code
        decoding[code] = node.label
    return (encoding, decoding)

def encode(string, encoding):
    out = ""
    for char in string:
        out += encoding[char]
    return out

def decode(string, decoding):
    out = ""
    curr_code = ""
    for char in string:
        curr_code += char
        if curr_code in decoding.keys():
            out += decoding[curr_code]
            curr_code = ""
    return out

def count_nodes(root):
    count = 1
    if root.left:
        count += count_nodes(root.left)
    if root.right:
        count += count_nodes(root.right)
    return count
     
string = "I" * 87 + "H" * 82 + "T" * 75 + "R" * 68 + "N" * 52 + "S" * 44 + "E" * 41 + "C" * 40 + "A" * 30 + "O" * 23 + "+" * 16

root = huffman(string)
encoding, decoding = generate_code(root)


print(pretty_print_graph(root))
print(count_nodes(root))
print(decode("0010111101110111100011101110000111000101111100", decoding))
