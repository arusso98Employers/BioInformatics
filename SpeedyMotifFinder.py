def main(input):
    j = -1
    ret = [j]

    for i, x in enumerate(input):
        while j >= 0 and input[j] != x:
            j = ret[j]
        j += 1
        ret.append(j)

    new_ret = ret[1:]
    print ' '.join(map(str, new_ret))

f = open("rosalind_kmp.txt", "r")
input = f.read()
input2 = input.replace(">Rosalind_8420", "")
input3 = input2.replace("\n", "")

main(input3)