def strcounter(s):

    for lit in s:
        counter = 0
        for sub_lit in s:
            if lit == sub_lit:
                counter += 1
        print(lit, counter)

strcounter('aaabccd')


s = 'aaabbcdddddd'
print(list(s))
print(set(s))

def srtcounter(s):
    for lit in set(s):
        counter = 0
        for sub_lit in s:
            if lit == sub_lit:
                counter +=1
        print(lit, counter)

srtcounter('aaabbcdddddd')



def strcounter(s):
    lits_counter = {}
    for lit in s:
        lits_counter[lit] = lits_counter.get(lit, 0) + 1
    for lit, counter in lits_counter.items():
        print(lit, counter)

strcounter('aaaaaabbcddddd')