def superDigit(n, k):
    # Write your code here
    concatenated = False
    while not concatenated or n > 9:
        n = str(n)
        digits = [int(c) for c in n]
        n = sum(digits)
        if not concatenated:
            n *= k
            concatenated = True

    return n