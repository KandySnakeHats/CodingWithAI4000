import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR
from gui import GUI
from game import TicTacToeGame

def main():
    # Initialize Pygame and create a window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tic-Tac-Toe")

    # Create game logic and GUI instances
    game = TicTacToeGame()
    gui = GUI(screen, game)

    # Main game loop
    running = True
    while running:
        running = gui.handle_events()  # Handle user input
        gui.draw()                     # Draw the updated game state

        pygame.display.flip()          # Update the display

    pygame.quit()

if __name__ == "__main__":
    main()
