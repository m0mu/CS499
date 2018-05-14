# pattern = "govt"
# n = 100
#
# k = len(pattern)
#
# list_of_a =[]
# bloom = [0]*101
# prime = 101
#
# # prime = 199
# # def find_a():
# #     # prime = 199
# #
# #     temp = []
# #     for i in range(n):
# #         c = 0
# #         count = 1
# #         for p in pattern:
# #             c += ord(p)*pow(i, k-count)
# #             count += 1
# #         temp.append(c % prime)
# #     print(set(sorted(temp)))
# #
# #
# # find_a()
#
#
# def getKey(item):
#     return item[0]
#
# def find_a():
#     # prime = 101
#     # result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     # temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     # print(temp)
#     result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     temp = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     base_list = []
#
#
#     for i in range(len(temp)):
#
#         base = -1
#         while temp[i] != result[i]:
#             base += 1
#             count = 1
#             c = 0
#             for p in pattern:
#                 c += ord(p)*pow(base, k-count)
#                 count += 1
#             c = c % prime
#             temp[i] = c
#             # if base % 1000000 == 0:
#                 # print(base)
#         base_list.append(base)
#         bloom[base] = 1
#         # temp.append(c % prime)
#     print("Target: ", sorted(temp))
#     print("Indexes: ", base_list)
#
#     c1 = 103
#     c2 = 111
#     c3 = 118
#     c4 = 116
#
#     res = []
#     for b in base_list:
#         res.append((c1*pow(b, 3) + c2*pow(b, 2) + c3*pow(b, 1) + c4*pow(b, 0))%prime)
#     print("Confirmed: ", res)
#
#     # 6, 51, 74, 94, 2, 44, 100, 86, 3, 38
#     # print(bloom)
#     return bloom
#
# print("Returned bloom: ", find_a())

window_length = 13
prime = 121501
bloomfilter = [0]*prime

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


def find_a():
    file = open("Text2_Server.txt", "rb")

    text = 0
    for f in file.readlines():
        text = f.decode("utf-8")
        text = list(map("".join, zip(*[iter(text)] * window_length)))

    for fragment in text:
        if len(fragment) >= window_length:
            for i in range(len(fragment)-window_length+1):
                # print(fragment[i:i+window_length])
                hashes_returned = do_hash(fragment[i:i+window_length])
                # print(hashes_returned)
                for h in hashes_returned:
                    bloomfilter[h] = 1

    print("Abv: ", bloomfilter)
    print("First 1 found at: ", bloomfilter.index(1))
    return bloomfilter
    # for i in range(bloomfilter.index(1)):
    #     print(i, end=' ')

find_a()


