import media
import fresh_tomatoes

#Define movie instance for Toy Story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#Define movie instance for Avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#Define movie instance for King's Speech
king_speech = media.Movie("King's Speech",
                          "An inspirational movie about England's King",
                          "https://upload.wikimedia.org/wikipedia/en/a/a0/Kings_speech_ver3.jpg",
                          "https://www.youtube.com/watch?v=dsgOquSwxd0")

#Define movie instance for School of Rock
school_of_rock = media.Movie("School of Rock",
                             "Using Rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

#Define movie instance for Ron Clark Story
ron_clark_story = media.Movie("Real Steel",
                              "A story of kid and a robot taking on the champ of robotic boxing",
                              "https://upload.wikimedia.org/wikipedia/en/2/22/Real_Steel_Poster.jpg",
                              "https://www.youtube.com/watch?v=3S8a180uYBM")

#Define movie instance for Phone Booth
phone_booth = media.Movie("Phone Booth",
                          "One phone call through the booth can change your life",
                          "https://upload.wikimedia.org/wikipedia/en/c/c4/Phone_Booth_movie.jpg",
                          "https://www.youtube.com/watch?v=p07lBCfC2q8")


#Create a list of all the movie instances
movies = [toy_story, avatar, king_speech, school_of_rock, ron_clark_story, phone_booth]

#Open the website url for the movie list
fresh_tomatoes.open_movies_page(movies)
