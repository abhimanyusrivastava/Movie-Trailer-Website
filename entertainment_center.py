import media
import fresh_tomatoes
#Importing media and fresh_tomatoes libraries

"""This python file stores the movie information. (Movie Title, Image URL, Youtube URL)"""

toystory = media.Movie("Toy Story", "Toy Story is a 1995 American computer-animated buddy-comedy adventure film", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar", "Avatar epic science fiction film. The film is set in the mid-22nd century, when humans are colonizing Pandora, a lush habitable moon of a gas giant in the Alpha Centauri star system to mine the mineral unobtanium.", "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=d1_JBMrrYw8")

school_of_rock = media.Movie("School of Rock", "School of Rock is a comedy film about a struggling rock singer and guitarist, Dewey Finn (portrayed by Black), who is kicked out of his band and subsequently disguises himself as a substitute teacher at a prestigious prep school.", "http://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille", "Ratatouille is a 2007 American computer-animated comedy film produced by Pixar Animation Studios and released by Walt Disney Pictures. The plot follows Remy, who dreams of becoming a chef and tries to achieve his goal by forming an alliance with a Parisian restaurant's garbage boy.", "http://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Midnight in Paris is an American 2011 romantic comedy fantasy film. Set in Paris, the film follows Gil Pender, a screenwriter, who is forced to confront the shortcomings of his relationship with his materialistic fiancee and their divergent goals, which become increasingly exaggerated as he travels back in time each night at midnight.", "http://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg", "https://www.youtube.com/watch?v=5nOF93SzX6s")

hunger_games = media.Movie("Hunger Games", "The Hunger Games is a 2012 American science fiction adventure film  The story takes place in a dystopian post-apocalyptic future in the nation of Panem, where boys and girls between the ages of 12 and 18 must take part in the Hunger Games, a televised annual event in which the tributes are required to fight to the death until there is one remaining who will be crowned the victor.", "http://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg", "https://www.youtube.com/watch?v=mfmrPu43DF8")


movies = [toystory, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]


# Calling open_movies_page definition from fresh_tomatoes library. This definition will create a static webpage for the list of movies and information passed on the list variable "movies"

fresh_tomatoes.open_movies_page(movies)
