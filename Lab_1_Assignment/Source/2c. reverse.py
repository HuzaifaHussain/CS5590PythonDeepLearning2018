sentence = input("Enter a sentence : ")


def reverse():
    p = sentence[::-1]  # Reversing the given sentence and storing it in 'p'
    q = p.split()
    r = []
    x = len(q) - 1  # Splitted sentence obtained then reduced it's length
    while x >= 0:
        r.append(q[x])  # putting x words into r
        x = x - 1
    y = " ".join(r)
    print('the reversed words obtained are : ', y)


reverse()
