# Collaborators: 
# https://www.tutorialspoint.com/python-program-to-print-all-the-numbers-divisible-by-3-and-5-for-a-given-number

for x in range(2, 51):
    if x%3==0:
        print(f"{x} is divisible by 3")
    else:
        print (f"{x} is not divisible by 3")
