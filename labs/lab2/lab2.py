import math

#  RMS
n = eval(input("Enter the values to be entered: "))
sum1 = 0
harmonic = 0
geometric = 1
for _ in range(n):
    value = (eval(input("Enter value: ")))
    sum1 = sum1 + (value**2)
    harmonic = harmonic + (1 / value)
    geometric = geometric * (value)

# RMS cont
final_rms = math.sqrt(sum1/n)
final_harmonic = n / harmonic
final_geometric = (geometric ** (1/n))

# RMS cont
print("The RMS average is: ", round(final_rms, 3))
print("The Harmonic mean is: ", round(final_harmonic, 3))
print("The Geometric mean is: ", round(final_geometric, 3))


#  Harmonic Mean






