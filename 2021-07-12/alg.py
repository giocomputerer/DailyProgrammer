def importmatrix(filename):
    matrix=[]
    with open(filename,'r') as f:
        for i in f.readlines():
            matrix.append(i.rstrip().split(' '))

    return (matrix)

if __name__ == '__main__':
    matrix=importmatrix("matrix-sum-20.txt")
    for i in matrix:
        print(i)
    ave,suma,count=0,0,0
    for i in matrix:
        for j in i:
            suma+=int(j)
            count+=1
    ave=suma/count

    print("============================================================")

    matrixset=[]
    for i in matrix:
        templ=[]
        for j in i:
            templ.append(int(int(ave)-int(j)))
        matrixset.append(templ)

    for i in matrixset:
        print(i)

    finalset=[]

    for i in range(0,len(matrixset)):
        templ=[]
        for j in range(0,len(matrixset[0])):
            cur=matrixset[i][j]
            for k in range(0,len(matrixset)):
                if(k !=i):
                    cur -= matrixset[k][j]
            for p in range(0,len(matrixset[i])):
                if(p != j):
                    cur -= matrixset[i][p]
            templ.append([cur,True])
        finalset.append(templ)

    print("==============================================")

    chosen=[]

    for i in finalset:
        print(i)

    print("==============================================")

    for i in range(0,20):
        maxi=-9999999999999999
        maxij=0
        maxik=0
        for j in range(0,len(finalset)):
            for k in range (0,len(finalset[0])):
                if(maxi<finalset[j][k][0] and finalset[j][k][1]):
                    maxi=finalset[j][k][0]
                    maxij=j
                    maxik=k
        for j in range(0,len(finalset)):
            for k in range (0,len(finalset[0])):
                if(j==maxij or k==maxik):
                    finalset[j][k][1]=False

        for i in finalset:
            print(i)
        print("/////////////////////////////////////////////////////////////////////")

        chosen.append([maxi,maxij,maxik])

    print (chosen)
    fsum=0
    for i in chosen:
        i1=i[1]
        i2=i[2]
        print (matrix[i1][i2])
        fsum += int(matrix[i1][i2])

    print("final answer:",fsum)
