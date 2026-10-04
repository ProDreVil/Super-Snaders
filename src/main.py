import subprocess

from game.progression import start_game

def clear_screen():
    subprocess.run('cls', shell=True)

def main():
    clear_screen()
    start_game()
    print("\nTHIS IS THE END")

if __name__ == "__main__":
    main()