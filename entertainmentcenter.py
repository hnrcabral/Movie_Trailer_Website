import fresh_tomatoes
import media

the_departed = media.Movie("The Departed", "South Boston cop Billy Costigan ("
                           "Leonardo DiCaprio) goes under cover to infiltrate "
                           "the organization of gangland chief Frank Costello "
                           "(Jack Nicholson). As Billy gains the mobster's "
                           "trust, a career criminal named Colin Sullivan "
                           "(Matt Damon) infiltrates the police department and"
                           " reports on its activities to his syndicate bosses"
                           ". When both organizations learn they have a mole "
                           "in their midst, Billy and Colin must figure out"
                           " each other's identities to save their own lives.",
                           "https://upload.wikimedia.org/wikipedia/en/5/50/"
                           "Departed234.jpg",
                           "https://www.youtube.com/watch?v=SGWvwjZ0eDc")

wonder_woman = media.Movie("Wonder Woman", "Before she was Wonder Woman "
                           "(Gal Gadot), she was Diana, princess of the "
                           "Amazons, trained to be an unconquerable "
                           "warrior. Raised on a sheltered island paradise,"
                           "Diana meets an American pilot (Chris Pine) who "
                           "tells her about the massive conflict that's raging"
                           " in the outside world. Convinced that she can stop"
                           " the threat, Diana leaves her home for the first "
                           "time. Fighting alongside men in a war to end all "
                           "wars, she finally discovers her full powers and "
                           "true destiny.",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/"
                           "Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")

the_dark_knight = media.Movie("The Dark Knight", "With the help of allies Lt."
                              "Jim Gordon (Gary Oldman) and DA Harvey Dent "
                              "(Aaron Eckhart), Batman (Christian Bale) has "
                              "been able to keep a tight lid on crime in "
                              "Gotham City. But when a vile young criminal "
                              "calling himself the Joker (Heath Ledger) "
                              "suddenly throws the town into chaos, the caped"
                              "Crusader begins to tread a fine line between "
                              "heroism and vigilantism.",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/"
                              "Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")

the_dark_knight_rises = media.Movie("The Dark Knight Rises", "It has been "
                                    "eight years since Batman (Christian Bale)"
                                    ", in collusion with Commissioner Gordon"
                                    "(Gary Oldman), vanished into the night. "
                                    "Assuming responsibility for the death of "
                                    "Harvey Dent, Batman sacrificed everything"
                                    " for what he and Gordon hoped would be"
                                    "the greater good. However, the arrival of"
                                    "a cunning cat burglar (Anne Hathaway) and"
                                    "a merciless terrorist named Bane (Tom "
                                    "Hardy) force Batman out of exile and into"
                                    " a battle he may not be able to win.",
                                    "https://upload.wikimedia.org/wikipedia/en"
                                    "/8/83/Dark_knight_rises_poster.jpg",
                                    "https://www.youtube.com/watch?v="
                                    "EXeTwQWrcwY")

wolf_of_wallstreet = media.Movie("The Wolf of Wall Street", "In 1987, Jordan"
                                 " Belfort (Leonardo DiCaprio) takes an entry-"
                                 "level job at a Wall Street brokerage firm. "
                                 "By the early 1990s, while still in his 20s, "
                                 "Belfort founds his own firm, Stratton "
                                 "Oakmont. Together with his trusted "
                                 "lieutenant (Jonah Hill) and a merry band of "
                                 "brokers, Belfort makes a huge fortune by "
                                 "defrauding wealthy investors out of "
                                 "millions. However, while Belfort and his "
                                 "cronies partake in a hedonistic brew of sex,"
                                 " drugs and thrills, the SEC and the FBI "
                                 "close in on his empire of excess.",
                                 "https://upload.wikimedia.org/wikipedia/en/"
                                 "thumb/d/d8/The_Wolf_of_Wall_Street_"
                                 "%282013%29.png/220px-The_Wolf_of_Wall_"
                                 "Street_%282013%29.png",
                                 "https://www.youtube.com/watch?v=iszwuX1AK6A")

interstellar = media.Movie("Interstellar", "In Earth's future, a global crop "
                           "blight and second Dust Bowl are slowly rendering "
                           "the planet uninhabitable. Professor Brand (Michael"
                           " Caine), a brilliant NASA physicist, is working on"
                           " plans to save mankind by transporting Earth's "
                           "population to a new home via a wormhole. But first"
                           ",Brand must send former NASA pilot Cooper (Matthew"
                           "McConaughey) and a team of researchers through the"
                           " wormhole and across the galaxy to find out which "
                           "of three planets could be mankind's new home.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/"
                           "Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=2LqzF5WauAw")

movies = [the_departed, wonder_woman, the_dark_knight, the_dark_knight_rises,
          wolf_of_wallstreet, interstellar]
fresh_tomatoes.open_movies_page(movies)
