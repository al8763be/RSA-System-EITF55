
import random


def euklid(a,m):
    u1, u2, v1, v2, d1, d2 = 1, 0, 0, 1, m, a
  

    while d2 != 0:
        q = d1 // d2
        t1 = u1 - q * u2
        t2 = v1 - q * v2
        t3 = d1 - q * d2
        u1, v1, d1= u2, v2, d2
        u2, v2, d2= t1, t2, t3
    
    u, v, d = u1, v1, d1
    
   
    print("u1: ", u)
    print("v1: ", v)
    print("d: ", d)

    return u, v, d

def inverse(a, m):
    v1,v2,d1,d2 = 0,1,m,a

    while d2 != 0:
        q = d1 // d2
        t2 = v1 - q * v2
        t3 = d1 - q * d2
        v1, d1= v2, d2
        v2, d2= t2, t3
    
    v, d = v1, d1

    # d = gcd(a,m) != 1 means that there is no inverse
    if d != 1:
        return -1
    
    #if v is negative, add m to it
    if v < 0:
        v += m

    return v,d

def test():
    #Test case from Example 2
    euklid(21, 93)

    #Test case using random numbers
    for _ in range(5):
        a = random.randrange(2**511, 2**512)
        m = random.randrange(2**511, 2**512)
        
        result = inverse(a, m)
        
        print(f'a: {a}\nm: {m}\nresult: {result}\n')

    #Test case for C.2
    print("Testcase for C.2")
    prime1 = 6938168183909476011711423782569145937582334327321712545715885438989823478711798510227258253737276814067807836904995661948940619120070366127008027527066103
    prime2 = 6799567461568200705908991986699895231497109379651706284696168519150076160951283987365163549611749850876280551858508087641524105908392504380214123161150113
    print(f"\nresult for prime 1: {inverse(pow(2,16) + 1, prime1)}\n")
    print(f"\nresult for prime 2: {inverse(pow(2,16) + 1, prime2)}\n")
