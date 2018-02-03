def find_triplets(p, q):            #making a function
    Num = True
    for i in range(0, q - 2):       #Using for loop in i from o to q-2

        for j in range(i + 1, q - 1):   #using j in earlier loop i

            for k in range(j + 1, q):   #using k in earlier loop j

                if (arr[i] + arr[j] + arr[k] == 0):     #if the sum of 3 digits in a list becomes zero
                    print(arr[i], arr[j], arr[k])

number = input('the list of numbers to be entered:')
arr = list(map(int, number.split()))            #mapping those numbers with list and storing it in array
q = len(arr)
find_triplets(arr, q)