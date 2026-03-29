#1.3
import random
running = True

def my_random_choice(a_list):
    random_index = random.randint(0, len(a_list) - 1)
    return a_list[random_index]

def puntjes() :
    for i in range(6):
      print("")

Innocents = []
words=[
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

undercover_mapping = {
"dog": "wolf","cat": "lion","horse": "zebra","cow": "bison","sheep": "goat",
"goat": "sheep","chicken": "duck","rooster": "chicken","duck": "goose","pig": "boar",
"lion": "tiger","tiger": "leopard","elephant": "rhino","giraffe": "camel","zebra": "horse",
"monkey": "chimpanzee","bear": "panda","wolf": "fox","fox": "coyote","deer": "elk",
"kangaroo": "koala","penguin": "seal","dolphin": "whale","shark": "octopus","whale": "dolphin",
"octopus": "squid","turtle": "tortoise","crocodile": "alligator","snake": "lizard",
"eagle": "hawk","owl": "falcon","pigeon": "dove","sparrow": "finch","butterfly": "moth",
"bee": "wasp","ant": "termite","spider": "scorpion","mosquito": "fly","squirrel": "chipmunk",
"rabbit": "hare","hamster": "gerbil","guinea pig": "rabbit","parrot": "canary","canary": "finch",
"swan": "goose","seal": "otter","armadillo": "pangolin","badger": "wolverine","bat": "flying fox",
"bison": "buffalo","camel": "llama","caribou": "reindeer","crow": "raven","dove": "pigeon",
"ferret": "weasel","flamingo": "stork","gecko": "lizard","gorilla": "chimpanzee","heron": "egret",
"hyena": "jackal","ibis": "crane","iguana": "chameleon","jackal": "wolf","jaguar": "panther",
"Gargamel": "Smurf","Smurf": "Gargamel",
"grandmother": "grandfather","grandfather": "grandmother","uncle": "aunt","aunt": "uncle",
"little brother": "little sister","little sister": "little brother","sister": "brother","brother": "sister",
"baker": "chef","butcher": "farmer","dentist": "doctor","doctor": "nurse","nurse": "doctor",
"firefighter": "police officer","police officer": "firefighter","teacher": "professor","hairdresser": "barber","chef": "baker",
"waiter": "bartender","pilot": "astronaut","driver": "taxi driver","farmer": "gardener","architect": "engineer",
"programmer": "scientist","journalist": "photographer","photographer": "journalist","painter": "sculptor","actor": "director",
"singer": "musician","musician": "singer","judge": "lawyer","lawyer": "judge","mechanic": "electrician",
"electrician": "plumber","plumber": "mechanic","captain": "pilot","mailman": "taxi driver","veterinarian": "zoologist",
"astronaut": "pilot","librarian": "teacher","taxi driver": "driver","inventor": "scientist","director": "producer",
"manager": "director","scientist": "programmer","detective": "police officer","gardener": "farmer",
"castle": "palace","palace": "castle","prison": "hospital","hospital": "clinic","library": "museum",
"museum": "library","stadium": "arena","theater": "opera house","amusement park": "zoo","zoo": "aquarium",
"beach": "island","desert": "mountain","jungle": "forest","island": "beach","volcano": "mountain",
"waterfall": "river","mountain": "hill","cave": "tunnel","harbor": "lighthouse","market": "bazaar",
"restaurant": "cafe","hotel": "hostel","camping site": "tent","swimming pool": "lake","supermarket": "store",
"church": "temple","mosque": "church","temple": "mosque","school": "university","university": "school",
"bridge": "tunnel","tunnel": "bridge","tower": "lighthouse","lighthouse": "tower","farm": "office",
"office": "factory","factory": "office","train station": "airport","airport": "train station","parliament": "court",
"wedding": "birthday","funeral": "farewell","birthday": "party","Christmas": "Easter","Easter": "Christmas",
"carnival": "festival","festival": "carnival","competition": "tournament","exam": "final exam","job interview": "meeting",
"vacation": "trip","moving": "relocation","accident": "storm","earthquake": "flood","storm": "earthquake",
"flood": "storm","reunion": "meeting","farewell": "goodbye","opening": "premiere","premiere": "opening",
"concert": "play","play": "concert","movie night": "cinema","campfire": "picnic","picnic": "campfire",
"parade": "demonstration","demonstration": "parade","meeting": "reunion","school trip": "tour","final exam": "exam",
"dive": "swimming","dance": "yoga","hike": "trekking","marathon": "race","party": "celebration",
"protest": "demonstration","race": "marathon","workshop": "seminar","yoga": "pilates","zumba": "dance",
"expo": "tournament","tournament": "competition","ceremony": "ritual","trial": "challenge","challenge": "trial",
"sleepover": "camping","camping": "sleepover","tour": "trip","trekking": "hike","paragliding": "surfing",
"surfing": "paragliding","swimming": "dive","sailing": "boat","umbrella": "coat","suitcase": "backpack","passport": "ID",
"phone": "headphones","camera": "drone","glasses": "binoculars","key": "lock","wallet": "bag","backpack": "suitcase",
"helmet": "cap","bicycle": "scooter","motorcycle": "bicycle","train": "subway","airplane": "helicopter","boat": "sailing",
"car": "taxi","scooter": "motorcycle","skateboard": "roller skates","roller skates": "skateboard","tractor": "farm",
"candle": "torch","mirror": "painting","alarm clock": "watch","pillow": "blanket","blanket": "pillow",
"refrigerator": "microwave","microwave": "oven","oven": "pan","pan": "knife","knife": "fork",
"fork": "spoon","spoon": "plate","plate": "bowl","glass": "bottle","bottle": "glass","bag": "wallet",
"coat": "jacket","scarf": "glove","glove": "mittens","cap": "hat","laptop": "tablet","tablet": "laptop",
"headphones": "speaker","game console": "controller","remote control": "TV","microphone": "speaker","printer": "scanner",
"drone": "camera","robot vacuum": "mop","smartwatch": "fitness tracker","fitness tracker": "smartwatch",
"wifi": "router","podcast": "radio","video game": "board game","streaming service": "podcast",
"controller": "game console","keyboard": "mouse","mouse": "trackpad","monitor": "TV","speaker": "microphone",
"book": "notebook","chair": "sofa","comb": "brush","computer": "laptop","fan": "air conditioner",
"lamp": "candle","microscope": "telescope","notebook": "journal","pencil": "pen","radio": "podcast",
"ruler": "tape measure","scissors": "knife","shovel": "spade","sofa": "chair","television": "monitor",
"toothbrush": "toothpaste","watch": "clock","wheelchair": "walker","bin": "trash can","pendulum": "clock",
"paintbrush": "palette","palette": "paintbrush","telescope": "microscope","torch": "candle","violin": "cello",
"map": "compass","keychain": "pendant","crystal": "gem","lantern": "candle","obelisk": "statue",
"quiver": "bow","satellite": "rocket","scroll": "diary","scepter": "wand","trophy": "medal",
"vortex": "tornado","whistle": "horn","zeppelin": "airplane",
"pizza": "pasta","pancake": "waffle","hamburger": "hotdog","soup": "stew","salad": "coleslaw",
"ice cream": "sorbet","chocolate": "candy","cookie": "brownie","cake": "pie","apple pie": "cake",
"spaghetti": "lasagna","rice": "noodles","sandwich": "burger","cheese": "yogurt","sausage": "bacon",
"apple": "banana","banana": "apple","strawberry": "raspberry","watermelon": "melon","lemon": "lime",
"grape": "raisin","pineapple": "mango","mango": "papaya","broccoli": "cabbage","carrot": "turnip",
"fries": "potatoes","lasagna": "spaghetti","pudding": "custard","popcorn": "chips","avocado": "guacamole",
"bagel": "croissant","bacon": "sausage","bread": "baguette","brownie": "cookie","cabbage": "lettuce",
"candy": "chocolate","cereal": "granola","cheesecake": "pie","chili": "soup","corn": "maize",
"croissant": "bagel","cupcake": "muffin","dumpling": "ravioli","eggs": "omelette","falafel": "tofu",
"guacamole": "avocado","honey": "syrup","lentils": "beans","mashed potatoes": "fries","noodles": "rice",
"oatmeal": "porridge","omelette": "eggs","pasta": "spaghetti","peanut butter": "jelly","pretzel": "bread",
"quiche": "omelette","sushi": "sashimi","taco": "burrito","tofu": "tempeh","waffle": "pancake","yogurt": "cheese",
"fairy tale": "fable","superhero": "villain","pirate": "privateer","knight": "squire","witch": "wizard",
"wizard": "sorcerer","spy": "detective","monster": "creature","dragon": "wyvern","prince": "duke",
"queen": "princess","emperor": "king","cowboy": "rancher","ninja": "samurai","samurai": "ninja",
"viking": "raider","clown": "magician","magician": "illusionist","alien": "extraterrestrial","zombie": "vampire",
"ghost": "spirit","time traveler": "explorer","bodyguard": "guard","champion": "winner","referee": "umpire",
"explorer": "adventurer","elf": "fairy","fairy": "elf","goblin": "troll","griffin": "pegasus","mermaid": "siren",
"orc": "goblin","princess": "queen","sorcerer": "wizard","troll": "giant","vampire": "werewolf",
"werewolf": "vampire","phoenix": "firebird","giant": "titan","demon": "devil","unicorn": "pegasus",
"cyclops": "giant","moon": "sun","sun": "moon","planet": "star","star": "planet","rainbow": "lightning",
"lightning": "thunder","snow": "ice","fog": "mist","iceberg": "glacier","glacier": "iceberg",
"compass": "map","treasure chest": "gold","diamond": "ruby","gold": "silver","silver": "gold",
"statue": "obelisk","fountain": "statue","painting": "portrait","comic book": "diary","diary": "journal",
"tent": "hammock","sleeping bag": "tent","hammock": "sleeping bag","cage": "terrarium","aquarium": "terrarium",
"terrarium": "aquarium","carriage": "wagon","harp": "piano","rocket": "satellite","sailboat": "yacht",
"windmill": "mill","yacht": "sailboat","amphitheater": "theater"
}

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
          if num_imposters > -1 and num_imposters <= num_players :
              Amountofimposters = num_imposters
              break
          else:
              print("Atleast 0 imposters.")
      except ValueError:
          print("Invalid input.")
  while True :
      print('How many undercovers?')
      user_input_undercovers = input()
      try:
          num_undercovers = int(user_input_undercovers)
          if num_undercovers >= 0 and num_undercovers <= num_players - Amountofimposters :
              Amountofundercovers = num_undercovers
              break
          else:
            print('Excess undercovers.')
      except ValueError:
        print("Invalid input.")

  running_2 = True
  while running_2 :

    Innocents = []
    Innocent_counter = 1
    Imposters = []
    undercovers = []
    for i in range(Amountofplayers) :
      Innocents.append(Innocent_counter)
      Innocent_counter = Innocent_counter + 1

    puntjes()
    print(str(Amountofplayers) + ' players.')
    print(str(Amountofimposters) + ' imposters.')
    print(str(Amountofundercovers) + ' undercovers.')
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

    for i in range(Amountofundercovers) :
      random_index = random.randint(0, len(Innocents)-1)
      undercover_player = Innocents.pop(random_index)
      undercovers.append(undercover_player)

    Word = my_random_choice(words)
    Undercover_word = undercover_mapping.get(Word, Word)######################################################################
    Currentplayer = 1
    puntjes()
    running_3 = True
    round_ended_early = False

    while running_3 and Currentplayer <= Amountofplayers:

      print("- to end game.")
      print('Number ' + str(Currentplayer) + ".")
      if Currentplayer in Innocents :
        print("Word: " + str(Word) + ".")
      elif Currentplayer in Imposters :
        print("You are the imposter.")
      elif Currentplayer in undercovers :
        print("Word: " + str(Undercover_word) + ".")

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
    while len(Imposters) + len(undercovers) != 0 :
      start_new_round = False
      start_new_game = False
      stop_game = False

      print("- to end game.")
      print("Who is not innocent?")
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

        if Imposter_guess in Imposters or Imposter_guess in undercovers:
          print("You are right!")
          guess_counter += 1
          if Imposter_guess in Imposters:
              Imposters.remove(Imposter_guess)
          if Imposter_guess in undercovers:
              undercovers.remove(Imposter_guess)
        else:
          print("Wrong.")
          guess_counter += 1

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
    if guess_counter == Amountofimposters + Amountofundercovers :
      print("Innocents won!")
    else :
      print("Innocents lost!")

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