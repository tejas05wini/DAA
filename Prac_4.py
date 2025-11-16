#Write a program to generate binomial coefficients using dynamic programming. 

def binomial(n,k):
    C =[[0 for i in range(k+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(min(k,i)+1):
            if j==0 or j==i:
                C[i][j]=1
            else:
                C[i][j]= C[i-1][j-1] + C[i-1][j]
    return C[n][k]

n = int(input("enter n : "))
k = int(input("enter k : "))
print(f"Binomial coefficient of C({n},{k}) is : {binomial(n,k)}")
