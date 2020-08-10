init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="dev_test_chess_teaching",
            prompt="TEST CHESS TEACHING DISPLAYABLE",
            category=["dev"],
            random=False,
            pool=True,
            unlocked=True,
            aff_range=(None,None)
        )
    )


label dev_test_chess_teaching:
    m 1hua "Sure!"
    m 1eua "I'll set your color to white."

    m 1dsa "Let me show the board.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    python:
        chess_teaching_disp = MASChessDisplayableBase(player_color=True)
        chess_teaching_disp.show()

    m 1esa "Let's just test the highlights.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    python:
        a_to_h = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        _1_to_8 = range(1, 9)

        for l in a_to_h:
            for num in _1_to_8:
                chess_teaching_disp.request_highlight("{0}{1}".format(l, num))
                pause(0.1)

    m 1eua "Now I'll remove the highlights.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    python:
        for l in a_to_h:
            for num in _1_to_8:
                chess_teaching_disp.remove_highlight("{0}{1}".format(l, num))
                pause(0.1)

    m "Okay, now I'll queue a move from b2 to b4."
    $ chess_teaching_disp.queue_move("b2b4")

    m 3eub "Now I'll queue from g8 to h6."
    $ chess_teaching_disp.queue_move("g8g6")

    m 3dua "Now I'll hide the board.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    $ chess_teaching_disp.hide()
    return
