import time

# a simple way to say "Hello world" in Python
tmps1 = time.process_time()
print("Hello world")
tmps2 = time.process_time()
print("simple way : %f secondes" % (tmps2 - tmps1))

# a complex way to say "Hello world" in Python
tmps1 = time.process_time()
x = 0
while x < 12 :
    if x ==1:
        print("H", end='')
    elif x == 2:
        print("e", end='')
    elif x == 3:
        print("l", end='')
    elif x == 4:
        print("l", end='')
    elif x == 5:
        print("o", end='')
    elif x == 6:
        print(" ", end='')
    elif x == 7:
        print("w", end='')
    elif x == 8:
        print("o", end='')
    elif x == 9:
        print("r", end='')
    elif x == 10:
        print("l", end='')
    elif x == 11:
        print("d")
    x = x + 1
tmps2 = time.process_time()
print("complicated way : %f secondes" % (tmps2 - tmps1))
