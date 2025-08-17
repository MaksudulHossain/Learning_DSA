def selection_sort(a):
    for i in range(0, len(a)-1):
        imin = i
        for j in range(i+1, len(a)):
            if a[j] < a[imin]:
                imin = j
        a[imin], a[i] = a[i], a[imin]

def main():
    a = [10,8,6,7]
    print(a)
    selection_sort(a)
    print(a)

main()
