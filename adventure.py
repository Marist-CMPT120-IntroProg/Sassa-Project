#Defining the main function
def main():
    count = 0.0
    name = input("Please enter your name:")
    def intro():
        welcome = (f"Welcome to No Man's Land, {name}!\nThis evening, you will voyage through the backcountry on bike as you make your way home from Big Brook Park. But be careful! You must return before darkness falls, or else the diving bats will emerge and bombard you as you bike along the trail!")
        print(welcome)
        instructions = ("The bike trail runs from north to south, so tell the game which direction you'd like to travel!")
        print(instructions)
    intro()
    list1 = []
    list1.append(input("Enter a valid command:"))
    bigbrook = (f"It's been a long day, {name}. You've had fun at Big Brook Park, with a delicious late afternoon picnic to top it off, but now it's time to make the 7 mile bike ride home. The only issue is that you will need energy to complete the voyage! For this reason, you must stop off at the local coffee shop before they close for the night, and then you may continue with your journey.")
    detail1 = (f"As you begin to leave the park, it's hard not to reflect upon the beauty of the lush meadows and colorful flowers surrounding you.")
    def location1():
        while count == 0:
            if str.lower(list1[0]) == "north":
                print(bigbrook)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail1)
                break
            elif str.lower(list1[0]) == "south":
                print("There are no locations to the south! You must head north on the trail!")
                list1[0] = str.lower(input("Enter a valid command:"))
            elif str.lower(list1[0]) == "help":
                print("The list of valid commands is: North, South, East, West, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
            elif str.lower(list1[0]) == "quit":
                print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
                break
            else:
                print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
    location1()
    count = count + 1
    list1[0] = input("Enter a valid command:")
    coffee = (f"After exiting the park and biking a half mile up the road, you've arrived at the coffee shop in just the nick of time! After ordering a large iced coffee, its time to hit the road on the way to the bike trail.")
    detail2 = (f"The friendly barista wishes you the best of luck as you make your way out the door and back onto your bike.")
    def location2():
        while count == 1.0:
            if str.lower(list1[0]) == "north":
                print(coffee)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail2)
                break
            elif str.lower(list1[0]) == "south":
                print(bigbrook)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail1)
                break
            elif str.lower(list1[0]) == "help":
                print("The list of valid commands is: North, South, East, West, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
            elif str.lower(list1[0]) == "quit":
                print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
                break
            else:
                print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
    location2()
    count = count + 1
    list1[0] = input("Enter a valid command:")
    route = f"To get to the start of the bike trail, you have no choice but to bike along a busy stretch of Route 79. Be careful {name}! It's almost dusk, so visibility is decreasing. There's no sidewalk, as you'll be biking past nothing but farms, so make sure to stay within the shoulder of the road!"
    detail3 = f"Beware, {name}: this part of the trek is a little scary, as you can literally feel the cars rushing on by right next to you!"
    def location3():
        while count == 2.0:
            if str.lower(list1[0]) == "north":
                print(route)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail3)
                break
            elif str.lower(list1[0]) == "south":
                print(coffee)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail2)
                break
            elif str.lower(list1[0]) == "help":
                print("The list of valid commands is: North, South, East, West, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
            elif str.lower(list1[0]) == "quit":
                print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
                break
            else:
                print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
    location3()
    count = count + 1
    list1[0] = input("Enter a valid command:")
    bikehub = f"At long last, you've arrived at the trailhead! Congrats {name}! It's time to complete the bulk of your journey! But wait! One of the tires on your bike feels a little light on air. Luckily, The Bicycle Hub bike shop is located right next to the trailhead! Time to fill up some air in that tire and continue on your journey."
    detail4 = f"The shop is closed, but fortunately you find an air pump laying in the parking lot."
    def location4():
        while count == 3.0:
            if str.lower(list1[0]) == "north":
                print(bikehub)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail4)
                break
            elif str.lower(list1[0]) == "south":
                print(route)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail3)
                break
            elif str.lower(list1[0]) == "help":
                print("The list of valid commands is: North, South, East, West, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
            elif str.lower(list1[0]) == "quit":
                print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
                break
            else:
                print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
    location4()
    count = count + 1
    list1[0] = input("Enter a valid command:")
    airport = (f"Now that your tires are all filled up with air, you begin biking along the paved path in earnest. About a mile into the trail, one of your favorite sunset-watching spots appears on your left adjacent to the trail- the Abandoned Marlboro Airport. And perfect timing, as golden hour has just begun! A brief pitstop on the abandoned tarmac won't hurt, but after snapping a few photos, it's time to get back on the trail!")
    detail5 = (f"Still, you can't help but think about how scenic the sun setting over the large clearing and old tarmac is, even though it's time to move along.")
    def location5():
        while count == 4.0:
            if str.lower(list1[0]) == "north":
                print(airport)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail5)
                break
            elif str.lower(list1[0]) == "south":
                print(bikehub)
                print(bikehub)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail4)
                break
            elif str.lower(list1[0]) == "help":
                print("The list of valid commands is: North, South, East, West, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
            elif str.lower(list1[0]) == "quit":
                print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
                break
            else:
                print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
    location5()
    count = count + 1
    list1[0] = input("Enter a valid command:")
    cemetary = (f"As you continue your ride, the trail winds up cutting directly through a creepy cemetary with a large Mausoleum. Off in the distance, you notice a cult-like group of people in red robes gathered around in a circle. As tempting as it is to check it out, you must continue onward and avoid leaving the trail!")
    detail6 = (f"For a split second, you pull out your phone to record the strange gathering, but then notice the people turning in your direction, prompting you to speed off.")
    def location6():
        while count == 5.0:
            if str.lower(list1[0]) == "north":
                print(cemetary)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail6)
                break
            elif str.lower(list1[0]) == "south":
                print(airport)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail5)
                break
            elif str.lower(list1[0]) == "help":
                print("The list of valid commands is: North, South, East, West, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
            elif str.lower(list1[0]) == "quit":
                print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
                break
            else:
                print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
    location6()
    count = count + 1
    list1[0] = input("Enter a valid command:")
    dirt = (f"Biking fast and furious and feeling slightly terrified after seeing such a weird sighting, you begin to realize that daylight is fading quickly. Luckily, a cut-through exists in the form of dirt-bike trails, which run off of the paved bike trail. The dirt bike trails cut off a significant portion of the journey before rejoining the paved trail later down the line, so it's time to take a detour!")
    detail7 = (f"You feel relieved that your tires are now fully inflated, as they're about to take a beating on the rough terrain of the dirt bike trails.")
    def location7():
        while count == 6.0:
            if str.lower(list1[0]) == "north":
                print(dirt)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail7)
                break
            elif str.lower(list1[0]) == "south":
                print(cemetary)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail6)
                break
            elif str.lower(list1[0]) == "help":
                print("The list of valid commands is: North, South, East, West, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
            elif str.lower(list1[0]) == "quit":
                print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
                break
            else:
                print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
    location7()
    count = count + 1
    list1[0] = input("Enter a valid command:")
    bog = (f"After bumping your way along the rugged dirt bike trails, you finally reemerge onto the glorious pavement. Nice job {name}! But the tricky terrain doesn't end there – mud from the polluted Burnt Fly Bog superfund site has leeched onto a low-lying portion of the bike trail after a recent storm, causing treacherous and slippery conditions. For this portion of the trail, you must walk your bike as a precaution against the dangerous conditions.")
    detail8 = (f"While walking your bike, your white shoes become completely soiled in the muck, but it's better than trying to ride the bike through the muck and risking injury.")
    def location8():
        while count == 7.0:
            if str.lower(list1[0]) == "north":
                print(bog)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail8)
                break
            elif str.lower(list1[0]) == "south":
                print(dirt)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail7)
                break
            elif str.lower(list1[0]) == "help":
                print("The list of valid commands is: North, South, East, West, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
            elif str.lower(list1[0]) == "quit":
                print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
                break
            else:
                print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
    location8()
    count = count + 1  
    list1[0] = input("Enter a valid command:")  
    substation = (f"As you move past the bog and mount back onto your bicycle, you begin to hear the hum of the Freneau electrical substation off in the near distance. You know this means you're in the homestretch! Keep biking as fast as you can – the bats are beginning to emerge!")
    detail9 = (f"The electrical substation is surrounded by a 10-foot high barbed wire fence and high voltage signs, which only add to the eery feel of the bike trail at dusk.")
    def location9():
        while count == 8.0:
            if str.lower(list1[0]) == "north":
                print(substation)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail9)
                break
            elif str.lower(list1[0]) == "south":
                print(bog)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail8)
                break
            elif str.lower(list1[0]) == "help":
                print("The list of valid commands is: North, South, East, West, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
            elif str.lower(list1[0]) == "quit":
                print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
                break
            else:
                print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
    location9()
    count = count + 1
    list1[0] = input("Enter a valid command:")
    shack = (f"As you near the end of the bike trail, there's one last landmark to pass! On your righthand side, you see it coming closer and closer: The creepy abandoned shack! As the purple graffiti of the shack gets closer and closer, a strange man emerges and runs towards the trail! Luckily you're able to slip past him just in time and make your way home!")
    detail10 = (f"The man is old with white hair, but you end up biking past him so fast that you're not able to get a good look at him or his face.")
    def location10():
        while count == 9.0:
            if str.lower(list1[0]) == "north":
                print(shack)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail10)
                break
            elif str.lower(list1[0]) == "south":
                print(substation)
                enter1 = input("Press Enter to Examine Location")
                print(enter1)
                print(detail9)
                break
            elif str.lower(list1[0]) == "help":
                print("The list of valid commands is: North, South, East, West, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
            elif str.lower(list1[0]) == "quit":
                print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
                break
            else:
                print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
                list1[0] = str.lower(input("Enter a valid command:"))
    location10()
    count = count + 1
    def ending():
        enter = input("Press Enter to continue")
        congrats = (f"Congrats {name}! After a long journey of {count} stops, it's finally time to exit the bike trail and cruise on home through your neighborhood! You're definitely gonna sleep well tonight!")
        print(enter)
        print(congrats)
    ending()
main()