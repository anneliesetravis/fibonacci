#writing a function to return either the first n terms
#of the fibonacci sequence (excluding 0 to solve /0 error)
#or return the ratio between the last two terms of the sequence
def goldenratio_sequence(n,term = False):
    n1 = 0
    n2 = 1
    sequence = []
    ratio_sequence = []
    sequence.append(n1)
    sequence.append(n2)
    ratio = 1
    for n in range(n):
        n3 = n1 + n2
        sequence.append(n3)
        n1 = n2
        n2 = n3
        ratio = n2/n1
        ratio_sequence.append(ratio)
    if term == True:
        return(ratio)
    else:
        return(ratio_sequence[0:n])

#writing a function to return the minimum fibonacci numbers required to
#calculate a suitable approximation of the golden ratio, subject to
#the tolerance and maximum generated number arguments
def find_minimum_fibonacci_numbers(tolerance=0.0000000001, maxnum=100):
#initialise by defining variables
    golden_ratio = 1.6180339887498948
    n = 1
    ratio = goldenratio_sequence(n, True)
    phi = abs(ratio - golden_ratio)
#while calculated approximation - actual value is greater than the tolerance,
#and the number of terms generated does not exceed the maximum, this loop will
#continue
    while phi >= tolerance and n < maxnum:
        ratio = goldenratio_sequence(n,True)
        phi = abs(ratio - golden_ratio)
#returning the desired values
        n = n + 1
    return(n, ratio)
  
#testing my code with the required outputs
print("The ratios between the first 20 fibonacci numbers are:")
print(goldenratio_sequence(20))
print("\n")
print("Minimum terms for a suitable golden ratio approximation & calculated ratio:")
print("Tolerance of 10^-10:", find_minimum_fibonacci_numbers(10**(-10)))
print("Tolerance of 10^-14:",find_minimum_fibonacci_numbers(10**(-14)))
print("Tolerance of 10^-18:",find_minimum_fibonacci_numbers(10**(-18)))
