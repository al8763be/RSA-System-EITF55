import random


def ProbablyPrime(n, k=20):  # k is the number of rounds
    if n < 3:
        return False
    for _ in range(k):
        if not miller_rabin(n):
            return False  # composite
    return True  # primew

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
        x = (x * x) % n
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
    
    with open("prime2.txt", "r") as file:
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


def random_mode():
    found = False
    print("Random mode selected")

    while not found:
        n = random.getrandbits(512)
        if(n % 2 != 0 and n > 3):
            found = True
            print("Random number generated: ", n)
            if ProbablyPrime(n) == True:
                print("Number is prime")
            else:
                print("Number is composite")
    
   

def main():
    end = False

    while not end:
        print("For manual test mode press 1,\n"
              "for automatic test mode press 2,\n"
              "for random mode press 3,\n"
              "to exit press q: ")
        
        pick = input()
        if pick == "1":
            Mtest()
        elif pick == "2":
            Atest()
        elif pick == "3":
            random_mode()
        elif pick == "q":
            end = True
        else:
            print("Invalid option. Please try again.") 

if __name__ == "__main__":
    main()