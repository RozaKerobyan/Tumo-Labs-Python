def find_pythgorean_triples(diff, low, high):
    triples = []

    for a in range(low, high + 1):
        if (a ** 2 - diff ** 2) % (2 * diff) == 0:  
            b = (a ** 2 - diff ** 2) // (2 * diff)
            c = b + diff
            if b > a and c > b:
                triples.append((a,b,c))
    return triples

# Test 
print(find_pythgorean_triples(1,2,10))
print(find_pythgorean_triples(3,10,25))
print(find_pythgorean_triples(4,100,100))
print(find_pythgorean_triples(10,91,99))
