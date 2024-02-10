import math
from manim import *

#config.disable_caching = True
config.frame_size = (420, 480)

def fit(mob: VMobject, to: VMobject, buff: float = 0):
    mob.move_to(to)

    if (mob.width > mob.height):
        mob.scale_to_fit_width(to.width - buff)
    else:
        mob.scale_to_fit_height(to.height - buff)

class Cell(VMobject):
    def __init__(self, content: VMobject, **kwargs):
        super().__init__(**kwargs)

        self.square = Square()
        self.square.set_opacity(0)

        self.content = content
        self.content.add_updater(lambda mob: mob.move_to(self.square.get_center()))
        fit(self.content, self.square, 1)

        self.add(
            self.square,
            self.content
        )

class PascalTriangle(VMobject):
    def __init__(self, num_rows: int, buff = .5, **kwargs):
        super().__init__(**kwargs)

        self.rows = VGroup()
        self.to_fill_cell_indices = []

        for row_i in range(num_rows):
            cells: VGroup[Cell] = VGroup()

            for cell_i in range(row_i + 1):
                cell = Cell(Tex(f"{math.comb(row_i, cell_i)}"))
                cells.add(cell)

                if (cell_i != 0 and cell_i != row_i):
                    self.to_fill_cell_indices.append([row_i, cell_i])
                    cell.content.set_opacity(0)

            cells.arrange(buff=buff)
            self.rows.add(cells)

        self.rows.arrange(direction=DOWN, buff=buff)

        self.add(self.rows)

    def get(self, n: int, k: int) -> Cell:
        return self.rows[n][k]

##
##
##

class Calc(MovingCameraScene):
    def construct(self):
        triangle = PascalTriangle(5)
        self.camera.frame.set(height=triangle.height)
        triangle.move_to(ORIGIN)
        self.add(triangle)

        for binom in triangle.to_fill_cell_indices:
            self.cell_sum(
                triangle.get(binom[0]-1, binom[1]-1),
                triangle.get(binom[0]-1, binom[1]),
                triangle.get(binom[0],   binom[1])
            )

        self.wait(3)

        self.play(*[FadeOut(triangle.get(binom[0], binom[1])) for binom in triangle.to_fill_cell_indices])

        self.wait(.5)

    def cell_sum(self, cell_1: Cell, cell_2: Cell, target_cell: Cell):
        cell_1.content.save_state()
        cell_2.content.save_state()

        content_1 = cell_1.content.copy()
        content_2 = cell_2.content.copy()

        cell_1.content.set_opacity(0)
        cell_2.content.set_opacity(0)

        self.play(content_1.animate.set_color(YELLOW), content_2.animate.set_color(YELLOW), run_time=.5)

        cell_1.content.restore()
        cell_2.content.restore()

        sum = VGroup(
            Tex(content_1.tex_string),
            Tex("+").scale(.75).set_opacity(0),
            Tex(content_2.tex_string),
        )

        sum.arrange(buff=.1)
        fit(sum, target_cell, .5)

        a_move = AnimationGroup(
            Transform(content_1, sum[0], replace_mobject_with_target_in_scene=True),
            Transform(content_2, sum[2], replace_mobject_with_target_in_scene=True)
        )

        a_plus = sum[1].animate.set_opacity(1)

        self.play(
            a_move, a_plus,
            lag_ratio=.5
        )

        self.play(
            Transform(sum, target_cell.content.copy().set_opacity(1), run_time=.5)
        )

        self.remove(sum)
        target_cell.content.set_opacity(1)