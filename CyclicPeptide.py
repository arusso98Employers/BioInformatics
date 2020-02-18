amino_acid = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115,
               'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def mass_of_peptide(pep):
    return sum([amino_acid[i] for i in pep])


def linear_spectrum(peptide):
    prefix_mass = [0]
    lp = len(peptide)
    for i in peptide:
        prefix_mass.append(prefix_mass[-1] + amino_acid[i])
    res = [0]
    for i in range(0, lp):
        for j in range(i + 1, lp + 1):
            res.append(prefix_mass[j] - prefix_mass[i])
    return sorted(res)


def cyclic_spectrum(peptide):
    prefix_mass = [0]
    lp = len(peptide)
    peptide = peptide + peptide
    for i in peptide:
        prefix_mass.append(prefix_mass[-1] + amino_acid[i])
    res = [0, prefix_mass[lp]]
    for i in range(0, lp):
        for j in range(1, lp):
            res.append(prefix_mass[i + j] - prefix_mass[i])

    return sorted(res)

s = "0 97 99 115 115 129 129 137 137 137 212 228 230 234 236 244 258 274 274 327 349 357 359 365 371 373 373 411 456 464 472 486 488 494 502 508 510 585 587 593 601 607 609 623 631 639 684 722 722 724 730 736 738 746 768 821 821 837 851 859 861 865 867 883 958 958 958 966 966 980 980 996 998 1095"

def solve():
    spectrum = list(map(int, s.split(" ")))

    parent_mass = max(spectrum)
    peptides = set([""])
    ans = []
    while len(peptides) != 0:
        peptides = set([t + n for n in amino_acid for t in peptides])
        removed = []
        for pep in peptides:
            if mass_of_peptide(pep) == parent_mass:
                pep_spectrum = cyclic_spectrum(pep)
                if pep_spectrum == spectrum:
                    ans.append(pep)
                removed.append(pep)
            else:
                t = linear_spectrum(pep)
                for i in t:
                    if i not in spectrum:
                        removed.append(pep)
                        break
        peptides = peptides.difference(set(removed))

    def print_ans(pep):
        return '-'.join([str(mass_of_peptide(t)) for t in pep])

    print(' '.join(set([print_ans(pep) for pep in ans])))

solve()