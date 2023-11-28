import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE
from nqueens import NQueenProblem


class NQueensGUI:
    def __init__(self, num_queens):
        pygame.init()

        self.num_queens = num_queens
        self.screen_size = self.num_queens * 40
        self.delay = 0

        self.solver = NQueenProblem(self.num_queens)

        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        pygame.display.set_caption("N-Queens Solver")

        self.queen_image = pygame.image.load("nqueens/images/queen.png")
        self.queen_image = pygame.transform.scale(self.queen_image, (40, 40))

        self.solve_and_visualize()

    def solve_and_visualize(self):
        self.solve_and_visualize_util(0)
        pygame.quit()

    def solve_and_visualize_util(self, col):
        if col == self.num_queens:
            self.visualize_solution()
            pygame.time.delay(self.delay)
            pygame.display.flip()
            self.wait_for_key_press()
            return True

        for i in range(self.num_queens):
            if self.solver.is_safe(i, col):
                self.solver.board[i][col] = 1
                self.visualize_solution()
                pygame.time.delay(self.delay)
                pygame.display.flip()

                if self.solve_and_visualize_util(col + 1):
                    return True

                self.solver.board[i][col] = 0

        self.visualize_solution()

        return False

    def visualize_solution(self):
        self.screen.fill((255, 255, 255))

        for i in range(self.num_queens):
            for j in range(self.num_queens):
                color = (255, 255, 255) if (i + j) % 2 == 0 else (0, 0, 0)
                pygame.draw.rect(
                    self.screen,
                    color,
                    (j * 40, i * 40, 40, 40),
                )

        for i in range(self.num_queens):
            for j in range(self.num_queens):
                if self.solver.board[i][j] == 1:
                    self.screen.blit(
                        self.queen_image,
                        (j * 40, i * 40),
                    )

        pygame.display.flip()

    def wait_for_key_press(self):
        waiting_for_key = True
        while waiting_for_key:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN and event.key == K_SPACE:
                    waiting_for_key = False


def main():
    num_queens = 16
    gui = NQueensGUI(num_queens)


if __name__ == "__main__":
    main()