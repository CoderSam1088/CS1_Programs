from twilio.rest import Client
import time
from Positivequotelist import choosequote


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

def sendtext(number):
    quotelist=["Successful people don’t become that way overnight."\
           "What most people see at a glance—happiness, wealth, a great career, purpose—is the result of hard work and hustle over time",
           "Your limitation—it’s only your imagination.",
           "Push yourself, because no one else is going to do it for you.",
           "Sometimes later becomes never. Do it now.",
           " Great things never come from comfort zones.",
           "Dream it. Wish it. Do it",
           "Success doesn’t just find you. You have to go out and get it.",
           "The harder you work for something, the greater you’ll feel when you achieve it.",
           "Dream bigger. Do bigger.",
           "Don’t stop when you’re tired. Stop when you’re done.",
           "You’re off to great places, today is your day. Your mountain is waiting, so get on your way",
           "Wake up with determination. Go to bed with satisfaction.",
           "Do something today that your future self will thank you for.",
           "The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty",
           "Don’t Let Yesterday Take Up Too Much Of Today.",
           "All our dreams can come true, if we have the courage to pursue them",
           "The secret of getting ahead is getting started",
           "The best time to plant a tree was 20 years ago. The second best time is now",
           "Only the paranoid survive.",
           "It’s hard to beat a person who never gives up",
           "I wake up every morning and think to myself, ‘how far can I push this company in the next 24 hours",
           "If people are doubting how far you can go, go so far that you can’t hear them anymore.",
           "Write it. Shoot it. Publish it. Crochet it, sauté it, whatever. MAKE",
           "You’ve gotta dance like there’s nobody watching, love like you’ll never be hurt, sing like there’s nobody listening, and live like it’s heaven on earth",
           "Fairy tales are more than true: not because they tell us that dragons exist, but because they tell us that dragons can be beaten",
           "Everything you can imagine is real",
           "Do one thing every day that scares you",
           "It’s no use going back to yesterday, because I was a different person then.",
           "Smart people learn from everything and everyone, average people from their experiences, stupid people already have all the answers",
           "Do what you feel in your heart to be right – for you’ll be criticized anyway.",
           "Happiness is not something ready made. It comes from your own actions.",
           "Whatever you are, be a good one",
           "The same boiling water that softens the potato hardens the egg. It’s what you’re made of. Not the circumstances",
           "If we have the attitude that it’s going to be a great day it usually is",
           "You can either experience the pain of discipline or the pain of regret. The choice is yours.",
           "Impossible is just an opinion.",
           "Your passion is waiting for your courage to catch up",
           "Magic is believing in yourself. If you can make that happen, you can make anything happen.",
           "If something is important enough, even if the odds are stacked against you, you should still do it.",
           "Hold the vision, trust the process.",
           "Don’t be afraid to give up the good to go for the great",
           "People who wonder if the glass is half empty or full miss the point. The glass is refillable",
           "No one is to blame for your future situation but yourself. If you want to be successful, then become Successful",
           "Things may come to those who wait, but only the things left by those who hustle",
           "Everything comes to him who hustles while he waits.",
           "Invest in your dreams. Grind now. Shine later.",
           "Hustlers don’t sleep, they nap.",
           "Greatness only comes before hustle in the dictionary",
           "Without hustle, talent will only carry you so far",
           "Work like there is someone working twenty four hours a day to take it away from you",
           "Hustle in silence and let your success make the noise."]

    chosen=choosequote(quotelist)
    account_sid = 'AC1eff3d503957d76088ec086508d9a572'
    auth_token = 'ef8113f651e90443a38ebbde1b88f6b5'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body=chosen,
             messaging_service_sid='MGf5be1625429d2d0dc63a483ff0061940',
             to='+1' + str(number)
         )

    #print(message.sid)


#print(messaging_service.sid)
