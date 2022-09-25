for a in (True, False):
    for b in (True, False):
        for c in (True, False):
            if ((not a) or (not b) or (not c)) and (not ((not a) and (not b))):
                print(a, b, c)