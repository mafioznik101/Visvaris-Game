# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Indrihs", color="#b3ff30")


# The game starts here.
image indrihs = "indrihs/indrihs1.png"
image indrihs_smile = "indrihs/indrihs2.png"
image city = "bg/bgcity.jpg"
transform half_size: 
    zoom 0.5 #adjust as required
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene city

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show indrihs at half_size
    with dissolve

    # These display lines of dialogue.

    e "Nauri, atnaca rezultati programmesanas projekta darba"
    hide indrihs
    show indrihs_smile at half_size
    e "un karoch tev pizda"

    # This ends the game.

    return
