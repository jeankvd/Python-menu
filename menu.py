#Jean Villalobos
#Programming; Menu/Driven Program
#This Program prompts the user to select a program
#Then runs that program


#First define all the functions & modules

def celsiusToFarenheit():
    print "This is a Celsius to Farenheit Converter"
    celsius = int(raw_input("Please enter Celsius: "))
    farenheit = (((float(5)/9)*celsius) + 32) #formula
    print"The temperature in Farenheit is %s Farenheit." % farenheit

def paintJobEstimate():

    labor = 20.00 #constant

    print "This programs estimates the cost of a paint job."
    sqFeet = int(raw_input("Enter the square feet to be painted: "))

    while sqFeet < 1:
        print "Sorry, that input is invalid"
        sqFeet = int(raw_input("Enter the square feet to be painted: "))

    gallonsCost = int(raw_input("Enter price of the paint per gallon: "))
    while gallonsCost < 1:
        print "Sorry, that iinput is invalid"
        gallonsCost = int(raw_input("Enter price of the paint per gallon: "))


    gallons = float(sqFeet) / 115   #1 gallon per 115 sqft
    laborHours = (float(sqFeet) / 115) * 8 #8hours per 115sqft

    paintCost = gallons * gallonsCost
    laborCost = laborHours * labor 
    
    #calculate costs multiply price * requisite

    totalCost = paintCost + laborCost

    print ""

    print "You are gonna need %s gallons." % gallons
    print "The workers have to work %s hours." % laborHours
    print "The total cost for gallons of paints is %s ." % paintCost
    print "The total cost for labor is %s ." % laborCost
    print "Finally, the total cost for the paint job is %s" % totalCost

def softwareDiscount():

    print "This program gives you a discont",
    print "according to the number of packages you buy"
    print ""

    packages = int(raw_input("Enter how many packages are you buying: "))
    while packages < 1:
        print "Sorry, that inut is invalid."
        packages = int(raw_input("Enter how many packages are you buying: "))

    discount = 0 #define

    if packages >= 100:
        total = (packages * 99) - ((packages * 99) * .5)
        discount = 50
                # if & elif statements starting from high to loe
    elif packages >= 50:
        total = (packages * 99) - ((packages * 99) * 0.4)
        discount = 40

    elif packages >=  20:
        total = (packages * 99) - ((packages * 99) * .3)
        discount = 30
        #packages - packages discount
    elif packages >= 10:
        total = (packages * 99) - ((packages * 99) * .2)
        discount = 20

    else:
        total = packages * 99

    print ""

    if discount == 0:
        print "You got no discount."
    else:
        print "You got %d percent off!" % discount

    print "Your total is %s" % total

def penniesForDays(days):
    
    pennies = 0

    while days > 0: #precheck loop

        if pennies == 0:
                pennies = 1
        else:
            pennies = pennies * 2

        days -= 1           #counter

    dollars = float(pennies) / 100  #float to make the 
    return dollars      #division a non integer

def is_prime(number):
    
    if number == 3:
        print"This number is a prime number!"   
    else:       #I figured out that if a number other than 3
                #is divisible by 2 or 3 then it is not a prime number
        if number % 2 == 0 or number % 3 == 0:
            print "This number is not a prime number"
        else:
            print "This number is a prime number!"

def speedingCalculator():
    speedLimit = int(raw_input("Please enter the speed limit: "))
    
    #If the speed limit is not within range
    #enter the while loop until speed limit is on range

    while speedLimit == speedLimit < 20 or speedLimit > 70:
        print ""
        print "Sorry, the speed limit is invalid"
        print "Please try again"
        speedLimit = int(raw_input("Please enter the speed limit: "))

    driverSpeed = int(raw_input("Please enter the driver's speed: "))

    #While the driver's speed is not over the limit
    #enter loop until otherwise

    while driverSpeed <= speedLimit:
        print ""
        print "The driver's speed must be higher than the speed limit"
        driverSpeed = int(raw_input("Please enter the driver's speed: "))
    
    #After passsing both validation tests
    #driverSpeed - speedLimit
    #return & print result 
    print ""
    result = driverSpeed - speedLimit
    

    if result == 1:
        print "The driver was over the speed limit by %s mile per hour" % result
    else:
        print "The driver was over the speed limit by %s miles per hour" % result


def driverExam():
    incorrectAnswers = []
    
    Answers = ["B", "D", "A", "A", "C", "A", "B", "A", "C",  
        "D", "B", "C", "D", "A", "D", "C", "C", "B", "D", "A"]

    print "You are about to take a Driver's License Exam."
    print "Please enter your answers for the number that is prompted."
    count = 0
    correct = 0     #Counters
    incorrect = 0

    for index in range(len(Answers)):
       
        print count + 1, #Coma to follow line on next code
        answer = raw_input(" ") 
        count += 1

        if answer.upper() == Answers[index]:    #add correct or incorrect
            correct += 1                        #to respective counter
        else:
            incorrect += 1
            incorrectAnswers.append(index + 1)

        print ""                                #for neatness

    if correct >= 15:
        print "Congrats! You passed the Exam!"
    else:                                       #inform the user of their status
        print "Sorry you got %s answers incorrect" % incorrect
        print "You failed the exam"

    print "These are the answers you got incorrect"
    print incorrectAnswers

def readFile():
    numbers = open('numbers.dat', 'r')
    line= numbers.read()

    for number in line:
        int(number)
        result += number
    return result
    numbers.close()

def backwardString():
    print "This program reverses any word that you enter!"

    word = raw_input("Enter the word you want to see backwards: ")
    new_Word = ""

    for character in word:
    
        new_Word = character + new_Word

    print new_Word

def threeInstances():
    class Info:  #class defined


        def __init__(self, name, adress, age, phoneNumber): 
            self.__name = name          #initialize the data holded by the class
            self.__adress = adress
            self.__age = 0
            self.__phoneNumber = 0

        def set_name(self, name):           #start mutator methods
            self.__name = name

        def set_adress(self, yrMod):
            self.__adress = adress

        def set_age(self, age):                 
            self.__age = 0

        def set_phoneNumber(self, phoneNumber):     #end mutator methods
            self.__phoneNumber = 0





        def get_name(self):     #start accesor methods
            return self.__name

        def get_adress(self):
            return self.__adress
                                     
        def get_age(self):
            return self.__age

        def get_phoneNumber(self):
            return self.__phoneNumber   #end accesor methods


    #Create instances of this class =

    myInfo=Info("Jean", "2402 50th Terr SW Apt B", 17, 2392002373)
    friendInfo = Info("Kat", "3808 Gazebo Place", 18, 8653145645)
    momInfo = Info ("Emy", "2333 55th ter SW", 38, 2398108263)



def menu():

    print "1. Celsius Converter"
    print "2. Paint Job Calculator"
    print "3. Software Sales"
    print "4. Pennies for Pay"
    print "5. Prime Numbers"
    print "6. Speeding Calculator"
    print "7. Driver's License Exam"
    print "8. Numbers addition (requires numbers.dat)"
    print "9. Backward String"
    print "10. Personal Information (class creation- no output)"

    print ""

    menu_selection = int(raw_input("Please enter your selection: "))
    print ""

    if menu_selection < 1 or menu_selection > 10:
        print "That is an invalid selection"
        menu_selection = int(raw_input("Please enter your selection: "))

    if menu_selection == 1:
        celsiusToFarenheit()
        menu()
        

    elif menu_selection == 2:
        paintJobEstimate()
        menu()
        
    elif menu_selection == 3:
        softwareDiscount()
        menu()
        

    elif menu_selection == 4:
        print "This is a program that doubles the amount of pennies you",
        print "earn each day." 
        print "You start with one penny"
        print ""
        days = int(raw_input("Enter how many days will you calculate for: "))
        print "You would have %s dollars" % penniesForDays(days)
        menu()
        
    elif menu_selection == 5:
        print "This programs verifies if a number is a prime number."
        print ""
        prime = int(raw_input("Please enter a number: "))
        print is_prime(prime)
        menu()

    elif menu_selection == 6:
        speedingCalculator()
        menu()



    elif menu_selection == 7:
        driverExam()
        menu()
        

    elif menu_selection == 8:
        readFile()
        menu()

    elif menu_selection == 9:
        backwardString()
        menu()

    elif menu_selection == 10:
        threeInstances()
        menu()


menu()
