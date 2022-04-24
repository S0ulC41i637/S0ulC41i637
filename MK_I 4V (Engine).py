# This is my first 4V engine. I'm thinking of
# making an app that help us find data about
# the status of pistons!


class Piston:
    def __init__(self, position_of_the_piston, time_of_the_piston, var_ex, var_re, on):
        self.position_of_the_piston = position_of_the_piston
        self.time_of_the_piston = time_of_the_piston
        self.var_ex = var_ex
        self.var_re = var_re
        self.on = on

    def admission(self):
        self.position_of_the_piston = 'button'
        self.on = True
        self.time_of_the_piston = 1
        self.var_ex = 2
        self.time_of_the_piston = self.var_ex
        print(self.var_re)

    def compression(self):
        self.position_of_the_piston = 'top'
        self.time_of_the_piston = 2
        self.var_ex = 3
        self.time_of_the_piston = self.var_ex
        if self.on:
            print(self.var_re*2)

    def expansion(self):
        self.position_of_the_piston = 'button'
        self.time_of_the_piston = 3
        self.var_ex = 4
        self.time_of_the_piston = self.var_ex
        if self.on:
            print(self.var_re*3)

    def scape(self):
        self.position_of_the_piston = 'top'
        self.time_of_the_piston = 4
        self.var_ex = 1
        self.time_of_the_piston = self.var_ex
        if self.on:
            print(self.var_re*4)


# pistons = (1, 3, 4, 2)
# position = ('button', 'top', 'mid')
# times = (1, 2, 3, 4)

p1 = Piston('mid', 1, '', '1', False)
p4 = Piston('mid', 3, '', '4', False)
p3 = Piston('mid', 1, '', '3', False)
p2 = Piston('mid', 3, '', '2', False)

cmd = ''
rev = 359
limit = 43
v = -1

while True:
    print('')
    cmd = input('>>> ').lower()
    print('')
    if cmd == 'start':
        while not v == limit:
            if rev == 359:
                rev = 0
                v += 1
                if rev == 0 and p1.time_of_the_piston == 1 and p4.time_of_the_piston == 3:
                    p1.admission()
                    p4.expansion()
                if rev == 0 and p1.time_of_the_piston == 3 and p4.time_of_the_piston == 1:
                    p1.expansion()
                    p4.admission()

            if rev < 359:
                rev += 1
                if rev == 90 and p3.time_of_the_piston == 1 and p2.time_of_the_piston == 3:
                    p3.admission()
                    p2.expansion()
                if rev == 90 and p3.time_of_the_piston == 3 and p2.time_of_the_piston == 1:
                    p3.expansion()
                    p2.admission()
                if rev == 180 and p1.time_of_the_piston == 2 and p4.time_of_the_piston == 4:
                    p1.compression()
                    p4.scape()
                if rev == 180 and p1.time_of_the_piston == 4 and p4.time_of_the_piston == 2:
                    p1.scape()
                    p4.compression()
                if rev == 270 and p3.time_of_the_piston == 2 and p2.time_of_the_piston == 4:
                    p3.compression()
                    p2.scape()
                if rev == 270 and p3.time_of_the_piston == 4 and p2.time_of_the_piston == 2:
                    p3.scape()
                    p2.compression()

        else:
            rev = 359
            limit = 5
            v = -1

    elif cmd == 'reset':
        p1.admission()
        p1.compression()
        p1.expansion()
        p1.scape()
        p2.admission()
        p2.compression()
        p2.expansion()
        p2.scape()
        p3.admission()
        p3.compression()
        p3.expansion()
        p3.scape()
        p4.admission()
        p4.compression()
        p4.expansion()
        p4.scape()
        p1 = Piston('mid', 1, '', '1', False)
        p4 = Piston('mid', 3, '', '4', False)
        p3 = Piston('mid', 1, '', '3', False)
        p2 = Piston('mid', 3, '', '2', False)

    elif cmd == 'quit':
        print('Shutting down...')
        break

    elif cmd == 'help':
        print('''
    start - Starts the engine simulator
    quit - Exit the engine simulator
    reset - Resets the pistons
    help - Shows commands
        ''')

    else:
        print('Invalid command. type help for commands.')
