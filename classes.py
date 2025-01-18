#Welsoome! This is my demoostration of classes in Python! A Short story introducing the user and 
#asking general questions only using functions, classes and variables.

#This is the class of the Person in our story
class Person:
    def __init__(self, name, age, dish):
        self.name = name
        self.age = age
        self.dish = dish
    #Self, Say hi to the user   
    def say_hi(self):
        print("Hello! My name is", self.name)
        
     #Self, ask name of the user   
    def ask_name(self):
        user_input = input("What is your name? >>>")
        if user_input == user_input:
           print("Cool name friend!")
    
    #Self, ask favorite dish of the user  
    def ask_fav(self):
        user_input = input("What is your favorits dish? >>>")
        if user_input == user_input:
            print("Yummy! Sounds delicious! Mine is", p1.dish)       
     
    #Self, ask age of the user, but if it's a duplicate of my age then return a different messgae       
    def ask_age(self):
        user_input = input("How old are you? >>>")
        if user_input == "22":
            print("Really? I'm", self.age, "as well!")
        else: 
            user_input == user_input
            print("That's nice! I'm", self.age)
            
    #Self, scold p2 from the conversation with the user
    def scold(self):
        user_input = input(">>>")
        if user_input == user_input:
            print("Don't speak to him friend...HEY! Go away Elon!")
            
    #Self, p2 runs away crying, no matter what the user types
    def cry(self):
        user_input = input(">>>")
        if user_input == user_input:
            print(p2.name, "*Runs away crying*")
            
    #Self, laughs at p2 Running away     
    def laugh(self):
        user_input = input(">>>")
        if user_input == user_input:
            print("Ha Ha Ha! I hope that he cries at home!")
    
    #Self, say bye to our new user friend    
    def say_bye(self):
        user_input = input("Welp, I'm leaving now! You headed home too? >>>")
        if user_input == user_input:
            print("Bye friend!")
            
#These are my characters, including me      
p1 = Person("Rose Parker", 22, "Chinese food")
p2 = Person("Elon Musk", 53, "Ketchup")
p3 = Person("Billy Grisham", 23, "Spaghetti")

#This is the story board using classes and functions that were earlier defined for the storyboard
p1.say_hi()
p1.ask_name()
p1.ask_age()
p1.ask_fav()
p2.say_hi()
p1.scold()
p2.cry()
p1.laugh()
p1.say_bye()

        