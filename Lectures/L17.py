a = list("smnpbnnaaaaa$a")
a_sorted = sorted(a)

count = {}
for i in range(len(a)):
    char = a[i]
    if char not in count.keys():
        count[char] = 1
    else:
        count[char] += 1
    a[i] = char + str(count[char])

count = {}
for i in range(len(a_sorted)):
    char = a_sorted[i]
    if char not in count.keys():
        count[char] = 1
    else:
        count[char] += 1
    a_sorted[i] = char + str(count[char])

l2f = []
for i in range(len(a)):
    l2f.append(a_sorted.index(a[i]))
