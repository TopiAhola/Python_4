def permutations(data, n=0):
    print(n, ":", data)

    # jos vain 1 kirjain, palauttaa yhden kirjaimen muuten palauttaa arrayn rekursion kautta -> rekursio jatkuu
    if n == len(data)-1:
        return data



                           #tai vain data kun n+1 == len(data)
    return [pattern + c for pattern in permutations(data, n+1) for c in data]


#main
if __name__ == '__main__':
    #print( permutations('123', 2 ) )

    #print(permutations('123', 1))

    #print(permutations('123', 0))

    print(permutations('123'))