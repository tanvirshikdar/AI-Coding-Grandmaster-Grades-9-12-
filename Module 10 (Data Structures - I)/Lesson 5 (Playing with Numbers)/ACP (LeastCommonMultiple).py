def hcf(numberSmallest,numberLargest): 
  while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore
  return numberLargest

numberLargest = int(input("Enter Largest number : "))
numberSmallest = int(input("Enter Smallest number : "))

lcm = int((numberSmallest / hcf(numberSmallest,numberLargest))* numberLargest)
print("LCM is : ",lcm)