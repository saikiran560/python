def find_common_factors(a, b):
    common_factors = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            common_factors.append(i)
    return common_factors

a = 50
b = 60

common_factors = find_common_factors(a, b)

print(f"Common factors of {a} and {b}: {common_factors}")
