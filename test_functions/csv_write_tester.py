# import csv
import json
import numpy as np

a = [[1, 2, 3], [11, 22, 33], [4, 5, 6]]
b = [["a","b","c"], ["ad","bd","cd"], ["afds","bfds","cfds"]]

#
# with open("output.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(a)


# filename = "output.txt"
# with open(filename, 'w') as file:
#     file.write(str(a) + "\n")
#     file.write(str(b))



filename = "../other_files/ca_output.txt"
final = []
with open(filename, 'r') as file:
    lines = [line.rstrip('\n') for line in file]

# for item in lines:
#     final.append(json.loads(item))

listy = [json.loads(item) for item in lines]

# for listx in final:
#     print(listx)



#
#
# if lines[-1] == "":
#     del lines[-1]
#
# ok = [item.strip('][').split(', ') for item in lines]
#
# print(ok[0])



#
# print(lines)
#
# for item in lines:
#     final.append(json.loads(item))
#
# print(final)

# print(json.loads(lines[2]))
# res = lines[2].strip('][').split(', ')
# print(res)



# threenum, num, booleans = ok
#
# print(threenum)
# print(num)
# print(booleans)

# print(json.loads(lines[0]))

# print(list1)



