DIRECTIONS = ['N', 'E', 'S', 'W']

MOVES_CONF = {
    'N': ('y',1),
    'S': ('y',-1),
    'E': ('x',1),
    'W': ('x',-1)
}

ASSIGNS = {
    'L': 'left',
    'R': 'right',
    'M': 'move'
}


class Rover(object):

    def __init__(self, initial_pos, commands, controller):
        self.pos = {
            'x': int(initial_pos[0]),
            'y': int(initial_pos[1]),
            'f': initial_pos[2]
        }
        self.commands = commands
        self.controller = controller

    def left(self):
        i = DIRECTIONS.index(self.pos['f'])
        i = (len(DIRECTIONS) - 1) if i == 0 else i - 1
        self.pos['f'] = DIRECTIONS[i]

    def right(self):
        i = DIRECTIONS.index(self.pos['f'])
        i = 0 if i == (len(DIRECTIONS) -1 ) else i + 1
        self.pos['f'] = DIRECTIONS[i]

    def move(self):
        m = MOVES_CONF[self.pos['f']]
        next_pos = dict(self.pos)
        next_pos[m[0]] += m[1]
        if self.controller.can_move(next_pos):
            self.pos = next_pos
        else:
            raise ValueError('Rovers positions conflict')

    def get_pos(self):
        return self.pos

    def execute_path(self):
        for d in self.commands:
            getattr(self, ASSIGNS[d])()
        return "{0} {1} {2}".format(self.pos['x'], self.pos['y'], self.pos['f'])
