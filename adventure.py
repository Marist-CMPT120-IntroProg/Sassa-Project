#Defining the main function
def main():
    #initalizing count to zero
    count = 0.0
    #asking for name so it can be included throughout the text to satisfy commit #1 requirements
    name = input("Please enter your name:")
    def intro():
        welcome = (f"Welcome to No Man's Land, {name}!\nThis evening, you will voyage through the backcountry on bike as you make your way home from Big Brook Park. But be careful! You must return before darkness falls, or else the diving bats will emerge and bombard you as you bike along the trail!")
        print(welcome)
        instructions = ("The bike trail runs from north to south, so tell the game which direction you'd like to travel!")
        print(instructions)
    intro()
    #creating a list to hold the command so that the program can interperet what is said
    list1 = []
    #adding the first command to the empty list
    list1.append(input("Enter a valid command:"))
    #creating a list of dictionaries to store each location and its accompanying location data
    locationsList = [{"location": "Big Brook Park", "summary": f"It's been a long day, {name}. You've had fun at Big Brook Park, with a delicious late afternoon picnic to top it off, but now it's time to make the 7 mile bike ride home. The only issue is that you will need energy to complete the voyage! For this reason, you must stop off at the local coffee shop before they close for the night, and then you may continue with your journey.", "details": f"As you begin to leave the park, it's hard not to reflect upon the beauty of the lush meadows and colorful flowers surrounding you.", "was_visited": False},
    {"location": "Coffee Shop", "summary": "After exiting the park and biking a half mile up the road, you've arrived at the coffee shop in just the nick of time! After ordering a large iced coffee, its time to hit the road on the way to the bike trail.", "details": "The friendly barista wishes you the best of luck as you make your way out the door and back onto your bike.", "was_visited": False},
    {"location": "Route 79", "summary": f"To get to the start of the bike trail, you have no choice but to bike along a busy stretch of Route 79. Be careful {name}! It's almost dusk, so visibility is decreasing. There's no sidewalk, as you'll be biking past nothing but farms, so make sure to stay within the shoulder of the road!", "details": f"Beware, {name}: this part of the trek is a little scary, as you can literally feel the cars rushing on by right next to you!", "was_visited": False},
    {"location": "Bike Hub", "summary": f"At long last, you've arrived at the trailhead! Congrats {name}! It's time to complete the bulk of your journey! But wait! One of the tires on your bike feels a little light on air. Luckily, The Bicycle Hub bike shop is located right next to the trailhead! Time to fill up some air in that tire and continue on your journey.", "details": f"The shop is closed, but fortunately you find an air pump laying in the parking lot.", "was_visited": False},
    {"location": "Airport", "summary": "Now that your tires are all filled up with air, you begin biking along the paved path in earnest. About a mile into the trail, one of your favorite sunset-watching spots appears on your left adjacent to the trail- the Abandoned Marlboro Airport. And perfect timing, as golden hour has just begun! A brief pitstop on the abandoned tarmac won't hurt, but after snapping a few photos, it's time to get back on the trail!", "details": "Still, you can't help but think about how scenic the sun setting over the large clearing and old tarmac is, even though it's time to move along.", "was_visited": False},
    {"location": "Cemetary", "summary": "As you continue your ride, the trail winds up cutting directly through a creepy cemetary with a large Mausoleum. Off in the distance, you notice a cult-like group of people in red robes gathered around in a circle. As tempting as it is to check it out, you must continue onward and avoid leaving the trail!", "details": "For a split second, you pull out your phone to record the strange gathering, but then notice the people turning in your direction, prompting you to speed off.", "was_visited": False},
    {"location": "Dirt Bike Trails", "summary": "Biking fast and furious and feeling slightly terrified after seeing such a weird sighting, you begin to realize that daylight is fading quickly. Luckily, a cut-through exists in the form of dirt-bike trails, which run off of the paved bike trail. The dirt bike trails cut off a significant portion of the journey before rejoining the paved trail later down the line, so it's time to take a detour!", "details": "You feel relieved that your tires are now fully inflated, as they're about to take a beating on the rough terrain of the dirt bike trails.", "was_visited": False}, 
    {"location": "The Bog", "summary": f"After bumping your way along the rugged dirt bike trails, you finally reemerge onto the glorious pavement. Nice job {name}! But the tricky terrain doesn't end there – mud from the polluted Burnt Fly Bog superfund site has leeched onto a low-lying portion of the bike trail after a recent storm, causing treacherous and slippery conditions. For this portion of the trail, you must walk your bike as a precaution against the dangerous conditions.", "details": "While walking your bike, your white shoes become completely soiled in the muck, but it's better than trying to ride the bike through the muck and risking injury.", "was_visited": False},
    {"location": "Substation", "summary": "As you move past the bog and mount back onto your bicycle, you begin to hear the hum of the Freneau electrical substation off in the near distance. You know this means you're in the homestretch! Keep biking as fast as you can – the bats are beginning to emerge!", "details": "The electrical substation is surrounded by a 10-foot high barbed wire fence and high voltage signs, which only add to the eery feel of the bike trail at dusk.", "was_visited": False},
    {"location": "Shack", "summary": "As you near the end of the bike trail, there's one last landmark to pass! On your righthand side, you see it coming closer and closer: The creepy abandoned shack! As the purple graffiti of the shack gets closer and closer, a strange man emerges and runs towards the trail! Luckily you're able to slip past him just in time and make your way home!", "details": "The man is old with white hair, but you end up biking past him so fast that you're not able to get a good look at him or his face.", "was_visited": False}]
    while locationsList[0]["was_visited"] == False:
        #making sure the command is interpreted as a string and eliminating case-sensitive
        if str.lower(list1[0]) == "north":
            current_location = locationsList[0]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[0]["details"])
            locationsList[0]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "south":
            print("There are no locations to the south and you have not yet arrived at the first location, so you must must head north on the trail!")
            list1[0] = str.lower(input("Enter a valid command:"))
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "help":
            print("The list of valid commands is: North, South, Help, and Quit")
            list1[0] = str.lower(input("Enter a valid command:"))
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "quit":
            print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
            break
        else:
            print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
            #giving the user a chance to re-enter a valid command
            list1[0] = str.lower(input("Enter a valid command:"))
    #increase location count by 1 after the first stop
    count = count + 1
    #replacing command in the list with a new command to be interpreted by the next while-loop
    list1[0] = input("Enter a valid command:")
    while locationsList[0]["was_visited"] == True:
        #making sure the command is interpreted as a string and eliminating case-sensitive
        if str.lower(list1[0]) == "north":
            current_location = locationsList[1]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[1]["details"])
            locationsList[0]["was_visited"] = False
            locationsList[1]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "south":
            print("There are no locations to the south, so you will have to stay here!")
            current_location = locationsList[0]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[0]["details"])
            list1[0] = str.lower(input("Enter a valid command:"))
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "help":
            print("The list of valid commands is: North, South, Help, and Quit")
            list1[0] = str.lower(input("Enter a valid command:"))
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "quit":
            print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
            break
        else:
            print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
            #giving the user a chance to re-enter a valid command
            list1[0] = str.lower(input("Enter a valid command:"))
    #increase location count by 1 after the next stop
    count = count + 1
    #replacing command in the list with a new command to be interpreted by the next while-loop
    list1[0] = input("Enter a valid command:")
    while locationsList[1]["was_visited"] == True:
        #making sure the command is interpreted as a string and eliminating case-sensitive
        if str.lower(list1[0]) == "north":
            current_location = locationsList[2]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[2]["details"])
            locationsList[1]["was_visited"] = False
            locationsList[2]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "south":
            current_location = locationsList[0]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[0]["details"])
            locationsList[1]["was_visited"] = False
            locationsList[0]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "help":
            print("The list of valid commands is: North, South, Help, and Quit")
            list1[0] = str.lower(input("Enter a valid command:"))
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "quit":
            print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
            break
        else:
            print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
            #giving the user a chance to re-enter a valid command
            list1[0] = str.lower(input("Enter a valid command:"))
    #increase location count by 1 after the next stop
    count = count + 1
    #replacing command in the list with a new command to be interpreted by the next while-loop
    list1[0] = input("Enter a valid command:")
    while locationsList[2]["was_visited"] == True:
        #making sure the command is interpreted as a string and eliminating case-sensitive
        if str.lower(list1[0]) == "north":
            current_location = locationsList[3]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[3]["details"])
            locationsList[2]["was_visited"] = False
            locationsList[3]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "south":
            current_location = locationsList[1]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[1]["details"])
            locationsList[2]["was_visited"] = False
            locationsList[1]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "help":
            print("The list of valid commands is: North, South, Help, and Quit")
            list1[0] = str.lower(input("Enter a valid command:"))
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "quit":
            print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
            break
        else:
            print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
            #giving the user a chance to re-enter a valid command
            list1[0] = str.lower(input("Enter a valid command:"))
    #increase location count by 1 after the next stop
    count = count + 1
    #replacing command in the list with a new command to be interpreted by the next while-loop
    list1[0] = input("Enter a valid command:")
    while locationsList[3]["was_visited"] == True:
        #making sure the command is interpreted as a string and eliminating case-sensitive
        if str.lower(list1[0]) == "north":
            current_location = locationsList[4]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[4]["details"])
            locationsList[3]["was_visited"] = False
            locationsList[4]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "south":
            current_location = locationsList[2]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[2]["details"])
            locationsList[3]["was_visited"] = False
            locationsList[2]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "help":
            print("The list of valid commands is: North, South, Help, and Quit")
            list1[0] = str.lower(input("Enter a valid command:"))
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "quit":
            print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
            break
        else:
            print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
            #giving the user a chance to re-enter a valid command
            list1[0] = str.lower(input("Enter a valid command:"))
    #increase location count by 1 after the next stop
    count = count + 1
    #replacing command in the list with a new command to be interpreted by the next while-loop
    list1[0] = input("Enter a valid command:")
    while locationsList[4]["was_visited"] == True:
        #making sure the command is interpreted as a string and eliminating case-sensitive
        if str.lower(list1[0]) == "north":
            current_location = locationsList[5]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[5]["details"])
            locationsList[4]["was_visited"] = False
            locationsList[5]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "south":
            current_location = locationsList[3]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[3]["details"])
            locationsList[4]["was_visited"] = False
            locationsList[3]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "help":
            print("The list of valid commands is: North, South, Help, and Quit")
            list1[0] = str.lower(input("Enter a valid command:"))
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "quit":
            print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
            break
        else:
            print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
            #giving the user a chance to re-enter a valid command
            list1[0] = str.lower(input("Enter a valid command:"))
    #increase location count by 1 after the next stop
    count = count + 1
    #replacing command in the list with a new command to be interpreted by the next while-loop
    list1[0] = input("Enter a valid command:")
    while locationsList[5]["was_visited"] == True:
        #making sure the command is interpreted as a string and eliminating case-sensitive
        if str.lower(list1[0]) == "north":
            current_location = locationsList[6]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[6]["details"])
            locationsList[5]["was_visited"] = False
            locationsList[6]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "south":
            current_location = locationsList[4]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[4]["details"])
            locationsList[5]["was_visited"] = False
            locationsList[4]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "help":
            print("The list of valid commands is: North, South, Help, and Quit")
            list1[0] = str.lower(input("Enter a valid command:"))
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "quit":
            print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
            break
        else:
            print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
            #giving the user a chance to re-enter a valid command
            list1[0] = str.lower(input("Enter a valid command:"))
    #increase location count by 1 after the next stop
    count = count + 1
    #replacing command in the list with a new command to be interpreted by the next while-loop
    list1[0] = input("Enter a valid command:")
    while locationsList[6]["was_visited"] == True:
        #making sure the command is interpreted as a string and eliminating case-sensitive
        if str.lower(list1[0]) == "north":
            current_location = locationsList[7]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[7]["details"])
            locationsList[6]["was_visited"] = False
            locationsList[7]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "south":
            current_location = locationsList[5]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[5]["details"])
            locationsList[6]["was_visited"] = False
            locationsList[5]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "help":
            print("The list of valid commands is: North, South, Help, and Quit")
            list1[0] = str.lower(input("Enter a valid command:"))
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "quit":
            print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
            break
        else:
            print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
            #giving the user a chance to re-enter a valid command
            list1[0] = str.lower(input("Enter a valid command:"))
    #increase location count by 1 after the next stop
    count = count + 1 
    #replacing command in the list with a new command to be interpreted by the next while-loop 
    list1[0] = input("Enter a valid command:")  
    while locationsList[7]["was_visited"] == True:
        #making sure the command is interpreted as a string and eliminating case-sensitive
        if str.lower(list1[0]) == "north":
            current_location = locationsList[8]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[8]["details"])
            locationsList[7]["was_visited"] = False
            locationsList[8]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "south":
            current_location = locationsList[6]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[6]["details"])
            locationsList[7]["was_visited"] = False
            locationsList[6]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "help":
            print("The list of valid commands is: North, South, Help, and Quit")
            list1[0] = str.lower(input("Enter a valid command:"))
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "quit":
            print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
            break
        else:
            print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
            #giving the user a chance to re-enter a valid command
            list1[0] = str.lower(input("Enter a valid command:"))
    #increase location count by 1 after the next stop
    count = count + 1
    #replacing command in the list with a new command to be interpreted by the next while-loop
    list1[0] = input("Enter a valid command:")
    while locationsList[8]["was_visited"] == True:
        #making sure the command is interpreted as a string and eliminating case-sensitive
        if str.lower(list1[0]) == "north":
            current_location = locationsList[9]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[9]["details"])
            locationsList[8]["was_visited"] = False
            locationsList[9]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "south":
            current_location = locationsList[7]["summary"]
            print(current_location)
            #Revealing deatils by prompting the user to examine the location (as per commit 5)
            enter1 = input("Press Enter to Examine Location")
            print(enter1)
            print(locationsList[7]["details"])
            locationsList[8]["was_visited"] = False
            locationsList[7]["was_visited"] = True
            break
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "help":
            print("The list of valid commands is: North, South, Help, and Quit")
            list1[0] = str.lower(input("Enter a valid command:"))
        #making sure the command is interpreted as a string and eliminating case-sensitive
        elif str.lower(list1[0]) == "quit":
            print(f"You've chosen quit the game, {name}! Copyright Luke Sassa, 2022")
            break
        else:
            print("You've entered an invalid command! The list of valid commands is: North, South, Help, and Quit")
            #giving the user a chance to re-enter a valid command
            list1[0] = str.lower(input("Enter a valid command:"))
    #increase location count by 1 after the next stop
    count = count + 1
    def ending():
        enter = input("Press Enter to continue")
        congrats = (f"Congrats {name}! After a long journey of {count} stops, it's finally time to exit the bike trail and cruise on home through your neighborhood! You're definitely gonna sleep well tonight!")
        print(enter)
        print(congrats)
    ending()
main()