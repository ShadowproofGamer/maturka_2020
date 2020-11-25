print("zad1.1: prawda,4,fałsz")

print("zad1.2:")
def k_podobne(n,A,B,k):
    #print(A[0:k-1:],B[n-k:n-1:],A[k:n-1:],B[0:n-k-1:],A,B)
    if k!=0:
        if A[0:k-1:] == B[n-k:n-1:] and A[k:n-1:]==B[0:n-k-1:]:
            print("k_podobne: PRAWDA")
            return 1
        else:
            print("FAŁSZ")
            return 0
    if k==0:
        if A==B:
            print("k_podobne: PRAWDA")
            return 1
        else:
            print("FAŁSZ")
            return 0

k_podobne(5,  [10, 9, 12, 10, 9],   [10, 10, 9, 9, 12], 3 )

print("zad 1.3:")

def czy_k_podobne(n, A, B):
    temp = 0
    for k in range(0,n):
        if k_podobne(n,A,B,k)==1:
            print("czy_k_podobne: PRAWDA")
            temp=1
            break
    if temp == 0:
        print("FAŁSZ")

czy_k_podobne(5,  [4, 7, 1, 4, 5], [1, 4, 5, 4, 7] )