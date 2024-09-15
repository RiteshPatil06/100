#Higher or Lower
import random
data = [
    {"name": "Cristiano Ronaldo", "followers": 589, "description": "Football player", "country": "Portugal"},
    {"name": "Kylie Jenner", "followers": 382, "description": "Reality TV", "country": "USA"},
    {"name": "Lionel Messi", "followers": 470, "description": "Football player", "country": "Argentina"},
    {"name": "Selena Gomez", "followers": 410, "description": "Singer, actress", "country": "USA"},
    {"name": "Dwayne Johnson", "followers": 378, "description": "Actor, wrestler", "country": "USA"},
    {"name": "Ariana Grande", "followers": 368, "description": "Singer, actress", "country": "USA"},
    {"name": "Kim Kardashian", "followers": 352, "description": "Reality TV", "country": "USA"},
    {"name": "Beyoncé", "followers": 302, "description": "Singer, actress", "country": "USA"},
    {"name": "Khloé Kardashian", "followers": 298, "description": "Reality TV", "country": "USA"},
    {"name": "Nike", "followers": 293, "description": "Sportswear brand", "country": "USA"},
    {"name": "Kendall Jenner", "followers": 279, "description": "Model, TV", "country": "USA"},
    {"name": "Justin Bieber", "followers": 276, "description": "Singer", "country": "Canada"},
    {"name": "National Geographic", "followers": 265, "description": "Media organization", "country": "USA"},
    {"name": "Taylor Swift", "followers": 253, "description": "Singer", "country": "USA"},
    {"name": "Virat Kohli", "followers": 241, "description": "Cricketer", "country": "India"},
    {"name": "Jennifer Lopez", "followers": 239, "description": "Singer, actress", "country": "USA"},
    {"name": "Nicki Minaj", "followers": 213, "description": "Rapper", "country": "Trinidad and Tobago"},
    {"name": "Kourtney Kardashian", "followers": 218, "description": "Reality TV", "country": "USA"},
    {"name": "Neymar", "followers": 206, "description": "Football player", "country": "Brazil"},
    {"name": "Miley Cyrus", "followers": 199, "description": "Singer, actress", "country": "USA"},
    {"name": "Katy Perry", "followers": 195, "description": "Singer", "country": "USA"},
    {"name": "Kevin Hart", "followers": 166, "description": "Comedian, actor", "country": "USA"},
    {"name": "Ellen DeGeneres", "followers": 129, "description": "TV host", "country": "USA"},
    {"name": "Real Madrid CF", "followers": 129, "description": "Football club", "country": "Spain"},
    {"name": "FC Barcelona", "followers": 117, "description": "Football club", "country": "Spain"},
    {"name": "Rihanna", "followers": 146, "description": "Singer, entrepreneur", "country": "Barbados"},
    {"name": "Demi Lovato", "followers": 146, "description": "Singer, actress", "country": "USA"},
    {"name": "Victoria's Secret", "followers": 75, "description": "Lingerie brand", "country": "USA"},
    {"name": "Zendaya", "followers": 163, "description": "Actress, singer", "country": "USA"},
    {"name": "Shakira", "followers": 86, "description": "Singer", "country": "Colombia"},
    {"name": "Drake", "followers": 133, "description": "Rapper, singer", "country": "Canada"},
    {"name": "Chris Brown", "followers": 131, "description": "Singer", "country": "USA"},
    {"name": "LeBron James", "followers": 141, "description": "Basketball player", "country": "USA"},
    {"name": "Vin Diesel", "followers": 84, "description": "Actor", "country": "USA"},
    {"name": "Cardi B", "followers": 149, "description": "Rapper", "country": "USA"},
    {"name": "David Beckham", "followers": 75, "description": "Former footballer", "country": "England"},
    {"name": "Billie Eilish", "followers": 108, "description": "Singer", "country": "USA"},
    {"name": "Justin Timberlake", "followers": 69, "description": "Singer, actor", "country": "USA"},
    {"name": "UEFA Champions League", "followers": 98, "description": "Football tournament", "country": "Europe"},
    {"name": "NASA", "followers": 87, "description": "Space agency", "country": "USA"},
    {"name": "Emma Watson", "followers": 67, "description": "Actress", "country": "UK"},
    {"name": "Shawn Mendes", "followers": 71, "description": "Singer", "country": "Canada"},
    {"name": "Gigi Hadid", "followers": 76, "description": "Model", "country": "USA"},
    {"name": "Priyanka Chopra", "followers": 85, "description": "Actress", "country": "India"},
    {"name": "9GAG", "followers": 57, "description": "Media platform", "country": "Hong Kong"},
    {"name": "Ronaldinho", "followers": 69, "description": "Former footballer", "country": "Brazil"},
    {"name": "Maluma", "followers": 63, "description": "Singer", "country": "Colombia"},
    {"name": "Camila Cabello", "followers": 66, "description": "Singer", "country": "Cuba"},
    {"name": "NBA", "followers": 74, "description": "Basketball league", "country": "USA"},
    {"name": "Deepika Padukone", "followers": 71, "description": "Actress", "country": "India"},
    {"name": "Will Smith", "followers": 64, "description": "Actor", "country": "USA"},
    {"name": "Shawn Mendes", "followers": 71, "description": "Singer", "country": "Canada"},
    {"name": "Anitta", "followers": 63, "description": "Singer", "country": "Brazil"},
    {"name": "Juventus", "followers": 55, "description": "Football club", "country": "Italy"},
    {"name": "Zac Efron", "followers": 56, "description": "Actor", "country": "USA"},
    {"name": "Lele Pons", "followers": 49, "description": "Internet celebrity", "country": "Venezuela"},
    {"name": "Marcelo", "followers": 54, "description": "Football player", "country": "Brazil"},
    {"name": "Wiz Khalifa", "followers": 38, "description": "Rapper", "country": "USA"},
    {"name": "Gareth Bale", "followers": 49, "description": "Football player", "country": "Wales"},
    {"name": "Dua Lipa", "followers": 87, "description": "Singer", "country": "UK"},
    {"name": "Snoop Dogg", "followers": 76, "description": "Rapper", "country": "USA"},
    {"name": "Khaby Lame", "followers": 79, "description": "Social media", "country": "Italy"},
    {"name": "Kylian Mbappé", "followers": 97, "description": "Football player", "country": "France"},
    {"name": "Adele", "followers": 52, "description": "Singer", "country": "UK"},
    {"name": "Millie Bobby Brown", "followers": 62, "description": "Actress", "country": "UK"},
    {"name": "Bella Hadid", "followers": 58, "description": "Model", "country": "USA"},
    {"name": "Karim Benzema", "followers": 66, "description": "Football player", "country": "France"},
    {"name": "Lil Wayne", "followers": 16, "description": "Rapper", "country": "USA"},
    {"name": "Disha Patani", "followers": 57, "description": "Actress", "country": "India"},
    {"name": "Shraddha Kapoor", "followers": 78, "description": "Actress", "country": "India"},
    {"name": "Alia Bhatt", "followers": 76, "description": "Actress", "country": "India"},
    {"name": "Neha Kakkar", "followers": 74, "description": "Singer", "country": "India"},
    {"name": "Jacqueline Fernandez", "followers": 65, "description": "Actress", "country": "Sri Lanka"},
    {"name": "Anushka Sharma", "followers": 64, "description": "Actress", "country": "India"},
    {"name": "Akshay Kumar", "followers": 64, "description": "Actor", "country": "India"},
    {"name": "Katrina Kaif", "followers": 70, "description": "Actress", "country": "UK"},
    {"name": "Ranveer Singh", "followers": 43, "description": "Actor", "country": "India"},
    {"name": "Varun Dhawan", "followers": 45, "description": "Actor", "country": "India"},
    {"name": "Narendra Modi", "followers": 76, "description": "Indian PM", "country": "India"},
    {"name": "Hrithik Roshan", "followers": 46, "description": "Actor", "country": "India"},
    {"name": "Shahid Kapoor", "followers": 42, "description": "Actor", "country": "India"},
    {"name": "Yo Yo Honey Singh", "followers": 13, "description": "Rapper", "country": "India"},
    {"name": "Guru Randhawa", "followers": 33, "description": "Singer", "country": "India"},
    {"name": "Kriti Sanon", "followers": 53, "description": "Actress", "country": "India"},
    {"name": "Sunny Leone", "followers": 54, "description": "Actress", "country": "Canada"},
    {"name": "Sonam Kapoor", "followers": 34, "description": "Actress", "country": "India"},
    {"name": "Hardik Pandya", "followers": 25, "description": "Cricketer", "country": "India"},
    {"name": "Diljit Dosanjh", "followers": 14, "description": "Singer, actor", "country": "India"},
    {"name": "Kapil Sharma", "followers": 42, "description": "Comedian", "country": "India"},
    {"name": "Parineeti Chopra", "followers": 39, "description": "Actress", "country": "India"},
    {"name": "Sonu Sood", "followers": 15, "description": "Actor", "country": "India"},
    {"name": "Amitabh Bachchan", "followers": 32, "description": "Actor", "country": "India"},
    {"name": "Sachin Tendulkar", "followers": 37, "description": "Cricketer", "country": "India"},
    {"name": "Aamir Khan", "followers": 27, "description": "Actor", "country": "India"},
    {"name": "Madhuri Dixit", "followers": 33, "description": "Actress", "country": "India"},
    {"name": "Arijit Singh", "followers": 14, "description": "Singer", "country": "India"},
    {"name": "Salman Khan", "followers": 58, "description": "Actor", "country": "India"},
    {"name": "Shah Rukh Khan", "followers": 32, "description": "Actor", "country": "India"},
    {"name": "Ajay Devgn", "followers": 14, "description": "Actor", "country": "India"},
    {"name": "Kajol", "followers": 14, "description": "Actress", "country": "India"}
]

#randomly choose  2 dictionary as A and B and show user
#ask user which has the higher/lower followers
#if they correct add 1 in score and repeat 
#else if they wrong , tell them and quit the game

def random_ppl(account):
    acc_name = account['name']
    acc_des = account['description']
    acc_nation = account['country']
    return f" {acc_name}, a {acc_des} from {acc_nation}"
game = True
score = 0    
B_statement = random.choice(data)
while game:
    A_statement = B_statement
    B_statement = random.choice(data)
    if A_statement == B_statement:
        B_statement = random.choice(data)
        
    f1 = A_statement['followers']
    f2 = B_statement['followers']    

    print(f"Comapre A: {random_ppl(A_statement)}")
    print(f"Comapre B: {random_ppl(B_statement)}")
        
    print(f"***************** Your current score is {score} *****************")
    user_choice = input("Which one has more followers: Type 'A' or 'B' :- ") 
    
    if  user_choice.upper() == 'A' and f1 > f2:
        print("Correct! You earn 1 point")
        score += 1
    elif user_choice.upper() == 'A' and f1 < f2:
        print("That's a wrong answer! YOU LOSE")
        game = False
        break
    elif user_choice.upper() == 'B' and f1 > f2:
        print("Correct! You earn 1 point")
        score += 1
    elif user_choice.upper() == 'B' and f1 < f2:
        print("That's a wrong answer! YOU LOSE")
        game = False
        break
    
    else:
        print("Invalid input! Please try again")
        
    