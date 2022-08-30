# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Croupier")
init:

    image bg sicboboard = "bg sicboboard.png"
# The game starts here.

label start:

    scene bg casino
    show Croupier at left
    c "Welcome. This game is Sic-Bo. Would you like to play?"
    $ looper = True
    while looper:
        menu:
            "Play Sic-Bo":
                scene bg sicboboard
                call sicBoStart
                c "Here are [chips] to start playing with.\nGood luck!"
                jump placeBets

                show bg casino
                show Croupier at left
                c "In that game you won [chips] from [gameCount]."

            "Learn how to play Sic-Bo":
                # This is the tutorial
                scene bg sicboboard
                call sicBoStart
                $ betSmall = 1 
                $ betBig = 1
                $ betTrips = [1, 1, 1, 1, 1, 1, 1]
                $ betDoubs = [1, 1, 1, 1, 1, 1]
                $ betNums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                $ betPairs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                $ betDice = [1, 1, 1, 1, 1, 1]
                call showBets
                c "This is a Sic-Bo table."
                call showBets
                c "You click on the board to place your chips and make a bet on which dice or combination of dice you think will appear."
                $ betSmall = 0 
                $ betBig = 0
                $ betTrips = [0, 0, 0, 0, 0, 0, 0]
                $ betDoubs = [0, 0, 0, 0, 0, 0]
                $ betNums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                $ betPairs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                call showBets
                c "The bottom row, allows you to bet on the face value of one of the three dice."
                $ betDice = [1, 0, 0, 0, 0, 0]
                call showBets
                c "For example, you could click on {b}One ⚀{/b}.\nIf one of the rolled dice is a ⚀ you will win 1 chip for every bet placed.\n(If two or three of the dice have a ⚀ you will win 2 or 12 chips)."
                $ betPairs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  
                call showBets
                $ betPairs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                $ betPairs[4] += 1
                c "The second bottom line allows you to bet on a pair occuring.\nIf you guess/bet correctly you get 6 chips for every chip you bet."
                call showBets
                c "For example you could click on {b}⚀⚄{/b} to bet on a 1 & 5 being rolled.\n\n{i}If the winning dice were one ⚀, five ⚄, six ⚅ - this bet would win you 7 chips. 6 chips for the pair, and 1 chip for the one dice.{/i}"
                $ betNums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                call showBets
                c "The next line up, with written numbers between 4 and 17 allow you to bet on the sum of the three dice.\nEach number has different payouts depending on its likelihood."
                $ betNums = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
                call showBets
                $ betNums[8] = 0
                $ betPairs[4] = 0
                $ betDice[0] = 0
                c "You can click on the {b}12{/b} to place a bet that the next sum of the dice will equal 12.\nIf you win you will get 7 chips for each chip you bet."
                $ betTrips[0] = 1
                call showBets
                c "At the top of the board you can place a bet if you think there will be a tripple in the next roll.\nIf this wins you will get 31 chips for each chip you bet."
                $ betTrips = [0,1,1,1,1,1,1]
                call showBets
                c "You can also place a bet on an exact tripple (i.e. ⚄⚄⚄)\nIf this bet wins you get 180 chips for every chip you bet."
                $ betTrips = [0, 0, 0, 0, 0, 0, 0]
                $ betDoubs = [1, 1, 1, 1, 1, 1]
                call showBets
                c "Similarly, you can place a bet on a double occuring (i.e. ⚄⚄).\nIf this bet wins you get 11 chips for every chip you bet."
                $ betDoubs = [0, 0, 0, 0, 0, 0]
                $ betSmall = 1 
                $ betBig = 1
                call showBets
                c "In the Top Left and Top Right of the table you can bet on Small (the total dice being 4-10), or Big (the total being 11-17).\nIf these win you get 1 chip for every chip you bet.\nBut beware, if a tripple is rolled these bets loose."
                $ betTrips = [1, 1, 1, 1, 1, 1, 1]
                $ betDoubs = [1, 1, 1, 1, 1, 1]
                $ betNums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                $ betPairs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                $ betDice = [1, 1, 1, 1, 1, 1]

                python:
                    ui.textbutton('"no more bets"', clicked=Jump('calcBets'), xalign=0.5, yalign=0.725)
                c "So after you have placed your bets, you click on {b}no more bets{/b} under the betting table."
                call showBets
                c "The crouper will then press a button to roll the dice, and the results will be shown.\nThen your winnings will be calculated and added to your chips."
                python:
                    ui.textbutton('"no more bets"', clicked=Jump('calcBets'), xalign=0.5, yalign=0.725)
                c "For example, lets say you bet one chip on everything everything."
                show Croupier at left
                $ tutorial = True
                call calcBets
                call showBets
                c "As you saw in that game, the winning numbers were [Dicex] - [Dicey] - [Dicez].\nWinning [cash] chips."
                c "Now the winning bets are still on the table.\n\nYou will need to select {b}Clear Bets{/b}"
                call clearBets
                
                show bg casino

                call sicBoStart
                show Croupier at left
                c "Remember: To play Sic-Bo:\n1. Click on the board to place bets.\n2. Click 'no more bets' when you have placed all your bets and are ready to let the dice roll.\n"
                c "3. Your winning bets remain on the table (if you want to remove them click {b}Clear Bets{/b})."
            "Quit game":
                $ looper = False


    c "Thanks for playing Sic-Bo."
    c ""

    return
