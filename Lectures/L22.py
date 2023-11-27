# cringe assignment
import heapq

# node labels just for niceness? idk
LABEL = list('ABCDEFGH')

# use cost for normal adjacencies, -1 for no adjacency
GRAPH = [[-1,  1,  4, -1, -1, 25, -1, -1,],
         [ 1, -1,  2, 19, 14, -1,  6, -1,],
         [ 4, -2, -1, -1, -1, -1, -1,  3,],
         [-1, 19, -1, -1,  9,  5,  7, -1,],
         [-1, 14, -1,  9, -1, 12,  2, -1,],
         [25, -1, -1,  5, 12, -1, -1, -1,],
         [-1,  6, -1,  7,  2, -1, -1,  2,],
         [-1, -1,  3, -1, -1, -1,  2, -1,],]

# simple priority queue (efficient? no. am i writing a fibonacci heap? also no. deal with it.)
class PriorityQueue: # technically we want to subclass this to object, so theoretically this needs to be nonempty i.e. PriorityQueue(Object) but screw it
    def __init__(self):
        self.heap = []
        self.data_map = {}
        self.remove_data = "l + ratio"

    def __str__(self):
        return ''.join([str(i) for i in self.heap])

    """def __repr__(self):
        return ''.join([str(i) for i in self.heap])
    """

    # i'm not writing a heap lmao
    def insert(self, priority, data):
        if data in self.data_map:
            self.remove(data)
        self.data_map[data] = [priority, data]
        heapq.heappush(self.heap, self.data_map[data])

    # we "remove" an item by...changing it to "removed"
    # very elegant, i know
    # since we leverage a dict, this is average O(1) instead of O(n), which i'll take as a W
    def remove(self, data):
        self.data_map[data][-1] = self.remove_data

    # no input validation on this baby
    def pop(self):
        while self.heap:
            priority, data = heapq.heappop(self.heap)
            if data != self.remove_data:
                del self.data_map[data]
                return (priority, data)
        return None

    def is_empty(self):
        return not self.heap

# yeah you need to be checked, don't you? you dirty little human
# cant even enter graphs properly
def check(graph, undirected=False, pseudo=False):
    # verify square matrix
    rows = len(graph)
    square = all([len(row) == rows for row in graph])
    if not square: # we check this in advance because other calculations assume square matrix
        return False

    # verify no self-loops if not pseudograph
    no_loops = True
    if not pseudo:
        no_loops = all([graph[idx][idx] == -1 for idx in range(len(graph))])      

    # verify symmetry if undirected
    symmetric = True
    if undirected:
        for row_idx in range(len(graph)):
            for col in range(row_idx + 1, len(graph)):
                if graph[row_idx][col] == graph[col][row_idx]:
                    symmetric = False

    return all([no_loops, symmetric])

# assumes no negative weights, but i think it can handle everything else
def djikstras(graph, start_node, verbose=False, label=None):
    if verbose:
        print(f"Beginning at node {start_node}.")
    if label:
        start_node = label.index(start_node)

    dists = {}
    visited = []

    for node in range(len(graph)):
        if node == start_node:
            dists[node] = [0, None]
        else:
            dists[node] = [-1, None]
        
    queue = PriorityQueue()
    queue.insert(0, start_node)
    while not queue.is_empty():
        vals = queue.pop() # needed because sometimes this pops empty
        if not vals:
            continue
        dist, curr = vals
        visited.append(curr)
        print(f"Popped node {curr if not label else label[curr]}.")
        for idx, n_dist in enumerate(graph[curr]):
            if idx in visited:
                continue
            if n_dist != -1:
                if dists[idx][0] == -1:
                    print(f"New path found to node {idx if not label else label[idx]} with distance {n_dist}.")
                    dists[idx][0] = n_dist
                    dists[idx][1] = curr
                    queue.insert(n_dist, idx)
                    if verbose:
                        print(f"Inserting node {idx if not label else label[idx]}.")
                if dist + n_dist < dists[idx][0]:
                    print(f"Distance to node {idx if not label else label[idx]} updated from {dists[idx][0]} to {dist + n_dist}.")
                    dists[idx][0] = dist + n_dist
                    dists[idx][1] = curr
                    queue.insert(dist + n_dist, idx)
                    if verbose:
                        print(f"Inserting node {idx if not label else label[idx]}.")
        print(f"Node {curr if not label else label[curr]} exhausted, popping next.")
    return dists

print(check(GRAPH))
print(djikstras(GRAPH, 'A', verbose=True, label=LABEL))
