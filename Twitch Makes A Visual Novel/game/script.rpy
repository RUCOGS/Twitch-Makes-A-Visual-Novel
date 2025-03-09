 # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform half_size: 
    zoom 0.5 #adjust as required

transform twice_size:
    zoom 2.0


init:
    $ fade = Fade(0.5, 0.0, 0.5, color = "#FFFFFF")
image Cogschan = "Cogschan.PNG"
image Ganon = "ganon.PNG"
image Ganon Eggs = "ganon.PNG" 
image evilFairy = "fairy.PNG"
image bg room = "forest.jpg"
image store = "store.png"
image forest blue = "forestblue.png"
image big boom = "bigboom.png"
image dark lonk:
    "darklonk.png"
    zoom 0.5
image lonk:
    "lonk.png"
    zoom 0.5

define c = Character("COGS-chan")
define e = Character("Evil Fairy") 
define g = Character("Ganon") 
define cg = Character("Costco Guys")
define l = Character("Lonk")
define dl = Character("Dark Lonk")
 

#

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room at twice_size

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Cogschan at half_size

    # These display lines of dialogue.

    c "It's a beautiful day, the sun is shining, birds are singing."

    hide Cogschan
    show fairy

    e "On day like these... kids like you..."


    c "GULP! Who's that?"

    hide fairy
    show Cogschan at half_size

    "The mysterious entity disappears."

    c "Welp. I have to buy some eggs today. I gotta eat."

    c "Yummy. That sounds delicious."

    scene store at twice_size

    show Cogschan at half_size

    c "Finally, I can EAT! These eggs look very expensive!"


    "COGS-Chan goes in for the grab. She wants those eggs. Delicious, beautiful, scrumptious EGGS."

    hide Cogschan
    show Ganon

    g "Move out the way!"

    hide Ganon
    show Ganon Eggs

    g "GRRRRR!"


    "COGS-Chan looks up to see a huge, overwhelming presence."

    g "Run along! Scram!"

    hide Ganon Eggs

    "COGS-Chan runs away with her tail between her legs."

    c "I'll take a shortcut home. Umm... I think the forest is the fastest way there."

    c "I'll head in the deep green forest."

    scene bg room at twice_size

    "*Walking Through the forest*"

    "THUMP!"

    c "OWIE! That tree was a heavy hitter..."

    scene black

    c "Huh. What's happening?"

    "She feels a strange aura. An unmistakable aura from before. She attempts to open her eyes."

    scene forest blue at twice_size

    c "Why is everything blue?!?!"

    show fairy

    e "YOU ARE TRAPPED FOREVER! YOU FOOL!!!! HA HA HA!"

    hide fairy
    show big boom

    cg "Well played, evil fairy! YOU GET FIVE BIG BOOMS!"

    cg "BOOM!"

    ''

    cg "BOOM!"

    ''

    cg "BOOM!"

    ''

    cg "BOOM!"

    ''

    cg "BOOM!"

    e "You are obnoxious! I'm gonna trap you here forever!"

    cg "Not if I have anything to say about this!"

    c "Yeah, you tell em Costco Guys!"

    cg "I'm going to activate my super power"
    
    cg "Super"
    
    cg "Chicken"
    
    cg "Bake"

    cg "Blast!!!!"

    show big boom at left
    show fairy at right

    e "Ough, my weakness!"
    
    e "Chicken bakes!"

    "She sees the blast of chicken bakes hits Fairy."

    "But suddenly, Fairy vanishes and takes with it the Costco Guys."

    hide big boom
    hide fairy
    show Cogschan at half_size

    c "Wait! I need my booms..."

    "Cogs chan is now alone in the deafening silence of the blue forest."

    "Suddenly, an eerie noise reverberates throughout the woods..."

    "u u u u u u...."

    c "Who's there?"

    "Cogs chan swivels her head frantically as she sees a green-hatted goofball!"

    show lonk at right

    l "Um.... Hello.... RED.... GIRL...."

    l "How did you get here?"

    c "I was transported here by a fairy."

    c "I'm looking for a way out."

    c "Can you help me?"

    l "Ah, the fairy!"

    l "She's the keeper of the blue woods"

    l "Every once in a millenium, a portal opens that bridges the blue-world with your world."

    "A ominous presence pops up. Dark and frightening aura eminates..."

    hide Cogschan
    show dark lonk at left

    dl "yOu MuSt nOT eScAPE!"

    l "Hyah! My evil twin has arrived! I'll fill you in later, runnnn!"
    

    "Dark lonk teleports infront of COGS-chan and prepares to strike"
    
    show lonk at right

    "Lonk teleports behind dark lonk"

    l "Omae wa mou shinderu!"

    dl "Nani?!"

    "Lonk swings his master sword and slices through Dark Lonk, turning him into dust"

    hide dark lonk

    l "I can only hold him off for so long."

    l "Dark Lonk is permanently tethered to this world, and he always comes back"
    
    "The pile of dust begins to stir..."

    l "I know a secret way out, follow me!"

    "Lonk leads cogs-chan to a secret cove carved into the side of a towering red-wood tree."

    "Within the cove lies a shell of a portal"

    l "I'll need a few minutes to conojour my spell and activate the portal back to your realm!"

    l "Just stand at the portal and you'll be fine!"

    show Cogschan at half_size  

    c "Got it Lonk!"

    "Cogs-chan sits in the portal, and the portal comes to life as Lonk activates the seal."

    "As the portal activates, Cogs-chan sees Dark Lonk appear at the cove's entrance, but Lonk has already finished the incantation and is ready to fight another day."

    "The eternal battle of lonks will never cease..."

    # transition to supermarket'

    

    ""

    scene store at twice_size 
    with fade


    "In a flash of white, COGS-chan falls out of a fridge door into the dairy aisle of the supermarket"

    show Ganon at right
    
    "Ganon towers in front of her"

    g "Ah, you're in the way!"

    show Cogschan at half_size
    
    "Ganon hastily shoves Cogs-chan aside as he fishes for a gallon of milk in the back of a fridge"

    c "What happened..."

    "As COGS-chan wanders out of the supermarket and heads back home, no one will know what happened that day."

    "The end!"
    
    # This ends the game.

    return
