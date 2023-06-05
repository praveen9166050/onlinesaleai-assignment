def compute(n):
    if n < 10:
        out = n ** 2
    # Changes '<' with '<=' to include 20 here as well
    elif n <= 20:
        out = 1
        # Added 1 to the upper limit of range to make the value of i reach n-10
        for i in range(1, n-10+1):
            out *= i
    else:
        lim = n - 20
        out = lim * lim
        # Changed '-' with '+' as the formula for sum to n natural number is n(n+1)/2
        out = out + lim
        # Changed '/' with '//' to produce an integer output
        out = out // 2 
    print(out)

compute(20)