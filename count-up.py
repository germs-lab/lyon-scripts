#!/usr/bin/python

import sys

if len(sys.argv) < 2:
    print "USAGE:  python count-up.py *blastfiles. Your results will be in summary-count.tsv"

d_gene = {}

for f in sys.argv[1:]:
    for line in open(f):
        query = f.split('.')[0]
        dat = line.rstrip().split('\t')
        gene = dat[1]
        if d_gene.has_key(gene):
            d_gene[gene][query] = d_gene[gene].get(query,0) + 1
        else:
            d_gene[gene] = {}
            d_gene[gene][query] = 1

fp = open('summary-count.tsv', 'w')

blast_outputs = sys.argv[1:]

for x in blast_outputs:
    fp.write('\t%s' % x.split('.')[0])

fp.write('\n')

for gene in d_gene:
    fp.write('%s\t' % gene)
    for x in blast_outputs:
        x1 = x.split('.')[0]
        if d_gene[gene].has_key(x1):
            fp.write('%s\t' % d_gene[gene][x1])
        else:
            fp.write('0\t')
    fp.write('\n')




