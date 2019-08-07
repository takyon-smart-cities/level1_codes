#https://www.hackerrank.com/challenges/dynamic-array/problem

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    seqList = [[] for i in range(n)]
    lastAnswer = 0
    
    for query in queries:
        qtype    = query[0]
        seqIndex = (query[1] ^ lastAnswer) % n
        seq      = seqList[seqIndex]
        y        = query[2]



        if qtype == 1 :
            seqList[seqIndex].append(y)
        else :
            lastAnswer = seq[y % len(seq)]

            print(lastAnswer)



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n,queries)
