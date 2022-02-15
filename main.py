from time import sleep

#class that helps me change the color of text. \033[ is the escape code
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#created starterPokemon class to hold different defs
class pokemon():
    # used __init__ to assign values. Its executed when class in initiated so it makes sure these values are set right at the beginning.
    def __init__(self, name, type, health, attack, defense):
        self.name = name
        self.type = type
        self.health = health
        self.attack = attack
        self.defense = defense
    def take_damage(self, decrease_health):
        self.health -= decrease_health + self.defense
    def health_potion(self, increase_health):
        self.health += increase_health
    def check_health(self):
        print(self.health)

#made this to get the loading text effect
def loading_print(text, rnum = 5, sec = .5):
    num_dots = 0
    print(end = text)

    for x in range(rnum):
        if num_dots == 3:
            #flush stops the function from buffering to make everything happen faster. The default value for end is \n which adds the text to a new line. We can change this to make sure the text is on the same line.
            print(end='\b\b\b', flush=True)
            print(end='   ',    flush=True)
            print(end='\b\b\b', flush=True)
            num_dots = 0
        else:
            print(end=".", flush=True)
            num_dots += 1
        sleep(sec)

#created starter_pokemon
starter_pokemon1 = pokemon("Bulbasaur", "Earth", 45, 49, 49)
starter_pokemon2 = pokemon("Charmander", "Fire", 39, 52, 43)
starter_pokemon3 = pokemon("Squirtle", "Water", 44, 48, 65)

user_name = ""


def intro():
    #I need to use global in order to change the variable outside the function
    global user_name
    
    loading_print("Hello there! Welcome to the world of Pokémon! My name is OAK")
    loading_print("\nPeople call me the Pokémon PROF")
    loading_print("\nThis world is inhabited by creatures called Pokémon")
    loading_print("\nFor some people, Pokémon are pets. Others use them for fights")
    loading_print("\nMyself...I study Pokémon as a profession")
    
    print(color.YELLOW + "\n\nFirst, what is your name?" + color.END)
    user_name = input("> ")
    user_name = user_name.title()
    loading_print("\nRight! So your name is"+ color.YELLOW + f" {user_name}" + color.END)
    loading_print(f"\n\n{user_name}! Your very own Pokémon legend is about to unfold!\nA world of dreams and adventures with Pokémon awaits! Let's go")
    
    loading_print("\n", 8, .2)

    print(color.BOLD + "\n*You attempt to walk out the door*" + color.END)

    loading_print("", 8, .2)
    
    loading_print("\nHey! Wait! Don't go out")
    loading_print("\nIt's unsafe! Wild Pokémon live in the tall grass")
    loading_print("\nYou need your own Pokémon for your protection. I know! Here, come with me")

def starter_selection():
    print("\n\n___________________________________")
    loading_print("", 8, .2)
    
    print(color.BOLD + "\n\n*He takes you to his laboratory. They approach a table upon which three Poke Balls have been placed*" + color.END)

    loading_print("", 8, .2)
    
    loading_print(f"\n\nHere, {user_name}! There are 3 Pokémon here! Haha! They are inside the Poke Balls")
    loading_print("\nWhen I was young, I was a serious Pokémon trainer")
    loading_print("\nIn my old age, I have only 3 left, but you can have one")

    print(color.YELLOW + f"\n\nNow, {user_name}, which Pokémon do you want?" + color.END)
    print(color.GREEN + f"The three available Pokemon are Bulbasaur [1], Charmander [2], and Squirtle [3]" + color.END)

    while True:
        selected_starter = input("Select your starter by typing either 1, 2, or 3!\n> ")
        if selected_starter == "1":
            selected_starter = starter_pokemon1
            break
        elif selected_starter == "2":
            selected_starter = starter_pokemon2
            break
        elif selected_starter == "3":
            selected_starter = starter_pokemon3
            break
        else:
            print("That's not an option. Please try again.\n")
            continue

intro()
starter_selection()