label tests:
    " This is going to test every dice combo."
    call sicBoStart
    $ DicexA = ['One ⚀', 'Two ⚁', 'Three ⚂', 'Four ⚃', 'Five ⚄', 'Six ⚅']
    $ X = 0
    $ Y = 0
    $ Z = 0
    scene bg sicboboard
    while X < 6:
        $Dicex = DicexA[X]
        while Y < 6:
            $Dicey = DicexA[Y]
            while Z < 6:
                $Dicez = DicexA[Z]
                # Place a bet on all tiles, cash the bets (remove loosing bets, sum up the winnings), then show the winning bets
                call allBets
                call cashBets
                call showBets
                "The winning numbers are [Dicex] - [Dicey] - [Dicez]"
                # "You have won [cash]"
                $ Z += 1
            $ Y += 1
            $ Z = 0
        $ X += 1
        $ Y = 0
    
    call allBets



label allBets:
    $ betSmall = 1 
    $ betBig = 1
    $ betTrips = [1, 1, 1, 1, 1, 1, 1]
    $ betDoubs = [1, 1, 1, 1, 1, 1]
    $ betNums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    $ betPairs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    $ betDice = [1, 1, 1, 1, 1, 1]

    return