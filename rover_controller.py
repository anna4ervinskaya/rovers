import re

from rover import Rover

PLATEAU_LIMITS = r"^(\d+\s\d+)"

POSITION_PATTERN = r"^(\d+\s\d+\s[NEWS])"

COMMANDS_PATTERN = r"^([LMR]+)"


class RoverController(object):

    def __init__(self, input_txt_path):
        with open(input_txt_path) as f:
            lines = f.read().splitlines()
            if not len(lines) or (len(lines) - 1) % 2 != 0:
                raise ValueError('No input data')

            if (re.sub(PLATEAU_LIMITS,'',lines[0])):
                raise ValueError('Plateau limits data is not correct')

            self.pl_limits = {
                'x': int(lines[0].split(' ')[0]),
                'y': int(lines[0].split(' ')[1])
            }

            self.rovers = list()

            i = 1
            while(i < len(lines)):
                if re.sub(POSITION_PATTERN, '', lines[i]):
                    raise ValueError('Rover position data is not correct')
                if re.sub(COMMANDS_PATTERN, '', lines[i+1]):
                    raise ValueError('Rover commands data is not correct')

                pos_ar = lines[i].split(' ')
                init_pos = (pos_ar[0], pos_ar[1], pos_ar[2])
                r = Rover(init_pos, lines[i+1], self)
                self.attach_rover(r)
                i += 2

    def perform_commands(self):
        result = list()
        for r in self.rovers:
            result.append(r.execute_path())
        return result

    def attach_rover(self, Rover):
        self.rovers.append(Rover)

    def can_move(self, pos):
        res = True
        if pos['x'] > self.pl_limits['x'] or pos['y'] > self.pl_limits['y']:
            res = False
            print(1)
            return res
        for r in self.rovers:
            if pos['x'] == r.get_pos()['x'] and pos['y'] == r.get_pos()['y']:
                res = False
                break
        return res