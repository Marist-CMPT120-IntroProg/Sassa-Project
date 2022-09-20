#Defining the main function
def main():
    def intro():
        welcome = f"Welcome to No Man's Land!\nThis evening, you will voyage through the backcountry on bike as you make your way home from Big Brook Park. But be careful! You must return before darkness falls, or else the diving bats will emerge and bombard you as you bike along the trail!"
        print(welcome)
    intro()
    def location1():
        enter = input("Press Enter to continue")
        bigbrook = f"It's been a long day of fun at Big Brook Park, with a delicious late afternoon picnic to top it off, but now it's time to make the 7 mile bike ride home. The only issue is that you will need energy to complete the voyage! For this reason, you must stop off at the local coffee shop before they close for the night, and then you may continue with your journey."
        print(enter)
        print(bigbrook)
    location1()
    def location2():
        enter = input("Press Enter to continue")
        coffee = f"After exiting the park and biking a half mile up the road, you've arrived at the coffee shop in just the nick of time! After ordering a large iced coffee, its time to hit the road on the way to the bike trail."
        print(enter)
        print(coffee)
    location2()
    def location3():
        enter = input("Press Enter to continue")
        route = f"To get to the start of the bike trail, you have no choice but to bike along a busy stretch of Route 79. Be careful! It's almost dusk, so visibility is decreasing. There's no sidewalk, as you'll be biking past nothing but farms, so make sure to stay within the shoulder of the road!"
        print(enter)
        print(route)
    location3()
    def location4():
        enter = input("Press Enter to continue")
        bikehub = f"At long last, you've arrived at the trailhead! It's time to complete the bulk of your journey! But wait! One of the tires on your bike feels a little light on air. Luckily, The Bicycle Hub bike shop is located right next to the trailhead! Time to fill up some air in that tire and continue on your journey."
        print(enter)
        print(bikehub)
    location4()
    def location5():
        enter = input("Press Enter to continue")
        airport = f"Now that your tires are all filled up with air, you begin biking along the paved path in earnest. About a mile into the trail, one of your favorite sunset-watching spots appears on your left adjacent to the trail- the Abandoned Marlboro Airport. And perfect timing, as golden hour has just begun! A brief pitstop on the abandoned tarmac won't hurt, but after snapping a few photos, it's time to get back on the trail!"
        print(enter)
        print(airport)
    location5()
    def location6():
        enter = input("Press Enter to continue")
        cemetary = f"As you continue your ride, the trail winds up cutting directly through a creepy cemetary with a large Mausoleum. Off in the distance, you notice a cult-like group of people in red robes gathered around in a circle. As tempting as it is to check it out, you must continue onward and avoid leaving the trail!"
        print(enter)
        print(cemetary)
    location6()
    def location7():
        enter = input("Press Enter to continue")
        dirt = f"Biking fast and furious and feeling slightly terrified after seeing such a weird sighting, you begin to realize that daylight is fading quickly. Luckily, a cut-through exists in the form of dirt-bike trails, which run off of the paved bike trail. The dirt bike trails cut off a significant portion of the journey before rejoining the paved trail later down the line, so it's time to take a detour!"
        print(enter)
        print(dirt)
    location7()
    def location8():
        enter = input("Press Enter to continue")
        bog = f"After bumping your way along the rugged dirt bike trails, you finally reemerge onto the glorious pavement. But the tricky terrain doesn't end there – mud from the polluted Burnt Fly Bog superfund site has leeched onto a low-lying portion of the bike trail after a recent storm, causing treacherous and slippery conditions. For this portion of the trail, you must walk your bike as a precaution against the dangerous conditions."
        print(enter)
        print(bog)
    location8()    
    def location9():
        enter = input("Press Enter to continue")
        substation = f"As you move past the bog and mount back onto your bicycle, you begin to hear the hum of the Freneau electrical substation off in the near distance. You know this means you're in the homestretch! Keep biking as fast as you can – the bats are beginning to emerge!"
        print(enter)
        print(substation)
    location9()
    def location10():
        enter = input("Press Enter to continue")
        shack = f"As you near the end of the bike trail, there's one last landmark to pass! On your righthand side, you see it coming closer and closer: The creepy abandoned shack! As the purple graffiti of the shack gets closer and closer, a strange man emerges and runs towards the trail! Luckily you're able to slip past him just in time and make your way home!"
        print(enter)
        print(shack)
    location10()
    def ending():
        enter = input("Press Enter to continue")
        congrats = f"Congrats! After a long journey, it's finally time to exit the bike trail and cruise on home through your neighborhood! You're definitely gonna sleep well tonight!"
        print(enter)
        print(congrats)
    ending()
main()
