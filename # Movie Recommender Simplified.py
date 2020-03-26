# Movie Recommender 
# Author: Michael Keller
# Date: 3/1/2020
# for Python 3.7.6 

# Imports 
import xlrd
import os 
from os import path 
import numpy as np
import random

##########################################################################################

# # Find path
# mpath = path.realpath("FavoriteMovies.csv")
# npath = path.realpath("FavoriteMovies.xlsx")

# # Sets working directory to path 
# os.chdir('c:/Users/Keller/Desktop/Learning/Projects/')

# # check to see if FavouriteMovies.csv exists 
# if path.exists("FavoriteMovies.csv") == 0:
#     print("Movie List can not be found, please download movie list or change directory.")

# # open movie list 
# import pandas as pd #makes function pandas called useing pd 
# df = pd.read_csv ('c:/Users/Keller/Desktop/Learning/Projects/FavoriteMovies.csv') # problem here, says path does not exist - fixed by writing path, use / instead of \ 

# # removes title row from DataFrame - only needed if name is in first row and coloum 
# # df = df.drop(df.index[0]) 

# # More from dataFrame to array 
# titles = [] 
# ratings = []
# genre = []
# for i, row in df.iterrows():
#     titles.append( row['Title'])
#     ratings.append(row['Rating'])
#     genre.append(row['Category'])

# for i in range(len(genre)):
#     genre[i] = genre[i].strip(' ')
# index = list(range(0, len(titles)))
# print(genre)

# # incase I ever want to make this not have to import from favorite movies.csv, copy paste below printout into code 
# print(titles)
# print(ratings)
# print(genre)

##########################################################################################

titles = ['Cold War', 'Trance', 'Killer Joe', 'Never Let Me Go', 'Lord of War', 'Shooting Dogs', 'The Machinist', '28 Days Later ', 'Equilibrium', 'Office Space', 'Funny Games', '12 Monkeys', 'Spartacus', 'On the Silver Globe', "Ferris Bueller's Day Off", 'The Big Red One', 'Help', 'The Souvenir ', 'Eye in the Sky', 'It Follows', 'Birdman', 'The Grand Budapest Hotel', 'Under the Skin', 'Enemy ', 'Dredd', 'A Beautiful Day in the Neighborhood ', 'The Tree of Life', 'A Single Man', 'Dear Zachary', 'The Wrestler', 'Crash', 'Jarhead', 'Black Hawk Down', 'Muholland Drive', 'Cast Away', 'Rushmore', 'The Big Lebowski', 'The Fifth Element', 'Fargo', 'Trainspotting', 'Jacobs Ladder', 'When the Wind Blows', 'Brazil', 'Platoon', 'Scarface', 'Pink Floyd The Wall', 'Catch-22', 'The Yellow Submarine', 'Cool Hand Luke', 'For a Few Dollars More', 'Zulu', 'Lolita', 
'The Longest Day', 'Psycho', 'Vertigo', 'The Bridge on the River Kwai', 'Rebecca', 'Jojo Rabbit', 'Midsommar Directors Cut', 'Once Apon a Time in Hollywood', 'The Last Black Man in San Francisco ', 'High Life', 'The Death of Stalin', 'They Shall not Grow Old', 'Tully', 'You Were Never Really Here', 'Baby Driver', 'Call Me By Your Name', 'I, Tonya ', 'The Killing of a Sacred Deer', 'Hunt for the Wilderpeople', 'Indignation', 'La La Land', 'The Irishman ', 'The Missing Picture', '12 Years a Slave', 'Upstream Colour', 'Zero Dark Thirty', 'Argo', 'Django Unchained', 'Moonrise Kingdom', '50/50', 'Blue Valentine', '500 Days of Summer', 'Avatar', 'Fantastic Mr. Fox', 'Moon', 'Watchmen', '1408', '310 to Yuma', 'Across the Universe', 'Hot Fuzz', 'The Assassination of Jesse James by the Coward Robert Ford', 'A Scanner Darkly', 'Borat', "Pan's Labyrinth", 'Syriana', 'Hotel Rwanda', 'Kill Bill Volume 2', 'Shaun of the Dead', 'Kill Bill Volume 1', 'Gangs of New York', 'Memento', 'The Green Mile', 'The Big Lebowski', 'Uncut Gems ', 'Gattaca', 'Before Sunrise', 'Forest Gump', 'The Shawshank Redemption', 'The Silence of the Lambs', 'Indiana Jones and the Last Crusade', 'Full Metal Jacket', 'Aliens', 'Once Apon a Time in America', 'Blade Runner', 'Indiana Jones and the Raiders of the Lost Ark', 'Airplane', 'The Shining', 'Alien ', 'Cross of Iron', 'Network', 'Barry Lyndon', 'Blazing Saddles', 'Chinatown', "Kelly's Heros", 'The Good, The Bad, and the Ugly', 'The Graduate', 'Repulsion', 'The Great Escape', 'La Strada', 'Rear Window', 'Casablanca', 'Citizen Kane', 'Battleship Potemkin', 'Annihilation', 'Burning', 'Hereditary  ', "Won't You Be My Neighbor ", 'Get Out', 'Lady Bird', 'Moonlight', 'Nocturnal Animals', 'Silence', 'The Lobster', 'Sicario', 'Cloud Atlas', 'We Need to Talk About Kevin', 'Drive', 'Inception', 'Shutter Island', 'The Girl With the Dragon Tattoo', 'The Social Network', 'Inglorious Bastards ', 'There Will be Blood', 'Lives of Others', 'Downfall', 'Before Sunset', 'Lilya-4-ever', 'The Pianist', 'The Thin Red Line', 'Pi', 'Saving Private Ryan', 'Das Boot', 'Good Fellas', 'Come and See', 'Apocalypse Now', 'Annie Hall', 'Taxi Driver', 'The Godfather Part 2', 'The Godfather', 'Patton', 'Dr. Strangelove or How I learned to Stop Worrying and Love the Bomb', 'Lawrence of Arabia', 'The Apartment', '12 Angry Men', 'Paths of Glory', 'The Killing', 'The Great Dictator', 'Mr. Smith Goes to Washington', 'M', 'Parasite', 'The Lighthouse', 'Roma', 'The Favourite', 'Blade Runner 2049', 'Dunkirk', 'Phantom Thread', 'Three Billboards Outside Ebbing, Missouri', 'Ex Machina', 'A Hidden Life ', 'Interstellar', 'Boyhood', 'Nightcrawler', 'Before Midnight', 'Her', 'Its Such a Beautiful Day', 'Children of Men', 'Babel', 'Eternal Sunshine of the Spotless mind', 'Lost in Translation', 'Requiem for a Dream', 'Magnolia', '2001 A Space Odyssey']
ratings = [3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 
4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
genre = ['Drama', 'Suspense', 'Crime', 'Romance', 'Drama', 'War', 'Psychological', 'Horror', 'Action', 'Comedy', 'Psychological', 'Psychological', 'Drama', 'Adventure', 'Adventure', 'War', 'Musical', 'Drama', 'War', 'Horror', 'Psychological', 'Comedy', 'Psychological', 'Psychological', 'Action', 'Drama', 'Coming of age', 'Drama', 'Documetary', 'Drama', 'Drama', 'War', 'War', 'Psychological', 'Adventure', 'Comedy', 'Comedy', 'Adventure', 'Crime', 'Drama', 'Psychological', 'Drama', 'Drama', 'War', 'Crime', 'Musical', 'Comedy', 'Musical', 'Drama', 'Action', 'War', 'Drama', 'War', 'Suspense', 'Drama', 'War', 'Suspense', 'Comedy', 'Horror', 'Drama', 'Drama', 'Psychological', 'Comedy', 'Documetary', 'Comedy', 'Psychological', 'Musical', 'Coming of age', 'Comedy', 'Drama', 'Coming of age', 'Drama', 'Musical', 'Crime', 'Documetary', 'Drama', 'Romance', 'Drama', 'Drama', 'Adventure', 'Comedy', 'Drama', 'Romance', 'Romance', 'Adventure', 'Adventure', 'Psychological', 'Action', 'Horror', 'Adventure', 'Musical', 'Comedy', 'Drama', 'Psychological', 'Comedy', 'Drama', 'Drama', 'War', 'Crime', 'Comedy', 'Crime', 'Drama', 'Psychological', 'Drama', 'Comedy', 'Drama', 'Drama', 'Romance', 'Drama', 'Drama', 'Crime', 'Adventure', 'War', 'Horror', 'Drama', 'Drama', 'Adventure', 'Comedy', 'Horror', 'Horror', 'War', 'Drama', 'Drama', 'Comedy', 'Noir', 'War', 'Action', 'Comedy', 'Psychological', 'Adventure', 'Drama', 'Suspense', 'Drama', 'Drama', 'Drama', 'Horror', 'Drama', 'Psychological', 'Documetary', 'Horror', 'Coming of age', 'Coming of age', 'Psychological', 'Drama', 'Comedy', 'Crime', 'Romance', 'Suspense', 'Crime', 'Action', 'Suspense', 'Drama', 'Drama', 'War', 'Drama', 'Drama', 'Drama', 'Romance', 'Drama', 
'Drama', 'War', 'Psychological', 'War', 'War', 'Crime', 'War', 'Psychological', 'Comedy', 'Psychological', 'Crime', 'Crime', 'War', 'Comedy', 'War', 'Romance', 'Drama', 'War', 'Crime', 'Comedy', 'Drama', 'Drama', 'Drama', 'Psychological', 'Drama', 'Drama', 'Drama', 'War', 'Drama', 'Drama', 'Psychological', 'Drama', 'Adventure', 'Coming of age', 'Psychological', 'Romance', 'Romance', 'Psychological', 'Drama', 'Drama', 'Psychological', 'Romance', 'Drama', 'Drama', 'Psychological']
index = list(range(0, len(titles)))
# Find what type of movie the user wants to watch 
print('What type of movie would you like to watch?')
print('1  = Action')
print('2  = Adventure')
print('3  = Comedy')
print('4  = Coming of Age')
print('5  = Crime')
print('6  = Documentary')
print('7  = Horror')
print('8  = Musical')
print('9  = Noir')
print('10 = Psychological')
print('11 = Romance')
print('12 = Suspense')
print('13 = War')
choice = int(input('Chose a number: '))


# Logically index movies out of the list based on their choice
# create mask 
mask = []
if choice == 1:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Action')
elif choice == 2:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Adventure')
elif choice == 3:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Comedy')
elif choice == 4:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Coming of Age')
elif choice == 5:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Crime')
elif choice == 6:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Documentary')
elif choice == 7:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Horror')
elif choice == 8:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Musical')
elif choice == 9:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Noir')
elif choice == 10:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Psychological')
elif choice == 11:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Romance')
elif choice == 12:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Suspense')
elif choice == 13:
    for i in range(len(genre)):
        mask.append(genre[i] == 'War')
else:
    mask = index
    
# apply mask 
locs = np.nonzero(mask)

# adjust for index
locs = locs[0]

while True:
    # Do they want to choose or have one selected 
    choice2 = input('Do you like free will? (Y/N) \n')

    if choice2 == 'Y':
        print('------------------ Movie List ----------------')
        print( 'Rating: Title')
        # Print list recommendations 
        for i in range(len(locs)):
            print(str(ratings[locs[i]])+ ': ' + titles[locs[i]]) 
        print('------------------ Movie List ----------------')
        break

    elif choice2 == 'N':
        print('------------------ Movie ----------------')
        movie = random.randrange(len(locs))
        movie = locs[movie]
        print(titles[movie])
        print('------------------ Movie ----------------')
        break

    else:
        print('Incorrect Input, try again')


