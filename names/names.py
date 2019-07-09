import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
def de_dupe():
    cur_name = ""
    cur_name_2 = ""
    name_set1_len = len(names_1)
    i = 0
    while name_set1_len > i:
        print(len(names_1))
        cur_name = names_1[i]
        for name_2 in names_2:
            j = i
            cur_name_2 = names_2[j]
            if cur_name == cur_name_2:
                duplicates.append(cur_name_2)
            j -= 1
        i += 1
    return duplicates

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
