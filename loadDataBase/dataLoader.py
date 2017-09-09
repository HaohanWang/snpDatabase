__author__ = 'Haohan Wang'

from utility.filePath import dataPath
import numpy as np

def rp(x):
    '''
    remove the punctuation
    :param x:
    :return:
    '''
    return x[1:-1]

def loadData():
    snps = {}
    text = [line.strip() for line in open(dataPath+'dbsnp.txt')]
    for line in text:
        items = line.split('\t')
        rsid = rp(items[1])
        chrid = rp(items[3])
        chrposition = rp(items[4])
        allele = rp(items[5])
        gene = rp(items[8].split(';')[0])
        print rsid, chrid, chrposition, allele, gene

        snps[rsid] = (chrid, chrposition, allele, gene)
    np.save(dataPath+'dbsnp', snps)

if __name__ == '__main__':
    loadData()