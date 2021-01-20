class DNA:
    def __init__(self, dna):
        self.dna = dna


    def count_nucleotides(self):
        nucleotides = {}
        a, c, g, t = 0, 0, 0, 0
        for i in self.dna:
            if i == "A":
                a += 1
            elif i == "C":
                c += 1
            elif i == "G":
                g += 1
            elif i == "T":
                t += 1

        nucleotides["A"] = a
        nucleotides["C"] = c
        nucleotides["G"] = g
        nucleotides["T"] = t

        return nucleotides

    def calculate_complement(self):
        self.dna = self.dna[::-1]
        new_dna = ''
        for i in self.dna:
            if i == "A":
                new_dna += "T"
            elif i == "C":
                new_dna += "G"
            elif i == "G":
                new_dna += "C"
            elif i == "T":
                new_dna += "A"
        return new_dna



dna1 = DNA("AGCGTACGTAGTCGATCGATCGATGCATCG")


print(dna1.count_nucleotides())
print(dna1.calculate_complement())