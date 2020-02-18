lines = open("input2.txt", "r").readlines()
dna = lines[0].strip()
k = int(lines[1])
profile = [map(float, l.split(" ")) for l in lines[2:]]

def calculate_probablity(kmer):
    t = []
    for i in range(len(kmer)):
        if kmer[i] == 'A':
            t.append(profile[0][i])
        elif kmer[i] == 'C':
            t.append(profile[1][i])
        elif kmer[i] == 'G':
            t.append(profile[2][i])
        elif kmer[i] == 'T':
            t.append(profile[3][i])
    return reduce(lambda x, y: x*y, t, 1)


pattern = ""
probability = 0.0000
for i in range(len(dna) - k + 1):
    kmer = dna[i:i+k]
    if calculate_probablity(kmer) > probability:
        pattern = kmer
        probability = calculate_probablity(kmer)

print pattern