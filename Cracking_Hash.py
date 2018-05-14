pattern = "govt of india"
n = 500000

k = len(pattern)

list_of_a =[]
prime = 121501
bloom = [0]*prime


def find_a():

    temp = []
    for i in range(n):
        c = 0
        count = 1
        for p in pattern:
            c += ord(p)*pow(i, k-count)
            count += 1
        temp.append(c % prime)

    temp = list(sorted(set(temp)))
    print(temp)


    # Find 13 consecutive
    for i in range(n-13):
        check = temp[i]
        if temp[i] == check:
            i+=1
            check +=1
            if temp[i] == check:
                i += 1
                check += 1
                if temp[i] == check:
                    i += 1
                    check += 1
                    if temp[i] == check:
                        i += 1
                        check += 1
                        if temp[i] == check:
                            i += 1
                            check += 1
                            if temp[i] == check:
                                i += 1
                                check += 1
                                if temp[i] == check:
                                    i += 1
                                    check += 1
                                    if temp[i] == check:
                                        i += 1
                                        check += 1
                                        if temp[i] == check:
                                            i += 1
                                            check += 1
                                            if temp[i] == check:
                                                i += 1
                                                check += 1
                                                if temp[i] == check:
                                                    i += 1
                                                    check += 1
                                                    if temp[i] == check:
                                                        i += 1
                                                        check += 1
                                                        if temp[i] == check:
                                                            i += 1
                                                            check += 1
                                                            print(temp[i])
                                                            break
find_a()


def getKey(item):
    return item[0]

def find_a():
    # prime = 101
    # result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # print(temp)
    # result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = [913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926]
    temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    base_list = []

    for i in range(len(temp)):

        base = -1
        while temp[i] != result[i]:
            base += 1
            count = 1
            c = 0
            for p in pattern:
                c += ord(p)*pow(base, k-count)
                count += 1
            c = c % prime
            temp[i] = c

        base_list.append(base)
        bloom[base] = 1
        # temp.append(c % prime)
    print("Consec val: ", sorted(temp))
    print("a values: ", base_list)

    # c1 = 103
    # c2 = 111
    # c3 = 118
    # c4 = 116
    #
    # res = []
    # for b in base_list:
    #     res.append((c1*pow(b, 3) + c2*pow(b, 2) + c3*pow(b, 1) + c4*pow(b, 0))%prime)
    # print("Confirmed: ", res)

    # 6, 51, 74, 94, 2, 44, 100, 86, 3, 38
    # print(bloom)
find_a()


