available=5
requested=int(input("Enter the number of candies you want"))
i=1
if requested<=available:
    print("Please wait for your candies")
    while i<=requested:
        print("Candy")
        i=i+1
else:
    while i<=available:
        print("Candy")
        i = i + 1
    print("Sorry, only",available, "candies are available")
print("Available candies:",available,"& requested candies:",requested)



