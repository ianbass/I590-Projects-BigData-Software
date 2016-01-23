import sys

def fizzbuzz(n):

    output1 = "FizzBuzz"
    output2 = "Fizz"
    output3 = "Buzz"

    for i in xrange(1, n+1):
        if i%6 == 0:
            print output1
        elif i%2 == 0:
            print output2
        elif i%3 == 0:
            print output3
        else:
            print i
    i +=1

if __name__ == '__main__':
    n = int(sys.argv[1])
    fizzbuzz(n)
