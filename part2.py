"""
******
PART 2
******
Write a program that asks the user to enter a positive integer n. The program will then print the sum of the first n positive cubes.

For example, if the user types in 4, the program should print 100 (since 1^3 + 2^3 + 3^3 + 4^3 = 100).
"""
n=int(input("Enter a positive integer: ")) 
final= 0
n=n+1
for n in range (1,n):
  product= n*n*n
  final = final + product 

print(final)