from collections import Counter

def get_suffix_array(string):
    suffixes = []
    for i in range(len(string)):
        suffixes.append((string[i:], i))
    suffixes.sort()
    arr = [ str(pair[1]) for pair in suffixes ]
    return (' '.join(arr), suffixes)

def bwt(string, inverse=False):
    if not inverse:
        rotations = []
        for i in range(len(string)):
            rotations.append((string[i:] + string[:i], i))
        rotations.sort()
        arr = [ pair[0][-1] for pair in rotations ]
        return (''.join(arr), rotations)
    else:
        string_sorted = sorted(string)
        string_list = sub_repeats(string)
        sorted_list = sub_repeats(string_sorted)
        retval = ""
        idx = sorted_list.index("$1")
        while len(retval) != len(string):
            retval += sorted_list[idx][0]
            idx = sorted_list.index(string_list[idx])
        # you're supposed to take the sorted values from the unsorted values
        # but doing it this way returns $string when we want string$
        # so instead we do it backwards ($gnirts) and then just reverse it
        # this is technically worse but i didnt want to have to do like
        # return retval[1:] + retval[0]
        return retval[::-1]

def sub_repeats(string): # returns a list
    string = list(string)
    count = {}
    for i in range(len(string)):
        char = string[i]
        if char not in count.keys():
            count[char] = 1
        else:
            count[char] += 1
        string[i] = char + str(count[char])
    return string

print(get_suffix_array("GCATCGC")[0])
print(get_suffix_array("CACAGATTACACACA")[0])


print(bwt("NIEMAMOSHIRI$"))
print(bwt("ABB$AILA", True))
