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

def queryData(queries):
    # text = [line.strip() for line in open(dataPath+'dbsnp.txt')]
    # for line in text:

    querySNP = {}
    for q in queries:
        querySNP[q] = None

    with open(dataPath+'dbsnp.txt') as f:
        for line in f:
            items = line.split('\t')
            rsid = rp(items[1])
            chrid = rp(items[3])
            chrposition = rp(items[4])
            allele = rp(items[5])
            gene = rp(items[8].split(';')[0])

            if rsid in querySNP:
                querySNP[rsid] = (chrid, chrposition, allele, gene)

    return querySNP