# Level 1
import random
def path1():
path1 = input("What do you choose to do, stay inside(1) or run outside and help(2)?")
if path1 == "1" :
path1_1()
elif path1 =="2":
path1_2()
else:
print("Invalid input, please try again!")
path1Choice()
def restartChoice():
restart = input("Would you like to try that again? (Y/N)")
if restart == "Y":
path1_2()
elif restart == "N":
print("Shame, bye bye!")
else:
print("Invalid input, please try again!")
restartChoice()
#in the list of weapons, "none" is a choice
#hand of Fate will determine whether you live or game over
#it is completely random
def handofFate():
fate = random.randint(1,2)
if fate == 1:
print("Sorry, game over!")
restartChoice()
else:
print("You survived.")



def path1_1() :
print("You choose to stay inside and ignore the chaos that is going on outside. After all, it's not
your problem.")
print("Why should you risk your life if you are so comfy in your own home?")
print("Congratulations, humanity is doomed but at least you'll be relaxing in your own
home!")
def path1_2():
print("You bolt open the door to the outside and find a bunch of zombies, what the hell?!")
print("The news wasn't lying for once!")
print("You see a bunch of other survivors running away and trying to fight off the undead
aliens!")
print("You quickly look around, your good natured self can't just let these people fight all by
themselves...")
print("After all, the zombies are coming for you too!")
print("You look around frantically for a weapon... Bingo!")
#assuming that knife is the only right answer,
#you will have to keep playing until you are given the option of "knife"
#or until you have the option of "none", which is a 50/50 chance random survival
#if you want to always have the right option tho,
#you may want to consider making two lists like the one on level 5 with correct and incorrect
body part
weapon = ['knife','tree branch', 'pebble', 'soil', 'left shoe', 'right shoe','none']
num = random.randint(0,len(weapon)-1)
newNum = random.randint(0,len(weapon)-1)
while num == newNum:
newNum = random.randint(0,len(weapon)-1)
one = (weapon[num])
two = (weapon[newNum])
print("What do you choose,", one,"(1) or", two,"(2)?")
path2 = int(input("Choice:"))
if path2 == 1 and one == "knife":
print("The obvious choice, how boring! But practical.")
print("John quickly dives to grab the combat knife, and does a quick 180 to stab the zombie
that was")
print("apparently coming up behind him!")
print("You make your way to the other survivors and quickly dispose of the zombies due to
them being")


print("distracted with the other humans.")
elif path2 == 2 and two == "knife":
print("The obvious choice, how boring! But practical.")
print("John quickly dives to grab the combat knife, and does a quick 180 to stab the zombie
that was")
print("apparently coming up behind him!")
print("You make your way to the other survivors and quickly dispose of the zombies due to
them being")
print("distracted with the other humans.")
elif path2 == 1 and one == "none":
print("Guess you are going for close combat.")
print("Wish you the best of luck.")
print("Sometimes in life there is no right choices...")
print("Your fate is in your hands.")
handofFate()
elif path2 == 2 and two == "none":
print("Guess you are going for close combat.")
print("Sometimes in life there is no right choices...")
print("Your fate is in your hands.")
handofFate()
elif path2 == 1:
print("Ah yes, the mighty %s, this will surely get those zombies good!" %one)
print("You run up to the first zombie you see and use it with all your might!")
print("You expect glorious blood splattering and gore, only to be met with
disappointment...")
print("The %s is rendered useless upon impact as you stand there looking stupid." %one)
print("Now that that dramatic sequence is over, the zombies quickly overwhelm you and
you die.")
print("Sorry, game over!")
restartChoice()
elif path2 == 2:
print("Ah yes, the mighty %s, this will surely get those zombies good!" %two)
print("You run up to the first zombie you see and use it with all your might!")
print("You expect glorious blood splattering and gore, only to be met with
disappointment...")
print("The %s is rendered useless upon impact as you stand there looking stupid." %two)
print("Now that that dramatic sequence is over, the zombies quickly overwhelm you and
you die.")
print("Sorry, game over!")


restartChoice()

path1Choice()

name = input("Please enter your name: ")
print("Welcome to The Last of Humanity %s" % name)
print("You find yourself alone in an LA apartment, you hear a bunch of fighting outside, with
bloodprints all over your windows!")
print("You tune on the television and hear the piercing sounds of the emergency broadcast
systems, the US IS IN DANGER.")
print("Videos of UFOs and zombies roaming the streets are all over Fox news, you can't even
believe it with your eyes...")
print("You play as John, an ex military veteran who has been preparing for the worst.")
print("You best hope your skills are sharp and your intuition are on par in order to deal with the
situation.")
print("Suddenly, you hear the screams of other people outside!")
path1Choice()

# level 2
##Level 2
print("Welcome to level 2!")
print("**You have to figure out a way to get over a river that's filled with lava and rocks that
would\nsometime burst into flames which used to be the Potomac River" )
print("Please choose your methods below\n ")
print("1. Using Special Alien UFO", "2. Hopping on the rock","3. Swimming across the Lava")
print("Hint: The lava is 2000 Fahrenheit")
methods = False
while not methods:
methods = input("What is your method (Please write: 1, 2 or 3): ")

25

if methods != "1":
methods= False
print("The Lava is too hot, you can't get close to it or it will burn you to death")
print("Failed! Please try again!")
else:
print("That's a great idea! Let's go...\n\n\n\n\n")
print("**They realize that they need to have the key to start the engine")
print("The key was hidden under few mysterious boxes")
print("Only the aliens have crystal eyes that could see through everything\n")
print("There are only 3 guesses for John and Survivors,\notherwise the system will alert the
Aliens and you will die.")
print("Now they will need to choose the right box to get a key!")
right_box = random.randint(1,10)
guesses_remaining = 3

keep_playing = "true"
while keep_playing == "true":
guess = int(input("\nGuess a number between 1 and 10: "))
guesses_remaining = guesses_remaining - 1
if guess == right_box:
print ("Bravo! You guessed the correct box. ")
print("You are now passed level 2!")
keep_playing = "false"
else:
if guesses_remaining == 0:
print ("\nYou are out of guesses! The right box was:",right_box)
print("The system is alerting the Aliens...")
print("\n\n Game over!")
keep_playing = "false"
elif guess != right_box:
print("Sorry, that is not the correct box. Try again!")

# level 3



import random

def start3():
print("As John is slowly waking up, he feels the ground slightly rumble beneath him")
print("However, John sees most of the other survivors still sleeping...")
choice = input("Should John look up the window to see what is making the ground shake or go
back to sleep.\n Type look or sleep: ")
if choice == "look" :
print()
path1()
if choice == "sleep" :
print("When John went back to sleep, he had a great dream but unfortunately never woke up
again")
print("Good luck next try! \n")

start3()
def path1():
print("John cautiously walks to the window....")
print("He leans toward the window and sees a gigantic zombie alien! John mutters under his
breath that it must be at least the size of a four story building")
print("John looks back to see the rest of the group and sees them now almost all woken up as
the giant zombie alien stumbles closer and closer to them")
print("John can only think of two choices!Go look for the weirdly-shaped alien laser gun or
run outside to distract the big alien zombie")
print("Choice 1: Run OR Choice 2: get the gun!")
answer2 = input("Enter 1 or 2: ")
if "2" in answer2:
path3()

else:
print("John ran track in highschool but since then he's gained a few pounds, regardless he
ran for his dear life!")
print("John is huffin n puffin....he knows he won't be able to outrun the giant alien zombie")
print("Choice 1: Run into an adjacent derelict building to hide from the giant zombie alien



OR Choice 2:Hide underneath a old van")
answer3 = input("Enter 1 or 2: ")
if "1" in answer3:
print("John turns the corner and runs into the abandoned house!")
print("The giant zombie alien attempts to reach inside to grab John but instead causes
the front entrance to collapse and entrap John!")
locked()

def locked():
print("John looks over at the pile of debris now blocking the front entrance and then scans
over to a lone metal door")
print("You examine the door, a three digit lock built internally built into the door stops John
from seeing if the doorway leads to the outside")
print("On the floor next to door lies a ragged note which reads: ")
print("As my time is near...\n")
print("what lies past this door is of \n")
print("no use to me when I'm dead\n")
print("perhaps it may help you...if you")
print("can solve this riddle...\n")
print("First number: I'm a number with a couple of friends, quarter a dozen, and you'll find me
again.")
print("Second number: Mom and dad have four daughters, and each daughter has one brother.
How many people are in the family?")
print("Third number: Three times what number is no larger than two times that same number?
\n")
answercombo1 = input("Enter the first riddle's number in the lock : ")
answercombo2 = input("Enter the second riddle's number in the lock: ")
answercombo3 = input("Enter the third riddle's number in the lock : ")
if "3" in answercombo1 and "7" in answercombo2 and "0" in answercombo3:
print("Thunk...it seems John is quite smart and got the combination correct! ")
combopath()
else:
print("The numbers you put in didn't seem to unlock the door, perhaps try again")
answercombo1 = input("Enter the first riddle's number in the lock : ")
answercombo2 = input("Enter the second riddle's number in the lock: ")
answercombo3 = input("Enter the third riddle's number in the lock : ")
if "3" in answercombo1 and answercombo2 =="7" and answercombo3 =="0":



print("Thunk...it seems John is quite smart and got the combination correct! ")
combopath()
else:
print("Maybe John wasn't as smart as he thought....after putting in the last set of numbers
he seems to have broken the lock")
print("With the lock broken and the entrance blocked off with debris...John has
unfortunately met his final resting place\n")
start3()
def combopath():
c4amt = random.randint(1,3)

print("John pushes the door open and is greeted with a musty room filled with large wooden
boxes and a tunnel entrance in the back corner")
print("You start opening the crates and find them filled with C-4, explosives with built in
fuses")
print("You find",c4amt, "C-4 still in good condition and crawl through the tunnel")
print("After pushing a manhole cover out of the way, you find youself back in fresh air....but
can hear screaming coming from where the group's building is!")
print("Once you get closer you see one of the survivors trying to crawl towards the alien
gun...but its directly underneath the giant alien zombie..")
print("You have",c4amt,"C-4 charges and take a second to think of your available
options....\n")
print("Option 1: Go to the roof of the building across from the giant alien zombie and attempt
to throw a C-4 charge at the alien's face")
print("Option 2: Flank the alien zombie and put a C-4 charge on it's achilles tendon")
combopathchoices = input("Enter your 1 or 2: ")
if "1" in combopathchoices:
print("You run up four flights of stairs and find yourself on the roof...just 20 feet across from
you is the giant alien zombies head")
print("John sets the fuse on the C-4 and readies himself to play C-4 dodgeball with the giant
zombie alien!!")
roll = input("When ready to throw, roll the 10 sided die. In order to accurately hit the alien
you must roll atleast or above a 6! Enter Y when ready: ")
boom = random.randint(1,10)
while c4amt > 0:
if roll =="Y" and boom >= 6:
print("You rolled a",boom,"!")



print("BOOOOOOOM...the giant alien zombie's head exploded....if Earth ever goes
back to normal, John might have a chance at going pro in dodgeball\n")
print("Congratulations you passed the level and defeated the infamous giant alien
zombie!")
lvl4()
break
elif boom <=5 and c4amt > 0 :
boom = random.randint(1,10)
print("Darn, you only rolled a",boom,"and the timing was off.")
c4amt = c4amt -1
print("You have",c4amt,"C-4 charge(s) remaining \n")
print("You attempt to throw another C-4 charge")
if c4amt == 0:
print("You ran out of C-4....\n")
print("Your only other option is to go get the alien laser gun\n")
print("John runs down the stairwell and sprints out of the building entrance directly to
the alien laser gun in the street...")
path3()
break

if "2" in combopathchoices:
flank()

def flank():
print("While the giant alien zombie is distracted trying to grab one of the survivors, you run
into an alleyway until you just past the giant alien zombie")
print("You catch your breath and then prime the C-4 charge")
print("In order to to be effective, the C-4 must be placed directly on the zombie's achilles.")
print("John is trying to remember where the Achilles tendon is...perhaps if he thinks of where
the Achilles mythology originated from he might remember...")
trivia = input("Hmmm where did the story originate from? Was it France/Egypt/Greece/Persia.
Type your answer: ")
if trivia == "Greece" or "greece":



print("John must be a history buff! After thinking of where Achilles story came from, he
now knows where to put the C-4 /n")
print("You sprint at full speed while the giant alien zombie is looking the other direction and
place the C-4 in the exact right spot!")
print("John quickly runs away and hops a barricade and then usees it to take
cover.....BOOOOM")
print("Once the giant alien zombie fell and was unable to chase the group, John and the
others escaped....")
print("Congratulations you passed level 3")
else:
print("Well that wasn't right...John thinks of when he was back in 8th grade learning about
Homer, the Odyssey, and Plato")
tryagain = input("Your running out of time...this is your last shot before its too late: ")
if tryagain == "Greece" or "greece":
print("You sprint at full speed while the giant alien zombie is looking the other direction
and place the C-4 in the exact right spot!")
print("John quickly runs away and hops a barricade and then usees it to take
cover.....BOOOOM")
print("Once the giant alien zombie fell and was unable to chase the group, John and the
others escaped....")
print("Congratulations you passed level 3")
else:
print("The correct answer was Greece! If only John had paid attention to his 8th grade
history teacher")
print("Since John didn't know the best place to put the C-4, he put it between the giant
aliens toes but got squashed right after...")
start3()

def path3():
print("John grabs the laser gun and looks up to see the giant alien zombie quickly approaching
but the trigger on the alien gun is nowhere to be found")
answer3 = input("What should John do? Choice 1: ditch the gun and run or Choice 2: Shout to
the other survivors for help? Type 1 or 2: ")
if answer3 =="1" :
print("John dropped the alien laser gun and ran into the building with the other frightened
survivors...")



print("Within being in the building for 15 seconds, the giant alien zombie devoured John and
all his group as none of their bullets could stop the alien!")
print("Good luck next try!")
start3()
if answer3 == "2" :
path4_1()

def path4():
words = ["boom", "bang","execute"]
shoot = random.choice(words)
print("John shouts to the other survivors for help....")
print("One of the original members of the group, Ted, a scientist from the secret U.S. military
base Area 51 screamed back at John")
print("There is no trigger! The aliens fire the gun telepathically!")
print("John doesn't have many options, the giant zombie alien is now within 40 yards ")
answer4 = input("What word should John think of to fire the alien laser gun: boom, bang, kill
or execute?: ")

if answer4 == shoot:
print("John focused intensely,", shoot,"...",shoot, "...",shoot)
print("BOOOOOM.....with one shot from the big alien gun, the giant zombie alien reverted
to a pile of burning flesh")
else:
print("hmm it doesen't seem to be working...")
input("What other word can John think of to get the alien laser gun to fire?: ")
if answer4 == shoot:
print("John focused intensley", shoot)
print("BOOOOOM.....with one shot from the big alien gun, the giant zombie alien
reverted to a pile of burning flesh")
print("Congratulations.....you passed level 3!")
path4_1()
else:
print("John realized it was the wrong word right before the giant alien zombie grabbed
him...")



print(shoot)
start3()
start3()
# level 4

import random
def path4_1():
diceRoll = random.randint(1, 6)
print("It looks like you rolled a %d" % diceRoll)
if diceRoll <= 2:
print("The zombies quickly overran the camp and killed everyone including you.")
print("That was very short lived, how about we try that again?")
while True:
path4_1_1 = input("Would you like to retry that? Yes or no? (Y/N): ")
if path4_1_1() not in ('Y', 'N', 'y', 'n'):
print("Invalid input, please try that again.")
continue
else:
break
if path4_1_1 == "Y" or "y":
path4_1()
if path4_1_1 == "N" or "n":
print("Game over, thank you for playing. Maybe you should work on your aim hahaha!")
if diceRoll == 3:
print("Good job, you managed to kill half of the zombies in the horde, but you should work
on your aim...")
if diceRoll >= 4:
print("You wiped out most of the hoard and were able to pick off the stragglers with ease,
nice shooting!")

print("Your party rests at a nearby abandoned camp as you reach Virginia...")
print("Everyone is tired and weary, you yourself can barely stand.")
print()
print("Although its been a hard journey, you can't help but stare at the stolen alien gun in awe!")



print("The architect of the gun is definitely out of this world, it outclasses any technology made
on this Earth.")
print()
print("Just as you start dozing off thinking about the gun, you hear yelling!")
print("There's a horde of aliens coming right for the camp, and these zombies aren't just any
slackers!")
print()
print("You get up from your seat and ponder over the situation, these alien zombies are no
pushovers.")
print("They look much more advanced than the previous horde that was killed, their bodies
having")
print("multiple legs and arms, running faster than Usain Bolt!")
print()
print("You say a small prayer before readying your weapon...")
print()
path4_1_1 = input("Roll the six sided dice in order to see how many zombies are killed. Input 'Y'
to continue: ")
path4_1()
# Level 5

def level5_1():
print("John and the rest of them are really close to the sanctuary in Washington D.C but when
walking")
print("to the entrance of the sanctuary they accidentally walked near a nest of alien eggs with
the parents still there!")
print("You could tell the aliens were agitated... John better act quickly before he's taken out!")
print("Currently you have an alien machine gun and a flame thrower, what are you going to
use?")
print()
firstPath = input("Alien machine gun or Flamethrower?: ")
if firstPath == "Alien machine gun" :
print()
path1()
elif firstPath == "Flamethrower":
print()
path2()


else:
print("Invalid input, please try again!")
level5_1()
def path1_5():
print("You have chosen the Alien machine gun! Good choice, the rate of fire will do some
damage to these damn aliens!")
print("John takes aim at the parents who are quickly making their way at him, readying
themselves to pounce and attack!")
print("Where would you like to fire?")
bodyTarget = input("Head or Leg?: ")
if bodyTarget == "Head":
print()
path5_2()
elif bodyTarget == "Leg":
print("You did minimal damage to the parents who shrugged off the shots like they were
nothing!")
print("They pounced you and murdered your entire squad, you will be forgotten.")
choice = input("Would you like to choose again? (Y/N)")
if choice == "Y":
path1()
else:
print("GAME OVER. Thank you for playing!")
else:
print("Invalid input, please try again!")
path1_5()
def path2():
print("You have chosen the deadly flamethrower, feared by both man and alien!")
print("Unfortunately for you, these aliens are actually invulnurable to flames...")
print("Let's switch back to the machine gun instead.")
path1()
def path5_2() :
print("John took aim at the sprawling alien creatures right for their weakpoint!")
print("The guts and blood of the alien zombie creatures splatter the background and floor,
covering the entire scenery.")
print("Congratulations, you killed the source of the aliens! Thank you for playing Last of
Humanity!")


level5_1()
