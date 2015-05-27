import media
import fresh_tomatoes

toystory = media.Movie("Toy Story","Toy Story is a 1995 American computer-animated buddy-comedy adventure film produced by Pixar Animation Studios and released by Walt Disney Pictures. \
	Directed by John Lasseter, Toy Story was the first feature-length computer-animated film and the first theatrical film produced by Pixar. \
	Toy Story follows a group of anthropomorphic toys who pretend to be lifeless whenever humans are present, and focuses on the relationship between Woody, a pullstring cowboy doll (voiced by Tom Hanks), and Buzz Lightyear, an astronaut action figure (voiced by Tim Allen). The film was written by John Lasseter, Andrew Stanton, Joel Cohen, Alec Sokolow, and Joss Whedon, and featured music by Randy Newman. \
	Its executive producers were Steve Jobs and Edwin Catmull.","http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar","Avatar (marketed as James Cameron's Avatar) is a 2009 American[7][8] epic science fiction film directed, written, produced, and co-edited by James Cameron, and starring Sam Worthington, Zoe Saldana, Stephen Lang, Michelle Rodriguez, and Sigourney Weaver. \
	The film is set in the mid-22nd century, when humans are colonizing Pandora, a lush habitable moon of a gas giant in the Alpha Centauri star system to mine the mineral unobtanium,[9][10] a room-temperature superconductor.[11]","http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=d1_JBMrrYw8")

school_of_rock = media.Movie("School of Rock","School of Rock is a 2003 American comedy film directed by Richard Linklater, written by Mike White, and starring Jack Black. \
	The main plot follows struggling rock singer and guitarist, Dewey Finn (portrayed by Black), who is kicked out of his band and subsequently disguises himself as a substitute teacher at a prestigious prep school. \
	After witnessing the musical talent in his students, Dewey forms a band of fourth-graders to attempt to win the upcoming Battle of the Bands and pay off his rent. \
	The picture's supporting cast features Joan Cusack, Sarah Silverman, and Mike White. A stage musical adaptation is planned to open on Broadway in late 2015,[3] with a television adaptation for Nickelodeon also planned.",
	"http://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",r"Ratatouille is a 2007 American computer-animated comedy film produced by Pixar Animation Studios and released by Walt Disney Pictures. \
	It is the eighth film produced by Pixar, and was co-written and directed by Brad Bird, who took over from Jan Pinkava in 2005. \
	The title refers to a French dish, ratatouille, which is served at the end of the film, and is also a play on words about the species of the main character. \
	The film stars the voices of Patton Oswalt as Remy, an anthropomorphic rat who is interested in cooking; Lou Romano as Linguini, a young garbage boy who befriends Remy; Ian Holm as Skinner, the head chef of Auguste Gusteau's restaurant; \
	aneane Garofalo as Colette, a rtisseur at Gusteau's restaurant; Peter O'Toole as Anton Ego, a restaurant critic; Brian Dennehy as Django, Remy's father and leader of his clan; Peter Sohn as Emile, Remy's older brother; and Brad Garrett as Auguste Gusteau, a recently deceased chef. \
	The plot follows Remy, who dreams of becoming a chef and tries to achieve his goal by forming an alliance with a Parisian restaurant's garbage boy.",
	"http://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",r"Midnight in Paris is an American 2011 romantic comedy fantasy film written and directed by Woody Allen.[3] Set in Paris, the film follows Gil Pender, a screenwriter, who is forced to confront the shortcomings of his relationship with his materialistic fiancee and their divergent goals, which become increasingly exaggerated as he travels back in time each night at midnight.[4] \
	The movie explores themes of nostalgia and modernism. Produced by the Spanish group Mediapro and Allen's Gravier Productions, the film stars Owen Wilson, Rachel McAdams, Marion Cotillard, Lea Seydoux, Kathy Bates and Adrien Brody. \
	It premiered at the 2011 Cannes Film Festival and was released in North America in May 2011.[4][5] The film opened to critical acclaim and has commonly been cited as one of Allen's best films in recent years. \
	In 2012, the film won both the Academy Award for Best Original Screenplay and the Golden Globe Awards for Best Screenplay; and was nominated for three other Academy Awards: Best Picture, Best Director, and Best Art Direction.[6]",
	"http://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg", "https://www.youtube.com/watch?v=5nOF93SzX6s")

hunger_games = media.Movie("Hunger Games",r"The Hunger Games is a 2012 American science fiction adventure film directed by Gary Ross and based on the novel of the same name by Suzanne Collins.\
 The picture is the first installment in The Hunger Games film series and was produced by Nina Jacobson and Jon Kilik, with a screenplay by Ross, Collins, and Billy Ray. \
 The film stars Jennifer Lawrence, Josh Hutcherson, Liam Hemsworth, Woody Harrelson, Elizabeth Banks, Lenny Kravitz, Stanley Tucci, and Donald Sutherland.[5] \
 The story takes place in a dystopian post-apocalyptic future in the nation of Panem, where boys and girls between the ages of 12 and 18 must take part in the Hunger Games, a televised annual event in which the tributes are required to fight to the death until there is one remaining who will be crowned the victor. Katniss Everdeen (Lawrence) volunteers to take her younger sister's place in the games. \
 Joined by her district's male tribute Peeta Mellark (Hutcherson), Katniss travels to the Capitol to train for the Hunger Games under the guidance of former victor Haymitch Abernathy (Harrelson).",
	"http://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg", "https://www.youtube.com/watch?v=mfmrPu43DF8")


movies = [toystory,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]
fresh_tomatoes.open_movies_page(movies)