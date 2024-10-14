import string

print("Bienvenue dans l'auction ventes aux enchères :\n")

alphabet = list(string.ascii_letters)
name_bid_auction = {}

while True:
    name = input("Name please :\n")
    
    # Validate the name to ensure it contains only alphabetic characters
    if all(c in alphabet for c in name):
        
        bid_number = input("Votre offre, s'il vous plaît :\n")
        
        # Validate that the bid is a valid number
        if bid_number.isdigit():
            bid = int(bid_number)
            name_bid_auction[name] = bid
        else:
            print("Offre invalide, veuillez entrer un numéro.")
    else:
        print("Nom invalide, veuillez entrer un nom alphabétique.")
    
    # Ask if there's another bidder
    other_bid = input(f"Y a-t-il une autre personne qui souhaite enchérir 'oui' ou 'non' ? \n "+"\n"*20).lower()
    
    if other_bid == 'oui':  # Handle French 'yes' response
        continue
    else:
        print("Merci d'avoir participé à l'événement et voici l'heureux gagnant de la soiree.")
        max_bid =0
        gagnant =""
        for name,bid in name_bid_auction.items():
            if bid >max_bid:
                max_bid =bid
                gagnant=name
        
        print(f"L'heureux gagnant est {gagnant} avec une offre de {max_bid} euros.")
        print("Les offres placées sont :", name_bid_auction)
        break

a="""
Once in a while, I like to share the random thoughts and opportunities on my mind.

So... here are two random thoughts and two random opportunities...

Random thought #1: I had a dream last night that I went into outer space and met aliens from different timelines.

One alien was from 700 years in the future, where humans lived on giant ships in outer space.

They created their own countries and colonies on ships that floated around the earth.

They looked like humans but lived in outer space.

The second alien was more "alien-like" and was from thousands of years in the future.

As humans evolved, they created smaller bodies and bigger brains and big eyes as they lived further and further from earth.

They plugged their brains into the cloud and created their own universes.

It was a weird dream, but this is actually my best theory about aliens - they are just future humans.

Random thought #2. I see AI and making entrepreneurs worse, not better.

I've noticed that businesses and brands are getting worse at marketing.

AI should make marketing easier, but instead, they are using it to do everything at a "just OK" level.

The ability to write copy... or do good customer service... or get reviews... is kind of a lost art now.

Instead of automating everything, do it the hard way first.

Then automate what works.

OK, now for two random opportunities...

Random opportunity #1: In four weeks, I am hosting a mastermind in Austin, TX.

We will be joined by Whole Foods founder John Mackey, as well as hosting chef made meals and a roundtable mastermind.

If you'd like to come, you can request an invitation through this link.

Our masterminds are a mix of fun, business, and networking, and it is common for people to find their next partner, mastermind friend, or investor at our meetups.

Access for the entire year is $7500, but you can "test out" a single event for $2500.

These are the best (and most fun) way to build a relationship with me and the rest of the Capitalism community.

Random opportunity #2: I'm starting an investment newsletter, mostly for fun.

I'm not an investing expert, but I have been learning a lot over the last two years.

I got my arse handed to me in the COVID-era, and I was determined to learn from my mistakes.

While my peers were predicting hyperinflation and the Fourth Turning, I noticed that markets continued to reach new all-time highs.

That's when I got serious about developing a sound investment thesis with a long-term focus.

I've learned to ignore the noise and the "hot takes" and just follow a sound long-term strategy.

Writing about things forces me to organize my thoughts and mindsets, and I've learned a lot about investing the last few years.

I also might share some of the private deal flow that comes my way... we'll see.

Anyway, this is separate from my primary business of helping entrepreneurs, so it will have a separate opt-in and form and follow up process.

If you want to be on the waiting list for when the newsletter comes out, you can get access to it here.

OK, there ya go...

There's two random thoughts and two opportunities.

Have a wonderful weekend.

Ryan
P.S. Since AI making entrepreneurs worse, I think ecommerce is getting easier.

I'm really stunned by the results that we are getting right now, because most people just won't do the work.

They would rather automate or use AI to do something, so their quality of work is low.

The market is expanding, but the competition is weak.

It's honestly... kind of weird.

Or maybe... our processes are just getting better.

Either way, this is my way of inviting you to lean into the opportunities to start a business right now.

The "getting" is really good right now, because most people are just unwilling to dive into the opportunities that exist.

Whenever you are ready to plant seeds for your 7-figure business, you can apply to work with us on your Road to $1 Million.


   
"""

print(a)