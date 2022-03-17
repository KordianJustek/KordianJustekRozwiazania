import time, sys
ident = 0
identincresing = True

try:
    while True:
        print(' c' * ident, end='')
        print("**********")
        time.sleep(0.1)

        if identincresing:
            ident +=1
            if ident == 20:
                identincresing = False
        else:
            ident -=1
            if ident == 0:
                identincresing = True
except KeyboardInterrupt:
    sys.exit()
