import argparse

from rover_controller import RoverController


def main(txt_path):

    r_c = RoverController(txt_path)
    res = r_c.perform_commands()

    print('\n'.join(res))
    return '\n'.join(res)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("txt_path", help="Path to the input file")
    args = parser.parse_args()

    main(args.txt_path)