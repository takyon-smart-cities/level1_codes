def candies(n, arr):
    result = 0

    candies_arr = [1]*n

    for x in range(1, n):
        if arr[x] > arr[x - 1]:
            candies_arr[x] = candies_arr[x - 1] + 1


    for x in range(n-2,-1,-1):
        if arr[x] > arr[x + 1] and candies_arr[x] <= candies_arr[x + 1]:
            candies_arr[x] = candies_arr[x + 1] + 1


    for j in candies_arr:
        result += j

    return result

def main():
    n = int(input())

    arr = []

    for i in range(n):
        X = int(input())
        arr.append(X)

    result = candies(n, arr)

    print(result)

if __name__ == '__main__':
    main()