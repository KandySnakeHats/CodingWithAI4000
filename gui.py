import pygame
from config import BG_COLOR, LINE_COLOR, X_COLOR, O_COLOR, FONT, SCREEN_WIDTH, SCREEN_HEIGHT

CELL_SIZE = SCREEN_WIDTH // 3

class GUI:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

    def handle_events(self):
        """Handle mouse clicks and exit events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and not self.game.winner:
                x, y = pygame.mouse.get_pos()
                row, col = y // CELL_SIZE, x // CELL_SIZE
                self.game.make_move(row, col)
        return True

    def draw(self):
        """Draw the board, grid, and players' moves"""
        self.screen.fill(BG_COLOR)
        self.draw_grid()
        self.draw_moves()

        # Display winner or draw
        if self.game.winner:
            self.draw_text(f"Player {self.game.winner} wins!")
        elif self.game.is_draw():
            self.draw_text("It's a draw!")

    def draw_grid(self):
        """Draw the grid for Tic-Tac-Toe"""
        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (0, CELL_SIZE * i), (SCREEN_WIDTH, CELL_SIZE * i), 3)
            pygame.draw.line(self.screen, LINE_COLOR, (CELL_SIZE * i, 0), (CELL_SIZE * i, SCREEN_HEIGHT), 3)

    def draw_moves(self):
        """Draw 'X' and 'O' on the board"""
        for row in range(3):
            for col in range(3):
                move = self.game.board[row][col]
                if move == 'X':
                    self.draw_x(row, col)
                elif move == 'O':
                    self.draw_o(row, col)

    def draw_x(self, row, col):
        """Draw an 'X' at the specified board position"""
        x_center = col * CELL_SIZE + CELL_SIZE // 2
        y_center = row * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.line(self.screen, X_COLOR, (x_center - 40, y_center - 40), (x_center + 40, y_center + 40), 5)
        pygame.draw.line(self.screen, X_COLOR, (x_center + 40, y_center - 40), (x_center - 40, y_center + 40), 5)

    def draw_o(self, row, col):
        """Draw an 'O' at the specified board position"""
        x_center = col * CELL_SIZE + CELL_SIZE // 2
        y_center = row * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.circle(self.screen, O_COLOR, (x_center, y_center), 40, 5)

    def draw_text(self, text):
        """Display text in the middle of the screen"""
        font = pygame.font.Font(FONT, 64)
        text_surface = font.render(text, True, X_COLOR)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text_surface, text_rect)
