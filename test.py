def findExponents():

    primes = 2
    # p,q = generate_Prime_For_RSA_Exponents(bits, primes) # Om vi vill generera random p, q primtal
    prime1 = 6938168183909476011711423782569145937582334327321712545715885438989823478711798510227258253737276814067807836904995661948940619120070366127008027527066103
    prime2 = 6799567461568200705908991986699895231497109379651706284696168519150076160951283987365163549611749850876280551858508087641524105908392504380214123161150113
    m = (prime1-1) * (prime2-1)
    # Om vi vill ha random värde på e av dessa tal
    # randomValue = [3,5,7, 2**16+1]
    # e = random.choice(randomValue)
    #Bestämt E
    e = 2**16+1

    d = extended_euclidean_with_inverse_mod(m, e)
    print("e value")
    print(e)
    print("m value")
    print(m)
    print("d value")
    print(d)
    return e, m, d

def extended_euclidean_with_inverse_mod(m, a):
    #Find numbers u,v,d such that d=gcd(a,m)=m x u + a x v

    d1 = m
    d2 = a
    v1 = 0
    v2 = 1

    while (d2 != 0):
        q = d1 // d2
        t2 = v1 - q*v2
        t3 = d1 - q*d2
        v1 = v2; d1 = d2
        v2 = t2; d2 = t3

    v=v1
    d=d1

    if d != 1:
        return None
    else:
        return v % m    # Göra v positivt enligt a × v ≡ a × (v + m) ≡ a × v + 0 (mod m) ≡ 1 (mod m)
                        # Thus we can always find a positive solution in the range 0 < v < m, to our problem

findExponents()