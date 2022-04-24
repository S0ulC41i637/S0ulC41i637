# This is my first 8V engine. I'm thinking of
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


# pistons = (1, 2, 3, 4, 8, 7, 6, 5)
# position = ('button', 'top', 'mid')
# times = (1, 2, 3, 4)

p1 = Piston('mid', 1, '', '1', False)
p8 = Piston('mid', 3, '', '8', False)
p2 = Piston('mid', 1, '', '2', False)
p7 = Piston('mid', 3, '', '7', False)
p3 = Piston('mid', 1, '', '3', False)
p6 = Piston('mid', 3, '', '6', False)
p4 = Piston('mid', 1, '', '4', False)
p5 = Piston('mid', 3, '', '5', False)


rev = 359
limit = 10
v = -1
cmd = ''

while True:
    print('')
    cmd = input('>>> ').lower()
    print('')
    if cmd == 'start':
        while not v == limit:
            if rev == 359:
                rev = 0
                v += 1
                if rev == 0 and p1.time_of_the_piston == 1 and p8.time_of_the_piston == 3:
                    p1.admission()
                    p8.expansion()
                if rev == 0 and p1.time_of_the_piston == 3 and p8.time_of_the_piston == 1:
                    p1.expansion()
                    p8.admission()

            if rev < 359:
                rev += 1
                if rev == 45 and p2.time_of_the_piston == 1 and p7.time_of_the_piston == 3:
                    p2.admission()
                    p7.expansion()
                if rev == 45 and p2.time_of_the_piston == 3 and p7.time_of_the_piston == 1:
                    p2.expansion()
                    p7.admission()
                if rev == 90 and p3.time_of_the_piston == 1 and p6.time_of_the_piston == 3:
                    p3.admission()
                    p6.expansion()
                if rev == 90 and p3.time_of_the_piston == 3 and p6.time_of_the_piston == 1:
                    p3.expansion()
                    p6.admission()
                if rev == 135 and p4.time_of_the_piston == 1 and p5.time_of_the_piston == 3:
                    p4.admission()
                    p5.expansion()
                if rev == 135 and p4.time_of_the_piston == 3 and p5.time_of_the_piston == 1:
                    p4.expansion()
                    p5.admission()
                if rev == 180 and p1.time_of_the_piston == 2 and p8.time_of_the_piston == 4:
                    p1.compression()
                    p8.scape()
                if rev == 180 and p1.time_of_the_piston == 4 and p8.time_of_the_piston == 2:
                    p1.scape()
                    p8.compression()
                if rev == 225 and p2.time_of_the_piston == 2 and p7.time_of_the_piston == 4:
                    p2.compression()
                    p7.scape()
                if rev == 225 and p2.time_of_the_piston == 4 and p7.time_of_the_piston == 2:
                    p2.scape()
                    p7.compression()
                if rev == 270 and p3.time_of_the_piston == 2 and p6.time_of_the_piston == 4:
                    p3.compression()
                    p6.scape()
                if rev == 270 and p3.time_of_the_piston == 4 and p6.time_of_the_piston == 2:
                    p3.scape()
                    p6.compression()
                if rev == 315 and p4.time_of_the_piston == 2 and p5.time_of_the_piston == 4:
                    p4.compression()
                    p5.scape()
                if rev == 315 and p4.time_of_the_piston == 4 and p5.time_of_the_piston == 2:
                    p4.scape()
                    p5.compression()

        else:
            rev = 359
            limit = 10
            v = -1

    elif cmd == 'reset':
        print('''Done
        ''')
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
        p5.admission()
        p5.compression()
        p5.expansion()
        p5.scape()
        p6.admission()
        p6.compression()
        p6.expansion()
        p6.scape()
        p7.admission()
        p7.compression()
        p7.expansion()
        p7.scape()
        p8.admission()
        p8.compression()
        p8.expansion()
        p8.scape()
        p1 = Piston('mid', 1, '', '1', False)
        p8 = Piston('mid', 3, '', '8', False)
        p2 = Piston('mid', 1, '', '2', False)
        p7 = Piston('mid', 3, '', '7', False)
        p3 = Piston('mid', 1, '', '3', False)
        p6 = Piston('mid', 3, '', '6', False)
        p4 = Piston('mid', 1, '', '4', False)
        p5 = Piston('mid', 3, '', '5', False)

    elif cmd == 'quit':
        print('Shutting down...')
        break

    elif cmd == 'help':
        print('''
    start - starts the engine simulator
    quit - Exit the engine simulator
    help - Shows commands
        ''')

    else:
        print('Invalid command. type help for commands.')
