import random

geo_dict = {"Austria": "Vienna", "Australia": "Canberra", "Slovenia": "Ljubljana", "France": "Paris",
            "Germany": "Berlin", "Croatia": "Zagreb", "Lithuania": "Vilnius", "Russia": "Moscow",
            "Bosnia and Herzegovina": "Sarajevo", "The United Kingdom": "London", "Ireland": "Dublin",
            "Spain": "Madrid", "Portugal": "Lisbon", "Ukraine": "Kiev", "Belarus": "Minsk", "Serbia": "Belgrade",
            "Kosovo": "Pristina", "Macedonia": "Skopje", "Greece": "Athens", "USA": "Washington DC",
            "The People's Republic of China": "Beijing", "Argentina": "Buenos Aires", "Brazil": "Brasilia",
            "Japan": "Tokyo"
            }

print("Welcome to Geography quiz, hope you have fun and learn lots about capitals!")


def geo_quiz():
    points_tally = 0
    while True:
        for country in random.sample(list(geo_dict), 10):

            capital = geo_dict[country]
            question = input("What is the capital of %s? " % country)
            if question.lower() == capital.lower():
                points_tally += 1
                print("Well done, but don't get ahead of yourself.")
            else:
                print("Wrong, the capital of {} is {}.".format(country, capital))
        print("You scored " + str(points_tally) + " points!")
        continue_playing_query = input("Would you like to play again? (yes/no)")
        if continue_playing_query.lower() == "yes":
            geo_quiz()
        else:
            break


geo_quiz()
