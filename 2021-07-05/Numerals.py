class numeral:

    def __init__(self,num):
        self.value=num
        self.dict={ord('I'):'a',ord('V'):'b',ord('X'):'c',ord('L'):'d',ord('C'):'e',ord('D'):'f',ord('M'):'g'}
    def __lt__(self, other):
        if(self.value.translate(self.dict)<other.value.translate(self.dict)):
            return (True)
        else:
            return (False)

    def __str__(self):
        return (self.value.translate(self.dict))

def numcompare(num1,num2):
    pass


if __name__ == '__main__':
    print("enter first:",end='')
    in1=numeral(input())
    print("enter second:", end='')
    in2 = numeral(input())

    print(in1<in2)
