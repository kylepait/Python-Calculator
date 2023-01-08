#loop control variable
powerOff = False
#ask for operator
while powerOff == False:
    print("|**********************|")
    print("|** Enter your Choice *|")
    print("|**********************|")
    print("| 1|      ADD (+)      |")
    print("| 2|    SUBTRACT (-)   |")
    print("| 3|    MULTIPLY (*)   |")
    print("| 4|     DIVIDE(/)     |")
    print("|**********************|")
    #print(type(nums))
    #ask for operator
    operator = int(input("Please enter your choice (1/2/3/4): "))
    #if addition is picked
    if operator == 1:
        #how many numbers that will be input
        amount = int(input("How many numbers will you input?: "))

        #list for numbers
        nums = []

        #add each input to the list
        for x in range(amount):
            userInput = int(input("Enter number: "))
            nums.append(userInput)

        #find the sum and print
        sum_nums = sum(nums)
        print("The sum of the given list is ", sum_nums)

        #prompt for another round or to end
        another = str(input("Would you like to caclulate another one? (yes,no): "))

        #if user is finished
        if another == 'no':
            powerOff = True
    
    #if subtraction if pickd

    elif operator == 2:

        #same as before
        amount = int(input("How many numbers will you input?: "))
        nums = []
        for x in range(amount):
            userInput = int(input("Enter number: "))
            nums.append(userInput)

        #variable to hold the answer
        sub_nums = nums[0]

        #subtract each num
        for x in range(1, len(nums)):
            sub_nums = sub_nums - nums[x]

        #print answer
        print("The subtraction of all numbers is ", sub_nums)

        #same as before
        another = str(input("Would you like to caclulate another one? (yes,no): "))
        if another == 'no':
            powerOff = True

    elif operator == 3:
        #same as before
        amount = int(input("How many numbers will you input?: "))
        nums = []

        for x in range(amount):
            userInput = int(input("Enter number: "))
            nums.append(userInput)

        #variable to hold the answer
        multi_nums = nums[0]

        #multiply each num
        for x in range(1, len(nums)):
            multi_nums = multi_nums * nums[x]

        #print answer
        print("The multiplication of all numbers is ", multi_nums)

        #same as before
        another = str(input("Would you like to caclulate another one? (yes,no): "))
        if another == 'no':
            powerOff = True

    elif operator == 4:
        #same as before
        amount = int(input("How many numbers will you input?: "))
        nums = []

        for x in range(amount):
            userInput = int(input("Enter number: "))
            nums.append(userInput)
        #variable to hold the answer
        div_nums = nums[0]

        #multiply each num
        for x in range(1, len(nums)):
            div_nums = div_nums / nums[x]

        #print answer
        print("The division of all numbers is ", div_nums)
        
        #same as before
        another = str(input("Would you like to caclulate another one? (yes,no): "))
        if another == 'no':
            powerOff = True