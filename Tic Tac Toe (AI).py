while True:
    turn=1
    owins=1
    xwins=1
    tl=0
    tr=0
    tm=0
    cl=0
    cm=0
    cr=0
    bl=0
    bm=0
    br=0
    while True:
        top_row=(str(tl) + str(tm) + str(tr))
        mid_row=(str(cl) + str(cm) + str(cr))
        bottom_row=(str(bl) + str(bm) + str(br))
        diag1=(str(tl) + str(cm) + str(br))
        diag2=(str(tr) + str(cm) + str(bl))
        vert1=(str(tl) + str(cl) + str(bl))
        vert2=(str(tm) + str(cm) + str(bm))
        vert3=(str(tr) + str(cr) + str(br))
        if str(top_row) == "xxx":
           print("Player X wins")
           print("Loading New Game...")
           print("New Game Loaded.")
           break
           break
        if str(top_row) == "ooo":
           print("Player O wins")
           print("Loading New Game...")
           print("New Game Loaded.")
           break
           break
        if str(mid_row) == "xxx":
           print("Player X wins")
           print("Loading New Game...")
           print("New Game Loaded.")
           break
           break
        if str(mid_row) == "ooo":
           print("Player O wins")
           print("Loading New Game...")
           print("New Game Loaded.")
           break
           break
        if str(bottom_row) == "xxx":
           print("Player X wins")
           print("Loading New Game...")
           print("New Game Loaded.")
           break
           break
        if str(bottom_row) == "ooo":
           print("Player O wins")
           print("Loading New Game...")
           print("New Game Loaded.")
           break
           break
        if str(diag1) == "xxx":
           print("Player X wins")
           print("Loading New Game...")
           print("New Game Loaded.")
           break
           break
        if str(diag2) == "ooo":
           print("Player O wins")
           print("Loading New Game...")
           print("New Game Loaded.")
           break
           break
        if str(vert1) == "xxx":
           print("Player X wins")
           print("Loading New Game...")
           print("New Game Loaded.")
           break
           break
        if str(vert1) == "ooo":
           print("Player O wins")
           print("Loading New Game...")
           print("New Game Loaded.")
           break
           break
        if str(vert2) == "xxx":
           print("Player X wins")
           print("Loading New Game...")
           print("New Game Loaded.")
           break
           break
        if str(vert2) == "ooo":
           print("Player O wins")
           print("Loading New Game...")
           print("New Game Loaded.")
           break
           break
        if str(vert3) == "xxx":
           print("Player X wins")
           print("Loading New Game...")
           print("New Game Loaded.")
           break
           break
        if str(vert3) == "ooo":
           print("Player O wins")
           print("Loading New Game...")
           print("New Game Loaded.")
           break
        user_input=input("You:  ")
        
        #top row
        if tl == "o":
           if tm == "o":
              if tr == "o":
                owins = 2
        elif tl == "x":
           if tm == "x":
              if tr == "x":
                 xwins = 2
        #middle row
        elif cl == "x":
           if cm == "x":
              if cr == "x":
                xwins = 2
        elif cl == "o":
           if cm == "o":
              if cr == "o":
                owins = 2
        #bottom row
        elif bl == "x":
           if bm == "x":
              if br == "x":
                 xwins = 2
        elif bl == "o":
           if bm == "o":
              if br == "o":
                 owins = 2
        #diagonal 1
        elif tl == "x":
           if cm == "x":
              if br == "x":
                 xwins = 2
        elif tl == "o":
           if cm == "o":
              if br == "o":
                 owins = 2

        #diagonal 2
        elif tr == "x":
           if cm == "x":
              if bl == "x":
                 xwins = 2
        elif tr == "o":
           if cm == "o":
              if bl == "o":
                 owins = 2

        #vertical 1
        elif tl == "x":
           if cl == "x":
              if bl == "x":
                 xwins = 2
        elif tl == "o":
           if cl == "o":
              if bl == "o":
                 owins = 2

        #vertical 2
        elif tm == "x":
           if cm == "x":
              if bm == "x":
                 xwins = 2
        elif tm == "o":
           if cm == "o":
              if bm == "o":
                 owins = 2

        #vertical 3
        elif tr == "x":
           if cr == "x":
              if br == "x":
                 xwins = 2
        elif tr == "o":
           if cr == "o":
              if br == "o":
                 owins = 2

        

    
               
        while True:
            if user_input == "1":
                if tl == 0:
                   if turn == 1:
                    tl = "x"
                    turn = 1
                    import random
                    aimove = [("tl", tl), ("tr", tr), ("tm", tm), ("cl", cl), ("cr", cr), ("cm", cm), ("bl", bl), ("br", br), ("bm", bm)]
                    ai = random.choice(aimove)
                    if ai[0] == "tl":
                        if tl == 0:
                            tl = "o"
                    elif ai[0] == "tm":
                        if tm == 0:
                            tm = "o"
                    elif ai[0] == "tr":
                        if tl == 0:
                            tr = "o"
                    if ai[0] == "cl":
                        if cl == 0:
                            cl = "o"
                    elif ai[0] == "cm":
                        if cm == 0:
                            cm = "o"
                    elif ai[0] == "cr":
                        if cr == 0:
                            cr = "o"
                    if ai[0] == "bl":
                        if bl == 0:
                            bl = "o"
                    elif ai[0] == "bm":
                        if bm == 0:
                            bm = "o"
                    elif ai[0] == "br":
                        if br == 0:
                            br = "o"
                    import random
                    aimove = [("tl", tl), ("tr", tr), ("tm", tm), ("cl", cl), ("cr", cr), ("cm", cm), ("bl", bl), ("br", br), ("bm", bm)]
                    ai = random.choice(aimove)
                    if ai[0] == "tl":
                        if tl == 0:
                            tl = "o"
                    elif ai[0] == "tm":
                        if tm == 0:
                            tm = "o"
                    elif ai[0] == "tr":
                        if tl == 0:
                            tr = "o"
                    if ai[0] == "cl":
                        if cl == 0:
                            cl = "o"
                    elif ai[0] == "cm":
                        if cm == 0:
                            cm = "o"
                    elif ai[0] == "cr":
                        if cr == 0:
                            cr = "o"
                    if ai[0] == "bl":
                        if bl == 0:
                            bl = "o"
                    elif ai[0] == "bm":
                        if bm == 0:
                            bm = "o"
                    elif ai[0] == "br":
                        if br == 0:
                            br = "o"
                    top_row=(str(tl) + str(tm) + str(tr))
                    mid_row=(str(cl) + str(cm) + str(cr))
                    bottom_row=(str(bl) + str(bm) + str(br))
                    print(str(top_row))
                    print(str(mid_row))
                    print(str(bottom_row))
                    if owins == "2":
                      print("Player  O wins!")
                      break
                    elif xwins == "2":
                      print ("Player X wins!")
                      break
                    else:
                      break
                   
                else:
                    print("Sorry, you can't do that move")
                    break

            elif user_input == "2":
                if tm == 0:
                   if turn == 1:
                    tm = "x"
                    turn = 1
                    import random
                    aimove = [("tl", tl), ("tr", tr), ("tm", tm), ("cl", cl), ("cr", cr), ("cm", cm), ("bl", bl), ("br", br), ("bm", bm)]
                    ai = random.choice(aimove)
                    if ai[0] == "tl":
                        if tl == 0:
                            tl = "o"
                    elif ai[0] == "tm":
                        if tm == 0:
                            tm = "o"
                    elif ai[0] == "tr":
                        if tl == 0:
                            tr = "o"
                    if ai[0] == "cl":
                        if cl == 0:
                            cl = "o"
                    elif ai[0] == "cm":
                        if cm == 0:
                            cm = "o"
                    elif ai[0] == "cr":
                        if cr == 0:
                            cr = "o"
                    if ai[0] == "bl":
                        if bl == 0:
                            bl = "o"
                    elif ai[0] == "bm":
                        if bm == 0:
                            bm = "o"
                    elif ai[0] == "br":
                        if br == 0:
                            br = "o"
                     
                    top_row=(str(tl) + str(tm) + str(tr))
                    mid_row=(str(cl) + str(cm) + str(cr))
                    bottom_row=(str(bl) + str(bm) + str(br))
                    print(str(top_row))
                    print(str(mid_row))
                    print(str(bottom_row))
                    if owins == "2":
                      print("Player  O wins!")
                      break
                    elif xwins == "2":
                      print ("Player X wins!")
                      break
                    else:
                      break
                   
                else:
                    print("Sorry, you can't do that move")
                    break

            elif user_input == "3":
                if tr == 0:
                   if turn == 1:
                    tr = "x"
                    turn = 1
                    import random
                    aimove = [("tl", tl), ("tr", tr), ("tm", tm), ("cl", cl), ("cr", cr), ("cm", cm), ("bl", bl), ("br", br), ("bm", bm)]
                    ai = random.choice(aimove)
                    if ai[0] == "tl":
                        if tl == 0:
                            tl = "o"
                    elif ai[0] == "tm":
                        if tm == 0:
                            tm = "o"
                    elif ai[0] == "tr":
                        if tl == 0:
                            tr = "o"
                    if ai[0] == "cl":
                        if cl == 0:
                            cl = "o"
                    elif ai[0] == "cm":
                        if cm == 0:
                            cm = "o"
                    elif ai[0] == "cr":
                        if cr == 0:
                            cr = "o"
                    if ai[0] == "bl":
                        if bl == 0:
                            bl = "o"
                    elif ai[0] == "bm":
                        if bm == 0:
                            bm = "o"
                    elif ai[0] == "br":
                        if br == 0:
                            br = "o"
                     
                    top_row=(str(tl) + str(tm) + str(tr))
                    mid_row=(str(cl) + str(cm) + str(cr))
                    bottom_row=(str(bl) + str(bm) + str(br))
                    print(str(top_row))
                    print(str(mid_row))
                    print(str(bottom_row))
                    if owins == "2":
                      print("Player  O wins!")
                      break
                    elif xwins == "2":
                      print ("Player X wins!")
                      break
                    else:
                      break
                  
                else:
                    print("Sorry, you can't do that move")
                    break


            elif user_input == "4":
                if cl == 0:
                   if turn == 1:
                    cl = "x"
                    turn = 1
                    import random
                    aimove = [("tl", tl), ("tr", tr), ("tm", tm), ("cl", cl), ("cr", cr), ("cm", cm), ("bl", bl), ("br", br), ("bm", bm)]
                    ai = random.choice(aimove)
                    if ai[0] == "tl":
                        if tl == 0:
                            tl = "o"
                    elif ai[0] == "tm":
                        if tm == 0:
                            tm = "o"
                    elif ai[0] == "tr":
                        if tl == 0:
                            tr = "o"
                    if ai[0] == "cl":
                        if cl == 0:
                            cl = "o"
                    elif ai[0] == "cm":
                        if cm == 0:
                            cm = "o"
                    elif ai[0] == "cr":
                        if cr == 0:
                            cr = "o"
                    if ai[0] == "bl":
                        if bl == 0:
                            bl = "o"
                    elif ai[0] == "bm":
                        if bm == 0:
                            bm = "o"
                    elif ai[0] == "br":
                        if br == 0:
                            br = "o"
                     
                    top_row=(str(tl) + str(tm) + str(tr))
                    mid_row=(str(cl) + str(cm) + str(cr))
                    bottom_row=(str(bl) + str(bm) + str(br))
                    print(str(top_row))
                    print(str(mid_row))
                    print(str(bottom_row))
                    if owins == "2":
                      print("Player  O wins!")
                      break
                    elif xwins == "2":
                      print ("Player X wins!")
                      break
                    else:
                      break
                 
                else:
                    print("Sorry, you can't do that move")
                    break

            elif user_input == "5":
                if cm == 0:
                   if turn == 1:
                    cm = "x"
                    turn = 1
                    import random
                    aimove = [("tl", tl), ("tr", tr), ("tm", tm), ("cl", cl), ("cr", cr), ("cm", cm), ("bl", bl), ("br", br), ("bm", bm)]
                    ai = random.choice(aimove)
                    if ai[0] == "tl":
                        if tl == 0:
                            tl = "o"
                    elif ai[0] == "tm":
                        if tm == 0:
                            tm = "o"
                    elif ai[0] == "tr":
                        if tl == 0:
                            tr = "o"
                    if ai[0] == "cl":
                        if cl == 0:
                            cl = "o"
                    elif ai[0] == "cm":
                        if cm == 0:
                            cm = "o"
                    elif ai[0] == "cr":
                        if cr == 0:
                            cr = "o"
                    if ai[0] == "bl":
                        if bl == 0:
                            bl = "o"
                    elif ai[0] == "bm":
                        if bm == 0:
                            bm = "o"
                    elif ai[0] == "br":
                        if br == 0:
                            br = "o"
                     
                    top_row=(str(tl) + str(tm) + str(tr))
                    mid_row=(str(cl) + str(cm) + str(cr))
                    bottom_row=(str(bl) + str(bm) + str(br))
                    print(str(top_row))
                    print(str(mid_row))
                    print(str(bottom_row))
                    if owins == "2":
                      print("Player  O wins!")
                      break
                    elif xwins == "2":
                      print ("Player X wins!")
                      break
                    else:
                      break
                   
                else:
                    print("Sorry, you can't do that move")
                    break

            elif user_input == "6":
                if cr == 0:
                   if turn == 1:
                    cr = "x"
                    turn = 1
                    import random
                    aimove = [("tl", tl), ("tr", tr), ("tm", tm), ("cl", cl), ("cr", cr), ("cm", cm), ("bl", bl), ("br", br), ("bm", bm)]
                    ai = random.choice(aimove)
                    if ai[0] == "tl":
                        if tl == 0:
                            tl = "o"
                    elif ai[0] == "tm":
                        if tm == 0:
                            tm = "o"
                    elif ai[0] == "tr":
                        if tl == 0:
                            tr = "o"
                    if ai[0] == "cl":
                        if cl == 0:
                            cl = "o"
                    elif ai[0] == "cm":
                        if cm == 0:
                            cm = "o"
                    elif ai[0] == "cr":
                        if cr == 0:
                            cr = "o"
                    if ai[0] == "bl":
                        if bl == 0:
                            bl = "o"
                    elif ai[0] == "bm":
                        if bm == 0:
                            bm = "o"
                    elif ai[0] == "br":
                        if br == 0:
                            br = "o"
                     
                    top_row=(str(tl) + str(tm) + str(tr))
                    mid_row=(str(cl) + str(cm) + str(cr))
                    bottom_row=(str(bl) + str(bm) + str(br))
                    print(str(top_row))
                    print(str(mid_row))
                    print(str(bottom_row))
                    if owins == "2":
                      print("Player  O wins!")
                      break
                   
                else:
                    print("Sorry, you can't do that move")
                    break

            elif user_input == "7":
                if bl == 0:
                   if turn == 1:
                    bl = "x"
                    turn = 1
                    import random
                    aimove = [("tl", tl), ("tr", tr), ("tm", tm), ("cl", cl), ("cr", cr), ("cm", cm), ("bl", bl), ("br", br), ("bm", bm)]
                    ai = random.choice(aimove)
                    if ai[0] == "tl":
                        if tl == 0:
                            tl = "o"
                    elif ai[0] == "tm":
                        if tm == 0:
                            tm = "o"
                    elif ai[0] == "tr":
                        if tl == 0:
                            tr = "o"
                    if ai[0] == "cl":
                        if cl == 0:
                            cl = "o"
                    elif ai[0] == "cm":
                        if cm == 0:
                            cm = "o"
                    elif ai[0] == "cr":
                        if cr == 0:
                            cr = "o"
                    if ai[0] == "bl":
                        if bl == 0:
                            bl = "o"
                    elif ai[0] == "bm":
                        if bm == 0:
                            bm = "o"
                    elif ai[0] == "br":
                        if br == 0:
                            br = "o"
                     
                    top_row=(str(tl) + str(tm) + str(tr))
                    mid_row=(str(cl) + str(cm) + str(cr))
                    bottom_row=(str(bl) + str(bm) + str(br))
                    print(str(top_row))
                    print(str(mid_row))
                    print(str(bottom_row))
                    if owins == "2":
                      print("Player  O wins!")
                      break
                    elif xwins == "2":
                      print ("Player X wins!")
                      break
                    else:
                      break
                  
                else:
                    print("Sorry, you can't do that move")
                    break

            elif user_input == "8":
                if bm == 0:
                   if turn == 1:
                    bm = "x"
                    turn = 1
                    import random
                    aimove = [("tl", tl), ("tr", tr), ("tm", tm), ("cl", cl), ("cr", cr), ("cm", cm), ("bl", bl), ("br", br), ("bm", bm)]
                    ai = random.choice(aimove)
                    if ai[0] == "tl":
                        if tl == 0:
                            tl = "o"
                    elif ai[0] == "tm":
                        if tm == 0:
                            tm = "o"
                    elif ai[0] == "tr":
                        if tl == 0:
                            tr = "o"
                    if ai[0] == "cl":
                        if cl == 0:
                            cl = "o"
                    elif ai[0] == "cm":
                        if cm == 0:
                            cm = "o"
                    elif ai[0] == "cr":
                        if cr == 0:
                            cr = "o"
                    if ai[0] == "bl":
                        if bl == 0:
                            bl = "o"
                    elif ai[0] == "bm":
                        if bm == 0:
                            bm = "o"
                    elif ai[0] == "br":
                        if br == 0:
                            br = "o"
                     
                    top_row=(str(tl) + str(tm) + str(tr))
                    mid_row=(str(cl) + str(cm) + str(cr))
                    bottom_row=(str(bl) + str(bm) + str(br))
                    print(str(top_row))
                    print(str(mid_row))
                    print(str(bottom_row))
                    if owins == "2":
                      print("Player  O wins!")
                      break
                    elif xwins == "2":
                      print ("Player X wins!")
                      break
                    else:
                      break
                   
                else:
                    print("Sorry, you can't do that move")
                    break

            elif user_input == "9":
                if br == 0:
                   if turn == 1:
                    br = "x"
                    turn = 1
                    import random
                    aimove = [("tl", tl), ("tr", tr), ("tm", tm), ("cl", cl), ("cr", cr), ("cm", cm), ("bl", bl), ("br", br), ("bm", bm)]
                    ai = random.choice(aimove)
                    if ai[0] == "tl":
                        if tl == 0:
                            tl = "o"
                    elif ai[0] == "tm":
                        if tm == 0:
                            tm = "o"
                    elif ai[0] == "tr":
                        if tl == 0:
                            tr = "o"
                    if ai[0] == "cl":
                        if cl == 0:
                            cl = "o"
                    elif ai[0] == "cm":
                        if cm == 0:
                            cm = "o"
                    elif ai[0] == "cr":
                        if cr == 0:
                            cr = "o"
                    if ai[0] == "bl":
                        if bl == 0:
                            bl = "o"
                    elif ai[0] == "bm":
                        if bm == 0:
                            bm = "o"
                    elif ai[0] == "br":
                        if br == 0:
                            br = "o"
                     
                    top_row=(str(tl) + str(tm) + str(tr))
                    mid_row=(str(cl) + str(cm) + str(cr))
                    bottom_row=(str(bl) + str(bm) + str(br))
                    print(str(top_row))
                    print(str(mid_row))
                    print(str(bottom_row))
                    if owins == "2":
                      print("Player  O wins!")
                      break
                    elif xwins == "2":
                      print ("Player X wins!")
                      break
                    else:
                      break
                  
                else:
                    print("Sorry, you can't do that move")
                    break




            