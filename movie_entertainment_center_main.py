import classic_movies
import movies_blueprint

your_name = movies_blueprint.Movie("Kimi No Na Wa",
                                   "Story of a boy and girl who exchanging their souls and Struggle for meeting with each other.",
                                   "http://i.imgur.com/Uqw37Sk.jpg",
                                   "https://www.youtube.com/watch?v=hRfHcp2GjVI")

interstellar = movies_blueprint.Movie("Interstellar",
                                  "team of researchers travelling through the wormhole and across the galaxy to find out which of three planets could be mankind's new home.",
                                  "https://image.tmdb.org/t/p/w300_and_h450_bestv2/nBNZadXqJSdt05SHLqgT0HuC5Gm.jpg",
                                  "https://www.youtube.com/watch?v=zSWdZVtXT7E&t=17s")

Natarang = movies_blueprint.Movie("Natarang",
                              "A village laborer is passionate about the theatre shows and decides to start a troupe. Instead of a king's role that he wished for, he gets to enact a homosexual; he is torn between his passion and societal prestige.",
                              "https://rukminim1.flixcart.com/image/1408/1408/av-media/movies/k/c/e/natrang-original-imadqgny7q6d5gcn.jpeg?q=90",
                              "https://www.youtube.com/watch?v=CnXdnNAyaY0")

davinci_code =  movies_blueprint.Movie("The Da Vinci Code",
                                "Leonardo da Vinci's most famous paintings lead to the discovery of a religious mystery. For 2,000 years a secret society closely guards information that -- should it come to light -- could rock the very foundations of Christianity.",
                                "https://upload.wikimedia.org/wikipedia/en/e/e9/The_da_vinci_code_final.jpg",
                                "https://www.youtube.com/watch?v=-rMElSGZpV4")
tamasha = movies_blueprint.Movie("Tamasha",
                             "Story of person who is trying to discover his true self.",
                             "http://www.media.glamsham.com/download/poster/images/tamasha/02-tamasha.jpg",
                             "https://www.youtube.com/watch?v=o-e5eWVCzx8")

classmate = movies_blueprint.Movie("Classmates",
                               "A story of group of best friends affected by misunderstanding betwwen them.",
                               "http://cdn1.marathistars.com/wp-content/uploads/2014/07/Classmates-Marathi-Movie-Poster.jpg",
                               "https://www.youtube.com/watch?v=z_5k5IAc3iM")
#print (your_name.storyline)
#interstellar.show_trailer()
movies = [your_name, interstellar, Natarang, davinci_code, tamasha, classmate]
classic_movies.open_movies_page(movies)

