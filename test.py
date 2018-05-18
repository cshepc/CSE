warning1_water = False
warning2_water = False
warning3_water = False
warning1_water = False
warning2_water = False
warning3_water = False
a = True

while a:
    if not warning1_water:
        warning1_water = True
        print("water 1")
    else:
        if not warning2_water:
            warning2_water = True
            print("water 2")
        else:
            if not warning3_water:
                warning3_water = True
                print("water 3")
                a = False
