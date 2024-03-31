from manim import *

config.frame_size = (500, 500)
config.frame_width = 5
config.frame_rate = 60
config.format = 'webm'
config.transparent = True

class SquareGrid(VMobject):
    def __init__(self, n: int, **kwargs):
        super().__init__(**kwargs)

        self.n = n
        self.squares = []

        for x in range(n):
            for y in range(n):
                square = Square(1, stroke_width=10)
                square.move_to([x,n-y-1,0])
                self.squares.append(square)
                self.add(square)
    
    def coords_to_index(self, coords: List):
        return coords[0] * self.n + coords[1]

    def highlight_rectangle(self, vertex1, vertex2) -> AnimationGroup:
        coords_list = []
        for x in range(min(vertex1[0], vertex2[0]), max(vertex1[0], vertex2[0]) + 1):
            for y in range(min(vertex1[1], vertex2[1]), max(vertex1[1], vertex2[1]) + 1):
                coords_list.append([x,y])

        squares = []
        for coords in coords_list:
            squares.append(self.squares[self.coords_to_index(coords)])

        return AnimationGroup(
            *[square.set_z_index(10).animate.set_fill(BLUE, .5).set_color(BLUE_D) for square in squares],
            run_time=.5
        )

    def clear_hightlight(self) -> AnimationGroup:
        return AnimationGroup(
            *[square.animate.set_fill(WHITE, 0).set_color(WHITE).set_z_index(0) for square in self.squares],
            run_time=.5
        )

class RectanglesInSquare(Scene):
    def construct(self):
        n = 4

        grid = SquareGrid(n)

        node = Circle(.2, GREEN)
        node.set_fill(GREEN, 1)
        node.set_z_index(20)
        node.move_to([1 - .5, n - 1 + .5, 0])

        scene = VGroup(grid, node)
        scene.move_to(ORIGIN)
        self.add(scene)

        #

        for x in range(n-1):
            self.play(grid.highlight_rectangle([1,0], [x+1,0]))
            self.wait(.5)
            self.play(grid.clear_hightlight())

        for x in range(n-1):
            self.play(grid.highlight_rectangle([1,0], [x+1,1]))
            self.wait(.5)
            self.play(grid.clear_hightlight())

        for x in range(n-1):
            self.play(grid.highlight_rectangle([1,0], [x+1,2]))
            self.wait(.5)
            self.play(grid.clear_hightlight())

        self.wait(3)