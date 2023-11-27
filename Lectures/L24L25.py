FOREST = [-1] * 8
COMPRESS = True

def find(forest, x, compress=False):
    if compress:
        path = []
    currVal = x
    nextVal = forest[currVal] # not strictly necessary but saves headaches
    while nextVal != -1:
        if compress:
            path.append(currVal)
        currVal = nextVal
        nextVal = forest[currVal]
    if compress:
        for i in path:
            forest[i] = currVal
    return currVal

def union(forest, x, y, compress=False, method=None):
    # TODO: implement union-by-size and union-by-height
    if not method: # default behavior is to make sentinel of x point at sentinel of y
        x_sent = find(forest, x, compress=compress)
        y_sent = find(forest, y, compress=compress)
        forest[x_sent] = y_sent

union(FOREST, 0, 1, compress=COMPRESS)
union(FOREST, 2, 3, compress=COMPRESS)
union(FOREST, 0, 2, compress=COMPRESS)
union(FOREST, 4, 0, compress=COMPRESS)
union(FOREST, 5, 6, compress=COMPRESS)
union(FOREST, 7, 5, compress=COMPRESS)
union(FOREST, 5, 4, compress=COMPRESS)
print(find(FOREST, 5, compress=COMPRESS))
