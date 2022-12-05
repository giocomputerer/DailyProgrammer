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
            print("the word with lettersum 319 is :",word)
        if(wordc%2==1):
            oddn+=1

    print("\n number of oddnumbered lettersum words is:",oddn)

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

    liset=["aba","asw"]
    bpliset=[1,2]

    for key in sorted(ldi.keys()):
        flag=False
        if type(ldi[key][0]) is str:
            liset.append(sorted(ldi[key], key=len,reverse=True)[0])
        else:
            liset.append(ldi[key])
        for f in sorted(ldi.keys()):
            if (f>key):
                for k in sorted(ldi[f], key=len,reverse=True):
                    if(len(k)<len(liset[(len(liset)-1)])):
                        liset.append(k)
                        flag=True
                        break
        if(len(liset)>len(bpliset)):
            bpliset=liset
        liset=[]


    print("extra 6 list:",bpliset)

    frequenter=mode(lettersums)
    print ("\nmost frequent lettersum words:")
    print (ldi[frequenter])