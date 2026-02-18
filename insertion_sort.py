def insertionSort(arr):
    for i in range(1, len(arr)):
        pos = i
        # 一つずつ戻って、該当する配列の数値が小さいものがあればswapするを繰り返す
        while pos > 0 and arr[pos - 1] > arr[pos]:
            arr[pos], arr[pos - 1] = arr[pos - 1], arr[pos]
            pos -= 1
    return arr
messy = [4, 2, 5, 1, 3, 9, 10]
print(insertionSort(messy))
#    - Best Case:    O(n) : already sorted; inner while loop runs once per element
#    - Average Case: O(n^2)
#    - Worst Case:   O(n^2)z