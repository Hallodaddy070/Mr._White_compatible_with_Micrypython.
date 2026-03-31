import random

running = True

def my_random_choice(a_list):
    random_index = random.randint(0, len(a_list) - 1)
    return a_list[random_index]

def puntjes() :
    for i in range(6):
      print("")

Innocents = []
words = [
# Animals
"dog","cat","horse","cow","sheep","goat","chicken","rooster","duck","pig",
"lion","tiger","elephant","giraffe","zebra","monkey","bear","wolf","fox",
"deer","kangaroo","penguin","dolphin","shark","whale","octopus","turtle","crocodile","snake",
"eagle","owl","pigeon","sparrow","butterfly","bee","ant","spider","mosquito","squirrel",
"rabbit","hamster","guinea pig","parrot","canary","swan","seal","armadillo","badger","bat",
"bison","camel","caribou","crow","dove","ferret","flamingo","gecko","gorilla","heron",
"hyena","ibis","iguana","jackal","jaguar","Gargamel","Smurf",

# Family
"grandmother","grandfather","uncle","aunt","little brother","little sister","sister","brother",

# Professions
"baker","butcher","dentist","doctor","nurse","firefighter","police officer","teacher","hairdresser","chef",
"waiter","pilot","driver","farmer","architect","programmer","journalist","photographer","painter","actor",
"singer","musician","judge","lawyer","mechanic","electrician","plumber","captain","mailman","veterinarian",
"astronaut","librarian","taxi driver","inventor","director","manager","scientist","detective","gardener",

# Places
"castle","palace","prison","hospital","library","museum","stadium","theater","amusement park","zoo",
"beach","desert","jungle","island","volcano","waterfall","mountain","cave","harbor","market",
"restaurant","hotel","camping site","swimming pool","supermarket","church","mosque","temple","school","university",
"bridge","tunnel","tower","lighthouse","farm","office","factory","train station","airport","parliament",

# Events / Activities
"wedding","funeral","birthday","Christmas","Easter","carnival","festival","competition","exam","job interview",
"vacation","moving","accident","earthquake","storm","flood","reunion","farewell","opening","premiere",
"concert","play","movie night","campfire","picnic","parade","demonstration","meeting","school trip","final exam",
"dive","dance","hike","marathon","party","protest","race","workshop","yoga","zumba","expo","tournament","ceremony",
"trial","challenge","sleepover","camping","tour","trekking","paragliding","surfing","swimming","sailing",

# Objects / Things
"umbrella","suitcase","passport","phone","camera","glasses","key","wallet","backpack","helmet",
"bicycle","motorcycle","train","airplane","boat","car","scooter","skateboard","roller skates","tractor",
"candle","mirror","alarm clock","pillow","blanket","refrigerator","microwave","oven","pan","knife",
"fork","spoon","plate","glass","bottle","bag","coat","scarf","glove","cap",
"laptop","tablet","headphones","game console","remote control","microphone","printer","drone","robot vacuum","smartwatch",
"fitness tracker","wifi","podcast","video game","streaming service","controller","keyboard","mouse","monitor","speaker",
"book","chair","comb","computer","fan","lamp","microscope","notebook","pencil","radio","ruler","scissors","shovel",
"sofa","television","toothbrush","watch","wheelchair","bin","pendulum","paintbrush","palette","telescope","torch","violin",
"map","keychain","crystal","lantern","obelisk","quiver","satellite","scroll","scepter","trophy","vortex","whistle","zeppelin",

# Foods
"pizza","pancake","hamburger","soup","salad","ice cream","chocolate","cookie","cake","apple pie",
"spaghetti","rice","sandwich","cheese","sausage","apple","banana","strawberry","watermelon","lemon",
"grape","pineapple","mango","broccoli","carrot","fries","lasagna","pudding","popcorn",
"avocado","bagel","bacon","bread","brownie","cabbage","candy","cereal","cheesecake","chili",
"corn","croissant","cupcake","dumpling","eggs","falafel","guacamole","honey","lentils",
"mashed potatoes","noodles","oatmeal","omelette","pasta","peanut butter","pretzel","quiche","sushi","taco",
"tofu","waffle","yogurt",

# Fantasy / Fiction
"fairy tale","superhero","pirate","knight","witch","wizard","spy","monster",
"dragon","prince","queen","emperor","cowboy","ninja","samurai","viking","clown","magician",
"alien","zombie","ghost","time traveler","bodyguard","champion","referee","explorer",
"elf","fairy","goblin","griffin","mermaid","orc","princess","sorcerer","troll","vampire",
"werewolf","phoenix","giant","demon","unicorn","cyclops",

# Nature / Science
"moon","sun","planet","star","rainbow","lightning","snow","fog","iceberg","glacier",
"compass","treasure chest","diamond","gold","silver","statue","fountain","painting","comic book","diary",
"tent","sleeping bag","hammock","cage","aquarium","terrarium","carriage","harp","rocket","sailboat","windmill","yacht","amphitheater"
]

while running :
  puntjes()
  while True:
      print('How many players?')
      user_input_players = input()
      try:
          num_players = int(user_input_players)
          if num_players > 2:
              Amountofplayers = num_players
              break
          else:
              print("Minimum 3 players.")
      except ValueError:
          print("Invalid input.")

  while True:
      print('How many imposters?')
      user_input_imposters = input()
      try:
          num_imposters = int(user_input_imposters)
          if num_imposters > 0 and num_imposters <= num_players :
              Amountofimposters = num_imposters
              break
          else:
              print("Minimum 1 imposter.")
      except ValueError:
          print("Invalid input.")

  running_2 = True
  while running_2 :

    Innocents = []
    Innocent_counter = 1
    Imposters = []
    for i in range(Amountofplayers) :
      Innocents.append(Innocent_counter)
      Innocent_counter = Innocent_counter + 1

    puntjes()
    print(str(Amountofplayers) + ' players.')
    print(str(Amountofimposters) + ' imposters.')
    print("- to end game.")
    Off = input("EXE to Start.")

    if Off == '-' :
        running_2 = False
        puntjes()
        print("Game ended.")
        print("New game?    - 1")
        print("Stop game?   - 2")

        while True:
            user_choice_final = input()

            if user_choice_final == '1':
                print("Starting new game...")
                break

            elif user_choice_final == '2':
                print("Goodbye!")
                running = False
                break

            else:
                print("Invalid input.")
        break

    puntjes()

    for i in range(Amountofimposters) :
      random_index = random.randint(0, len(Innocents)-1)
      imposter_player = Innocents.pop(random_index)
      Imposters.append(imposter_player)

    Word = my_random_choice(words)
    Currentplayer = 1
    puntjes()
    running_3 = True
    round_ended_early = False

    while running_3 and Currentplayer <= Amountofplayers:

      print("- to end game.")
      print('Number ' + str(Currentplayer) + ".")

      if Currentplayer in Innocents :
        print("Word: " + str(Word) + ".")
      else :
        print("You are the imposter.")

      Off = input("EXE to continue.")

      if Off == '-' :
        puntjes()
        print("Game ended.")
        print("Again?       - 1")
        print("New game?    - 2")
        print("Stop game?   - 3")

        while True:
            user_choice_final = input()

            if user_choice_final == '1':
                print("Starting new round...")
                round_ended_early = True
                break

            elif user_choice_final == '2':
                print("Starting new game...")
                running_2 = False
                break

            elif user_choice_final == '3':
                print("Goodbye!")
                running = False
                running_2 = False
                break

            else:
                print("Invalid input.")

        break

      if Currentplayer != Amountofplayers :
        puntjes()
        print('Number ' + str(Currentplayer+1) + ".")
        input("EXE to continue.")
        puntjes()

      Currentplayer = Currentplayer + 1

    if not running_2:
        break

    if round_ended_early:
        continue

    Imposter_guess = 0
    puntjes()
    
    guess_counter = 0
    guessed_players = []
    print(str(random.randint(1,Amountofplayers))+ " is first." )
    while len(Imposters) != 0 :
      start_new_round = False
      start_new_game = False
      stop_game = False

      print("- to end game.")
      print("Who is the imposter?")
      Imposter_guess_str = input()

      if Imposter_guess_str == '-':
          puntjes()
          print("Game ended.")
          print("Again?       - 1")
          print("New game?    - 2")
          print("Stop game?   - 3")

          while True:
              user_choice_final = input()

              if user_choice_final == '1':
                  print("Starting new round...")
                  start_new_round = True
                  break

              elif user_choice_final == '2':
                  print("Starting new game...")
                  start_new_game = True
                  break

              elif user_choice_final == '3':
                  print("Goodbye!")
                  stop_game = True
                  break

              else:
                  print("Invalid input.")

          break

      try:
        Imposter_guess = int(Imposter_guess_str)
        puntjes()
        if Imposter_guess < 1 or Imposter_guess > Amountofplayers:
          print("Player doesn't exist.")
          continue

        if Imposter_guess in guessed_players:
          print("Already guessed.")
          continue

        guessed_players.append(Imposter_guess)

        if Imposter_guess in Imposters:
          print("You are right!")
          guess_counter = guess_counter + 1
          Imposters.remove(Imposter_guess)

          if len(Imposters) == 0:
            break
        else:
            print("Wrong.")
            guess_counter = guess_counter + 1

      except ValueError:
        print("Invalid input.")

    if stop_game:
      running = False
      break

    if start_new_game:
      running_2 = False
      break

    if start_new_round:
      continue

    puntjes()
    if guess_counter == Amountofimposters :
      print("Innocents won!")
    else :
      if Amountofimposters == 1 :
        print("The imposter won!")
      else :
        
        print("The imposters won!")
    
    print("Again?       - 1")
    print("New game?    - 2")
    print("Stop game?   - 3")

    while True:
        user_choice_final = input()

        if user_choice_final == '1':
           print("Starting new round...")
           break

        elif user_choice_final == '2':
           print("Starting new game...")
           break

        elif user_choice_final == '3':
           print("Goodbye!")
           running = False
           break

        else:
          print("Invalid input.")

    if user_choice_final == '1':
        continue
    elif user_choice_final == '2':
        break
    elif user_choice_final == '3':
        break
