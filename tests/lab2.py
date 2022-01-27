from scripts import config

LAB_DIR = '../Final-Lab_2'
SOL_PATH = 'solutions/lab2_sol'
CONFIG_DICT = {
    'mastermind.MasterMind': {
        'mastermind-in-1234.txt': 1234,
        'mastermind-in-7483.txt': 7438,
    }
}


def main():
    config.execute(LAB_DIR, SOL_PATH, CONFIG_DICT)


if __name__ == '__main__':
    main()
