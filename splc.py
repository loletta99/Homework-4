# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:55:48 2019

@author: Rosa
"""

with open('rosalind_splc.txt', 'r') as file:

    text = file.read()



introns = {}



items = text.split('>')



dna = ''.join(items[1].split('\n')[1:])



for item in items[2:]:

    item = item.split('\n')

    string_id = item.pop(0)

    introns[string_id] = ''.join(item)



for intron in introns.values():

    dna = dna.replace(intron, '')

    

rna = dna.replace('T', 'U')



codon_table =  {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",

                "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",

                "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",

                "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",

                "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",

                "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",

                "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",

                "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",

                "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",

                "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",

                "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",

                "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",

                "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",

                "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",

                "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",

                "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

    

protein = ''

for codon in range(0, len(rna), 3):

    for key, value in codon_table.items():

        if rna[codon:codon +3] == key:

            protein += value

            

print(protein)