import random
import timeit


def ProbablyPrime(n, k=20):  # k is the number of rounds
    if n < 3:
        return False
    for _ in range(k):
        if not miller_rabin(n):
            return False  # composite
    return True  # primew

def miller_rabin_recompute(n):
    s = n - 1
    r = 0

    while s % 2 == 0:
        s = s // 2
        r += 1
    
    a = random.randint(2, n - 2)
    x = pow(a,s,n)
    if x == 1 or x == n - 1:
        return True # n is prime
    
    for i in range(1, r): # r - 1 give 5 is composite
        x = pow(a, (2 ** i) * s, n)
        if x == 1:
            return False # n is composite
        if x == n - 1:
            return True # n is prime
        
    return False # n is composite

def miller_rabin(n):
    s = n - 1
    r = 0

    while s % 2 == 0:
        s = s // 2
        r += 1
    
    a = random.randint(2, n - 2)
    x = pow(a,s,n)
    if x == 1 or x == n - 1:
        return True # n is prime
    
    for i in range(1, r): # r - 1 give 5 is composite
        #x = pow(a, (2 ** i) * s, n)
        x = pow(x, 2, n)
        if x == 1:
            return False # n is composite
        if x == n - 1:
            return True # n is prime
        
    return False # n is composite

def Mtest():
    print("\n")
    print("Test mode selectecd")
    print("Enter a number to test if it is prime: ")
    found = False
    while not found:
        n = int(input())
        if(n % 2 != 0 and n > 3):
            found = True
            print ("Number entered: ", n)
            if ProbablyPrime(n) == True:
                print("Number is prime")
            else:
                print("Number is composite")
        else:
            print("Invalid number. Please enter an odd number greater than 3.")

def Atest():
    print("Automatic test mode selected")
    
    with open("prime.txt", "r") as file:
        for line in file:
            parts = line.split()
            for part in parts:
                n = int(part)
                print("Number entered:", n)
                # Test the number's primality right away
                if ProbablyPrime(n):
                    print("Number is prime")
                else:
                    print("Number is composite")


def comp_test():
    print ("Computational time test mode selected")


    # number to test, currently the biggest one from primeXL
    n = 15485863

    #Number is how many times we want to run the test
    recompute_time = timeit.timeit(lambda: miller_rabin_recompute(n), number=100000)
    iterative_time = timeit.timeit(lambda: miller_rabin(n), number=100000)

   
    print("Iterative squaring average time:", iterative_time / 100000, "seconds per run")
    print("Recomputing exponent average time:", recompute_time / 100000, "seconds per run")
    print("Time difference:", (iterative_time / 100000) - (recompute_time / 100000), "seconds")
    
    print("\n")

def generate_with_time():
    print("Generate primes seleceted, pick bits: 512, 1024, 2048, 4096")
    
    bits = int(input())
    count = 0
    primes = []

    start = timeit.default_timer()
    while count < 100:
        
        n = random.randrange(2**(bits-1), 2**bits)
        if ProbablyPrime(n):
            count += 1
            print(count)
            primes.append(n)
    end = timeit.default_timer()

    f = open(str(bits) + ".txt", "a")
    for prime in primes:
        f.write(str(prime) + "\n")
    f.close()


    print("Time taken to generate 100 primes:", end - start, "seconds")
    print("\n")


def main():
    end = False

    while not end:
        print("For manual test mode press 1,\n"
            "For automatic test mode press 2,\n"
            "For computational time test press 3,\n"
            "For generating primes press 4,\n"
            "To exit press q: ")
        
        pick = input()
        if pick == "1":
            Mtest()
        elif pick == "2":
            Atest()
        elif pick == "3":
            comp_test()
        elif pick == "4":
            generate_with_time()
        elif pick == "q":
            end = True
        else:
            print("Invalid option. Please try again.") 

if __name__ == "__main__":
    main()