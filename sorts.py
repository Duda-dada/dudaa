
def bubble_sort(B):
    N = len(B)
    unordered = True
    while unordered:
        unordered = False
        for j in range(N-1):
            if B[j]>B[j+1]:
                B[j], B[j+1] = B[j+1], B[j]
                unordered = True
        N-=1
    return B



def selection_sort(B):
    for j in range(len(B) - 1):
        jmin = j
        for e in range(j + 1, len(B)):
            if B[e] < B[jmin]:
                jmin = e
        B[j], B[jmin] = B[jmin], B[j]
        return B

def insertion_sort(B):
    for j in range(1, len(B)):
        tmp = B[j]
        e=j-1
        while e>=0 and B[e]>tmp:
            B[e+1]=B[e]
            e-=1
        B[e+1]=tmp
    return B




