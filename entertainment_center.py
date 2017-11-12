import fresh_tomatoes
import media


#Initialize each instance of the movie class
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#avatar.show_trailer()

contagion = media.Movie("Contagion",
                         "A deadly virus quickly wreaks havoc on the human population",
                        "https://upload.wikimedia.org/wikipedia/en/8/86/Contagion_Poster.jpg",
                        "https://www.youtube.com/watch?v=4sYSyuuLk5g")
harry_potter = media.Movie("Harry Potter and the Order of the Phoenix",
                           "A young wizard and his friends join together to conquer evil",
                           "https://upload.wikimedia.org/wikipedia/en/e/e7/Harry_Potter_and_the_Order_of_the_Phoenix_poster.jpg", 
                           "https://www.youtube.com/watch?v=y6ZW7KXaXYk")
wall_e = media.Movie("Wall-E",
                    "A robot saves humanity",
                    "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg", 
                    "https://www.youtube.com/watch?v=alIq_wG9FNk")
lord_of_the_rings = media.Movie("Lord of the Rings: Fellowship of the Ring",
                  "A hobbit is tasked with destroying the ring of evil",
                  "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                  "https://www.youtube.com/watch?v=V75dMMIW2B4")

#Create a list of all the movies to be displayed on the website
movies = [toy_story, avatar, contagion, harry_potter, wall_e, lord_of_the_rings]

#Call the function to display the movie webpage
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__module__)
