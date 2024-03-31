def test(tmp, N):
    return ((1 + tmp) * tmp) // 2 >= N

def search(N):
    l = 1
    r = 10_000_000_000
    mid = 0
    
    while l < r:
        mid = (l + r) // 2
        
        if test(mid, N):
            r = mid
        else:
            l = mid + 1
            
    return r - 1

def main():
    N = int(input())
    
    diag = search(N) + 1 
    
    if diag % 2 == 0:
        tmp = ((diag) * (diag - 1)) // 2
        N -= tmp
        
        print(f"{diag - N + 1}/{N}")
        
    else:
        tmp = ((diag) * (diag - 1)) // 2 
        N -= tmp          
        print(f"{N}/{diag - N + 1}")

if __name__ == "__main__":
    main()
