import os



import tokenize
from collections import OrderedDict
import time
from os import listdir
import collections
import pickle
import sys
import glob
print("For the terms in array given:")
dictDocFreq,dictDocList,stemDocList,docPosts,dictDocFreql,dictDocListl,lemDocList,docPostl= tokenize.tokens()
#index1=spimi.spimi_invert(stem,150000)
#spimi_blocks = [open('/Users/rld1996/Desktop/untitled folder/index blocks/'+block) for block in listdir('/Users/rld1996/Desktop/untitled folder/index blocks/')]
#spimi.merge_blocks(spimi_blocks)
#spimi.spimi(stem,150000)
s,l=tokenize.extra()
start1=time.time()
fd = open('index2.uncompressed', 'wb')
dictDf=collections.OrderedDict(sorted(dictDocFreq.items()))
dictDocL=collections.OrderedDict(sorted(dictDocList.items()))
fd.write(bytearray("term:DocumentFrequency|||| docid,termfreq,doclen,max_term_frequency||"))
for term in dictDocL:
    fd.write(bytearray(term + ":" + str(dictDf[term])+"||||"))
    if term in s:
        print("term name:"+term,"DF:"+str(dictDf[term]))
        print("posting:\n doc,tf,docLen,max_tf\n")
    d=dictDocL[term]
    for doc in d:
        tfd=stemDocList[(term,doc)]
        d,m=docPosts[doc]
        if term in s:
            print(str(doc)+","+str(tfd)+","+str(d)+","+str(m)+"\n")
        fd.write(bytearray(str(doc)+","+str(tfd)+","+str(d)+","+str(m)+"||"))
    #fd.write("\n")

fd.close()
end1=time.time()

print("1 st stems uncompressed:"+str(end1-start1))

start2=time.time()
fd1 = open('index1.uncompressed', 'wb')
dictDfl=collections.OrderedDict(sorted(dictDocFreql.items()))
dictDocLl=collections.OrderedDict(sorted(dictDocListl.items()))
fd1.write(bytearray("term:DocumentFrequency|||| docid,termfreq,doclen,max_term_frequency||"))
for term in dictDocLl:
    fd1.write(bytearray(term + ":" + str(dictDfl[term])+"||||",'utf-8'))
    d=dictDocLl[term]
    for doc in d:
        tfd=lemDocList[(term,doc)]
        d,m=docPostl[doc]
        fd1.write(bytearray(str(doc)+","+str(tfd)+","+str(d)+","+str(m)+"||"))
fd1.close()
end2=time.time()

print("2 st lemmas uncompressed:"+str(end2-start2))
#tokenize.
# block()
start3=time.time()
tokenize.frontcode()
end3=time.time()
print("1 st lemas compressed:"+str(end3-start3))
start4=time.time()
tokenize.blockl()
end4=time.time()
print("1 st stems compressed:"+str(end4-start4))
#tokenize.frontcodelem()
print("size of stems dictionary uncompressed:"+str(os.path.getsize("a.uncompressed")))
print("size of lemmas dictionary uncompressed:"+str(os.path.getsize("alem.uncompressed")))
print("size of stems dictionary compressed:"+str(os.path.getsize("Stem.compressed")))
print("size of lemmas dictionary compressed:"+str(os.path.getsize("blem.compressed")))
all=[]
'''
def writeDictToFile():
    fd1 = open('/Users/rld1996/Desktop/a.txt', 'rb')
    for line in fd1:
        all.append(line)
    with open('/Users/rld1996/Desktop/x', 'wb') as handle:
      pickle.dump(all, handle)

#tokenize.frontcoding()



def spimi():
    fd = open("/Users/rld1996/Desktop/a.txt", 'r')
    limit=10000
    token_stream=[]
    bno=0
    for line in fd:
        if len(token_stream)<limit or line!="":
            token_stream.append(line)
        bno+=1
    writeBlock(token_stream,bno)
    token_stream=[]
    merge()

def writeBlock(token_stream,bno):
    fd = open("/Users/rld1996/Desktop/blocks"+"/block"+str(bno), 'w')
    for stream in token_stream:
        fd.write(stream)
    fd.close()
    print("block"+str(bno)+"written")

def merge():
    fd = open("/Users/rld1996/Desktop/spimiIndex", 'w')
    files = glob.glob("/Users/rld1996/Desktop/blocks/*")
    for block in files:
        f=open(block,'r')
        for line in f:
            fd.write(line)

    fd.close()
    print("merge completed")



'''
low1=sorted(dictDocFreq.values())
i=list(dictDocFreq.keys())[list(dictDocFreq.values()).index(low1[0])]
j=list(dictDocFreq.keys())[list(dictDocFreq.values()).index(low1[-1])]
print("dictionary stem with lowest df:",i)
print("dictionary stem with highest df:",j)
low2=sorted(dictDocFreql.values())
i1=list(dictDocFreql.keys())[list(dictDocFreql.values()).index(low2[0])]
j1=list(dictDocFreql.keys())[list(dictDocFreql.values()).index(low2[-1])]
print("dictionary term with lowest df:",i1)
print("dictionary term with highest df:",j1)
print("NASA posting list:")

for term in dictDocL:

    if term in s and term=='nasa':

        print("posting:\n doc,tf,docLen,max_tf\n")
    d=dictDocL[term]
    for doc in d:
        tfd=stemDocList[(term,doc)]
        d,m=docPosts[doc]
        if term in s and term=='nasa':
            print(str(doc)+","+str(tfd)+","+str(d)+","+str(m)+"\n")


