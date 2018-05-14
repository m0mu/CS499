from bitarray import bitarray
import Server



bloom_filter = Server.find_a()
matched_bf = [0]*len(bloom_filter)
window_length = 13
prime = 121501


def do_hash(fragment):
    h_index = [28125, 64168, 7548, 42363, 32001, 99007, 65647, 33133, 113529, 71322, 82087, 110173, 69241]

    result = []
    for i in range(window_length):
        count = 1
        c = 0
        for j in range(window_length):
            c += ord(fragment[j])*pow(h_index[i], window_length-count)
            count += 1
        result.append(c % prime)
    return result


# file = open("Text1.txt", "rb")

# text = 0
# for f in file.readlines():
#     text = f.decode("utf-8").split()

with open('Text1.txt') as f:
    file = [f.read()]
    # file = list(map("".join, zip(*[iter(file)] * window_length)))

# print(file)

for fragment in file:
    if len(fragment) >= window_length:
        for i in range(len(fragment)-window_length+1):
            # print(fragment[i:i+window_length])
            hashes_returned = do_hash(fragment[i:i+window_length])
            for h in hashes_returned:
                matched_bf[h] = 1
    # print(matched_bf)

print("Abv: ", bloom_filter)
print("Mbv: ", matched_bf)
# print(bloom_filter.index(1))
