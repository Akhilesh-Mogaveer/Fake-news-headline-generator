import random

place = ["Mumbai"," Delhi","Banglore","Kolkata","Chennai","Hyderabad","Pune","Ahmedabad","Goa","Kerala","TamilNadu","Karnataka"]
normal_actions = ["visits a local market","attends a wedding","goes for a morning walk","enjoys street food","reads a book in the park",
    "travels by metro","meets old friends","celebrates a festival","takes a selfie with fans","shops at a mall"]

def celeb():
    celebrities = ["Shah Rukh Khan","Priyanka Chopra","Deepika Padukone","Alia Bhatt","Amitabh Bachchan"]
    celebrities_actions = ["announces a new movie","hosts a grand event","launches a fashion brand","wins an international award","donates to charity"]
    sub1 = random.choice(celebrities)
    acction1 = random.choice(celebrities_actions)
    place1 = random.choice(place)
    return f"\033[1m Breaking news: {sub1} {acction1} in {place1}\033[om"

def sport():
    sportspersons = ["Virat Kohli","MS Dhoni","Sachin Tendulkar","PV Sindhu","Neeraj Chopra","Rohit-Sharma"]
    sportspersons_actions = ["breaks a world record","wins a gold medal","announces retirement","launches a sports academy","becomes team captain"]
    sub2 = random.choice(sportspersons)
    action2 = random.choice(sportspersons_actions)
    place2 = random.choice(place)
    return f"\033[1m Breaking news: {sub2} {action2} in {place2}\033[0m"

def politics():
    politicians = ["Narendra Modi","Rahul Gandhi","Amit Shah","Mamata Banerjee","Arvind Kejriwal"]
    politicians_actions = ["launches a new policy","addresses the nation","wins an election","inaugurates a project","meets world leaders"]
    sub3 = random.choice(politicians)
    action3 = random.choice(politicians_actions)
    place3 = random.choice(place)
    return f"\033[1m Breaking news: {sub3} {action3} in {place3}\033[0m"

def save(headline):
    with open("headline.txt", "a") as f:
        f.write(headline + "\n")
    print("Headline saved to headline.txt")

def ask_save(headline):
    s = input("Do you want to save the headline?(yes/no)")
    if(s == "yes"):
        save(headline)

def news():
    choose = input("Do you have any suggestions to create news on? (yes/no)").lower()
    if(choose == "yes"):
        manually = input("Do you want to create a Headline manually? (yes/no)").lower()
        if( manually == "yes"):
            action = input("Enter the headline:")
            print(f"\033[1m Breaking news:  {action}\033[om")
            ask_save(action)
                
        else:
            who = input("Tell the name of that person:")
            default = random.choice(normal_actions)
            p = random.choice(place)
            headline = f"\033[1m Breaking news: {who} {default} in {p}\033[0m "
            print(headline)
            ask_save(headline)
            
    else:
        cat = input("choose on whom you want to create headline.(celebrities/sportsperons/politicians)").lower()
        if( cat == "celebrities"):
            headline  = celeb()
            print(headline)
            ask_save(headline)

        elif( cat == "sportspersons"):    
            headline = sport()
            print(headline)
            ask_save(headline)
            
        else:
            headline = politics()
            print(headline)
            ask_save(headline)

news()

repeat = input("Do you want to create another headline? (yes/no)")
while repeat == "yes":
    news()
    repeat = input("Do you want to create another headline? (yes/no)")
