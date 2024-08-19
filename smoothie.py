name_list = ["Rose, Elon"]
name = "Rose"
age = 22
name = "Elon"
age = 53

print (name, age)
print ("Welcome,", name, ",in order to continue you must type a number below to verify yourself...")

number = input("Type any number to get a generated verification code, you'll have to remember your code for later>>>>")
try:
    print(12 * int(number))
except:
    print("That is not a number...")

number = input ("Type your pin here, do not share>>>")
try:
    print(number, "Success!")
except:
    input(number,"The verification has failed, try again below...")

print("Wecome to ManiText!")
print("Today, in this enviorment, we're going to be making a delicious smoothie for the user!")

i = 0

while i <1:
    i = i + 1
    print (i)
    print (name_list)

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
        input(">>>")
        print(">>>Blend?<<<")
        input(">>>")
        print("3...")
        print("2...")
        print("1...")
        print("Done!")
        print ("The smoothie is done! Thanks for playing and enjoy your smoothie!")
        break

    elif   user_input == "Rose":
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
        break

    else:
        print("Goodbye!")
        break
