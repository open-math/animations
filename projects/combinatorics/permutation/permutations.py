from manim import *
import itertools

config.frame_size = (380,150)

class Permutations(MovingCameraScene):
    def construct(self):
        letter_data = [
            ("A", RED),
            ("B", GREEN),
            ("C", BLUE),
        ]

        letters = VGroup()
        squares = VGroup()

        for letter, letter_color in letter_data:
            letters.add(Text(letter, font_size=80, color=letter_color))
            squares.add(Square().set_stroke(WHITE, 10))

        #
        # Setting up scene
        #

        squares.arrange(RIGHT, .5)
        self.add(squares)

        for i, letter in enumerate(letters):
            letter.move_to(squares[i])

        self.add(letters)
        (squares + letters).scale(2)

        #
        # Loop permutations
        #

        self.wait(1)
        for permutation in reversed(list(itertools.permutations(letters))):
            anims = []
            for i, letter in enumerate(permutation):
                anims.append(letter.animate.move_to(squares[i]))

            self.play(*anims, run_time=.5)
            self.wait(.5)