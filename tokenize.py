import collections
import time
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
#from typing import List
from collections import defaultdict
import os

startToken = time.time()
import re
docPosts={}
docPostl={}
dictDocListl={}
cont = ""
stopwo=[]
import glob
stemmd={}
dictDocList=defaultdict(list)
lemm={}
stdf={}
ltdf={}
dictDocFreq={}
dictDocFreql={}
ps=PorterStemmer()
wnl=WordNetLemmatizer()
def tokens():

    stoplist = open('/people/cs/s/sanda/cs6322/resourcesIR/stopwords', 'r')
    for line in stoplist:
        line = line.strip()
        stopwo.append(line)
    p = raw_input("Enter the path of your file: ")
    if p == "":
       p = "/people/cs/s/sanda/cs6322/Cranfield"
    cnt = 0
    c = 0
    s = []  # type:
    l=[]
    tot = {}
    stemDocList={}
    lemDocList = {}
    freqs = {}
    freql={}
    average = []
    path = p + "/*"
    # path = '/Users/rld1996/Desktop/IR/Assignment 1/*.txt'
    docId=0
    unique = []
    files = glob.glob(path)
    for file in files:
        docId+=1
        max_tfs=0
        max_tfl=0
        f = open(file, 'r')
        print("file:"+f.name)
        doclen=0
        for cont in f:
            print("-----Removing Tags----")
            clean = re.compile('<.*?>')
            cont = re.sub(clean, "", cont)
            print("-----Removing Punctuations and alphanumerics----")
            cont = re.sub(r'[,-]', " ", cont)
            cont = re.sub(r'[^\w\s]', '', cont)
            print("-----Removing numbers----")
            tokens = re.sub(r'[0-9]+', ' ', cont)
            print("-----Removing blank lines----")
            tokens = tokens.strip("\n")
            #get each word of each line in b
            b = tokens.split()
            #if b is not null
            if b != []:
                #for each word in b
                for x in b:
                    stermfreq = 0
                    ltermfreq = 0
                    #convert to lowercase
                    x = x.lower()
                    doclen=doclen+len(x)
                    if x not in stopwo:
                    #add to dict
                    #remove stop words
                        lm = wnl.lemmatize(x)
                        stm = ps.stem(x)
                        stm=stm.encode('utf-8')
                        if (stm,docId) not in stemDocList:

                            stemDocList[(stm,docId)]=1
                            xt=1
                            if xt>max_tfs:
                                max_tfs=xt
                        else:
                            xt=stemDocList[(stm,docId)]
                            xt+=1;
                            stemDocList[(stm, docId)] = xt
                        #lm = lm.encode('utf-8')
                            if xt>max_tfs:
                                max_tfs=xt
                        if (lm, docId) not in lemDocList:

                            lemDocList[(lm, docId)] = 1
                            xt=1
                            if xt > max_tfl:
                                max_tfl = xt
                        else:
                            xt = lemDocList[(lm, docId)]
                            xt += 1;
                            lemDocList[(lm, docId)] = xt
                            if xt > max_tfl:
                                max_tfl = xt

                        if stm not in dictDocList:
                            tmplist = []
                            tmplist.append(docId)
                            dictDocList[stm] = tmplist
                        else:
                            if docId not in dictDocList[stm]:
                                dictDocList[stm].append(docId)
                        if lm not in dictDocListl:
                            tmplist = []
                            tmplist.append(docId)
                            dictDocListl[lm] = tmplist
                        else:
                            if docId not in dictDocListl[lm]:
                                dictDocListl[lm].append(docId)

        docPosts[docId]=(doclen,max_tfs)
        docPostl[docId] = (doclen, max_tfl)
    for term in dictDocList:
        dictDocFreq[term] = len(dictDocList[term])
    for term in dictDocListl:
        dictDocFreql[term] = len(dictDocListl[term])

    return dictDocFreq,dictDocList,stemDocList,docPosts,dictDocFreql,dictDocListl,lemDocList,docPostl


'''
def block():
    dictDocL = collections.OrderedDict(sorted(dictDocList.items()))
    block = {}
    blk = []
    b = 0
    l = 0
    string=""
    fd = open('/Users/rld1996/Desktop/b.txt', 'w')
    for term in dictDocL:
        d=dictDocList[term]
        block[term]=len(term)
        b+=1
        l=l+len(term)
        if b%8==0:
            blk.append(l)
            fd.write(str(l) + "\n")
            l=0
        fd.write(term+"\n")
        gap=[]
        gap.append(gammaCode(d[0]))
        fd.write(str(d[0])+":"+str(gap[0])[2:]+"\n")
        for i in range(1,len(d)-1):
            gap.append(gammaCode(d[i]-d[i-1]))
            fd.write(str(d[i]-d[i-1])+":"+str(gap[i])[2:]+"\n")



        string=string+str(len(term))+term


    fd.write(string + "\n")

    fd.close()
    return string,blk
'''

def blockl():
    dictDocLl = collections.OrderedDict(sorted(dictDocListl.items()))
    block = {}
    blk = []
    b = 0
    l = 0
    string = ""
    fd = open('index1.compressed', 'wb')
    for term in dictDocLl:
        d = dictDocListl[term]
        block[term] = len(term)
        b += 1
        l = l + len(term)
        if b % 8 == 0:
            blk.append(l)
            fd.write(bytearray(str(l) ))
            l = 0
        fd.write(bytearray(term,'utf-8'))
        gap = []
        gap.append(gammaCode(d[0]))
        fd.write(bytearray(str(gap[0])[2:]) )
        for i in range(1, len(d) - 1):
            gap.append(gammaCode(d[i] - d[i - 1]))
            fd.write(bytearray(str(gap[i])[2:]) )

        string = string + str(len(term)) + term

    fd.write(bytearray(string,'utf-8'))

    fd.close()
    return string, blk


def deltaCode(n):
    unary=binaryString(n)
    length=len(unary)
    lenUnary=binaryString(length)
    compressed=''
    i=1
    while(i<len(lenUnary)):
        compressed+='1'
        i+=1
    compressed+='0'+lenUnary[1:]
    compressed+=compressed+unary[1:]
    return bin(int(compressed,2))

def binaryString(n):
    return str(bin(n))[2:]

def gammaCode(n):
    unary=binaryString(n)
    compressed=''
    i=1
    while(i<len(unary)):
        compressed+='1'
        i+=1

    compressed+='0'+unary[1:]
    return bin(int(compressed,2))

def frontcode():
    dictDocL = collections.OrderedDict(sorted(dictDocList.items()))
    blcks={}
    b=0
    c=0
    blck=[]
    for term in dictDocL:
        b+=1
        if b%8!=0:
            blck.append(term)
        else:
            c+=1
            blcks[c]=blck[:]
            blck=[]
    lcp={}
    fd1 = open('index2.compressed', 'wb')
    for no in blcks:
        ad=blcks[no]
        lcp[no]=os.path.commonprefix(ad)


        #fd1.write("Block"+str(no)+":")
        #fd1.write(str(lcp[no]))
        fc=str(len(lcp[no]))+str(lcp[no])+"*"
        for t in ad:
            fc=fc+t[len(lcp[no]):]+str(len(t)-len(lcp[no]))+"$"
        fd1.write(bytearray(fc))
    #fd1.write("-----------------------------\n")
    for no in blcks:
        terms=blcks[no]
        #fd1.write("Block" + str(no) + ":\n")
        for t in terms:
            d=dictDocList[t]
            gap=[]
            gap.append(deltaCode(d[0]))
            fd1.write(bytearray(str(gap[0])[2:] ))
            for i in range(1, len(d) - 1):
                gap.append(deltaCode(d[i] - d[i - 1]))
                fd1.write( bytearray(str(gap[i])[2:] ))


    fd1.close()

'''
def frontcodelem():
    dictDocLl = collections.OrderedDict(sorted(dictDocListl.items()))
    blcks={}
    b=0
    c=0
    blck=[]
    for term in dictDocLl:
        b+=1
        if b%8!=0:
            blck.append(term)
        else:
            c+=1
            blcks[c]=blck[:]
            blck=[]
    lcp={}
    fd1 = open('/Users/rld1996/Desktop/clem.txt', 'w')
    for no in blcks:
        ad=blcks[no]
        lcp[no]=os.path.commonprefix(ad)


        fd1.write("Block"+str(no)+":")
        fd1.write(str(lcp[no])+"\n")
        fc=str(len(lcp[no]))+str(lcp[no])+"*"
        for t in ad:
            fc=fc+t[len(lcp[no]):]+str(len(t)-len(lcp[no]))+"$"
        fd1.write(fc+"\n")
    fd1.write("-----------------------------\n")
    for no in blcks:
        terms=blcks[no]
        fd1.write("Block" + str(no) + ":\n")
        for t in terms:
            d=dictDocListl[t]
            gap=[]
            gap.append(deltaCode(d[0]))
            fd1.write(str(d[0]) + ":" + str(gap[0])[2:] + "\n")
            for i in range(1, len(d) - 1):
                gap.append(deltaCode(d[i] - d[i - 1]))
                fd1.write(str(d[i] - d[i - 1]) + ":" + str(gap[i])[2:] + "\n")


    fd1.close()

'''



'''def frontcoding():
    dictDocL = collections.OrderedDict(sorted(dictDocList.items()))

    cd=os.path.commonprefix([dictDocL.keys()[0],dictDocL.keys()[1]])
    string,x=change(cd,0,len(dictDocL))
    fd1 = open('/Users/rld1996/Desktop/d.txt', 'w')
    fd1.write(string)
    while(x<len(dictDocL)-1):
        cad=os.path.commonprefix([dictDocL.keys()[x],dictDocL.keys()[x+1]])
        string, x = change(cd, 0, len(dictDocL))
        fd1 = open('/Users/rld1996/Desktop/d.txt', 'w')
        fd1.write(string)
    fd1.close()

def change(cd,i,l):
    dictDocL = collections.OrderedDict(sorted(dictDocList.items()))
    string=str(len(cd))+cd
    for x in range(i,l-2):
        while(os.path.commonprefix([dictDocL.keys()[x],dictDocL.keys()[x+1]]==cd)):
            string=string+str(dictDocL.keys()[x])[len(cd):]+str(len(str(dictDocL.keys()[x])[len(cd):]))
        x=l
    return string,x
'''

def extra():
    stemms=[]
    lemmms=[]
    terms = ["reynolds", "nasa", "prandtl", "flow", "pressure", "boundary", "shock"]
    for t in terms:
        x=ps.stem(t).encode('utf-8')
        stemms.append(x)
        y=wnl.lemmatize(t).encode('utf-8')
        lemmms.append(y)
    return stemms,lemmms