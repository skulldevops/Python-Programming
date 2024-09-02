# This is "Smoothie Commands" a weird terminal experience. First I add my names list so users can select their preferred person when they log onto the console
name_list = ["Rose, Elon"]
name = "Rose"
age = 22
# I add only 2 users, for example Myself, and Elon Musk, he's not as important as me right now
# I start with a simple print of the name and age oonce the user logs onto the console and the second print line is a nice Greeting, the name oof the user and verification
print (name, age)
print ("Welcome,", name, ",in order to continue you must type a number below to verify yourself...")
# For the verification, I use a simnple equation soo that when a user types any number, that number is multiplied by 12, that number will be our verification code
number = input("Type any number to get a generated verification code, you'll have to remember your code for later>>>>")
try:
    print("Your code is:", 12 * int(number))
    number = input("Enter your code>>>")
# I make sure that the user can only attempt to enter a number 2 times before being locked out of the console and they have to restart the process
# After the number is entered, the number will multiply by 12
except:
    print("That is not a number...")
    number = input("*1 attempt left*, Enter a number>>>")
    print("Your code is:", 12 * int(number))
    number = input ("Type your code here, do not share>>>")
    # Now if the user didn't enter a number, they will get a warning they'll have too try again later
    print("That is not a number...Try again later")

# Now if the number was entered correctly, they will continue to the Smoothie console

print("Success!")

# This is where I add a greeting to the user logged onto the console, Rose or Elon

print("Wecome to ManiText!")
print("Today, in this enviorment, we're going to be making a delicious smoothie for the user!")
# This displays the name list of all users, the users names are keywoords in oordr to continue
print ("Users - ", name_list)
print ("To exit, enter any key")
# I tell them to enter a user's name below, and the game will continue, after the user types the ingridients, the console will ask to blend it
while True:
    user_input = input("Start Typing a name to make a smoothie for that person>>>")
    if user_input == "Elon":
        print("Let's Begin! Stary by picking a fruit for the smoothie!")
        print("Pick from list below")
        print("Banana")
        print("Apple")
        print("Orange")
        print("Peach")
        print("Grapes")
        input(">>>")
        print("Okay! Now, let's add 1 more fruit to our smoothie!")
        print("Pick from list below")
        print("Banana")
        print("Apple")
        print("Orange")
        print("Peach")
        print("Grapes")
        input(">>>")
        print("Okay! Now, let's add milk our smoothie!")
        print("Pick from list below")
        print("1 Cup - Dairy Milk")
        print("1 Cup - Oat Milk")
        input(">>>")
        print("Okay! Now, let's blend our smoothie! It'll take a little while...ok?")
        # The user types "ok"
        input(">>>")
        print(">>>Blend?<<<")
        # The user types "yes"
        input(">>>")
        #The console coounts down while the smoothie blends
        print("3...")
        print("2...")
        print("1...")
        print("Done!")
        print ("The smoothie is done! Thanks for playing and enjoy your smoothie!")
        #And once the smooothie is complete, the console shuts down
        break
        
        # This is for the second User, same rules and same inputs
    elif user_input == "Rose":
        print("Let's Begin! Stary by picking a fruit for the smoothie!")
        print("Pick from list below")
        print("Banana")
        print("Apple")
        print("Orange")
        print("Peach")
        print("Grapes")
        input(">>>")
        print("Okay! Now, let's add 1 more fruit to our smoothie!")
        print("Pick from list below")
        print("Banana")
        print("Apple")
        print("Orange")
        print("Peach")
        print("Grapes")
        input(">>>")
        print("Okay! Now, let's add milk to our smoothie!")
        print("Pick from list below")
        print("1 Cup - Dairy Milk")
        print("1 Cup - Oat Milk")
        input(">>>")
        print("Okay! Now, let's blend our smoothie! It'll take a little while...ok?")
        input(">>>")
        print(">>>Blend?<<<")
        input(">>>")
        print("3...")
        print("2...")
        print("1...")
        print("Done!")
        print ("The smoothie is done! Thanks for playing and enjoy your smoothie!")
        #And once the smooothie is complete, the console shuts down
        break
        
        #If the user refuses to enters anything but keywords: "Rose" or, "Elon", the console will ask to shut down
    else:
        print ("Are you sure you want to exit?")
        user_input == input(">>>")
        # If the user types yes, Smoothie will shut down
        if user_input == "yes":
            break
        
        print ("Goodbye")
        break
