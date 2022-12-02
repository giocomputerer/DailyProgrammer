from statistics import mode

def lettersum(word):
    sum=0
    for i in word:
        sum+=ord(i)-96
    return(sum)


if __name__ == '__main__':

    with open('enable1.txt','r') as file:
        Lines=file.readlines()


    oddn=0
    lettersums=[]
    ldi = dict()

    for line in Lines:
        word=line.rstrip()
        wordc=lettersum(word)
        lettersums.append(wordc)
        if wordc in ldi.keys():
            ldi[wordc].append(word)
            pass
        else:
            ldi[wordc]=list((word,))
        if(wordc==319):
            print(word)
        if(wordc%2==1):
            oddn+=1

    for key in ldi.keys():
        for i in range(0,len(ldi[key])):
            for f in range(i,len(ldi[key])):
                if (abs(len(ldi[key][i])-len(ldi[key][f]))==11):
                    print("diff 11 ones")
                    print(ldi[key][i])
                    print(ldi[key][f])
                if (len(set(ldi[key][i]).intersection(ldi[key][f]))==0 and key > 187):
                    print("unsames")
                    print(ldi[key][i])
                    print(ldi[key][f])

    liset=[]
    bpliset=[]

    for key in sorted(ldi.keys()):
        liset.append(sorted(ldi[key][0], key=len,reverse=True))
        for f in sorted(ldi.keys()):
            if (f>key):
                for k in sorted(ldi[f], key=len,reverse=True):
                    if(len(k)<len(liset[(len(liset)-1)])):
                        liset.append(k)
                        print(k)
        if(len(liset)>len(bpliset)):
            bpliset=liset
    print("======================")
    print(bpliset)
    print("======================")

    frequenter=mode(lettersums)
    frequentercount=0
    for line in Lines:
        word=line.rstrip()
        if(lettersum(word)==frequenter):
            print(word, end=' : ')
            frequentercount+=1
    print()
    print(frequentercount)
    print(oddn)