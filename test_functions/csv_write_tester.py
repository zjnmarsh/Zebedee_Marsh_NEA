# import csv
import json

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

filename = "text.txt"
final = []
with open(filename, 'r') as file:
    lines = [line.rstrip('\n') for line in file]

if lines[-1] == "":
    del lines[-1]
#
# print(lines)
#
# for item in lines:
#     final.append(json.loads(item))
#
# print(final)

# print(json.loads(lines[2]))
res = lines[2].strip('][').split(', ')
# print(res)

print([item.strip('][').split(', ') for item in lines])

# print(json.loads(lines[0]))

# print(list1)



