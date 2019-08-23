#function to return the first n Fibonacci numbers in a list
def fibonacci(n):
#initialise with first two terms
    n1 = 0
    n2 = 1
    sequence = []
    sequence.append(n1)
    sequence.append(n2)
    for n in range(n-2):
        n3 = n1 + n2
        sequence.append(n3)
#moving along the sequence by redefining the variables
        n1 = n2
        n2 = n3
#conditional to handle the case where user inputs n < 2
    if(n > 2):
        return(sequence)
    else:
        return(sequence[0:n])

#testing the function with the required output
print("The first 6 fibonacci numbers are", fibonacci(6))
        

