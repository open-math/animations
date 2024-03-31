from manim import *
from pyramid import Pyramid

config.frame_size = (550 * 3, 480 * 3)

class SumOfSquaresAlternate(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(theta=-45 * DEGREES, phi=60 * DEGREES, zoom=1.75)

        #

        cuboid = VGroup()

        pyramid_blue = Pyramid(3, BLUE_D, 100).rotate(180 * DEGREES, [-1,1,0]).rotate(90 * DEGREES, [0,0,1]).move_to(ORIGIN)
        pyramid_green = Pyramid(3, GREEN_D, 300).rotate(90 * DEGREES, [0,1,0]).rotate(90 * DEGREES, [-1,0,0]).move_to(ORIGIN).shift([1,0,0])
        pyramid_purple = Pyramid(3, PURPLE_C, 200).rotate(90 * DEGREES, [0,1,0]).rotate(90 * DEGREES, [0,0,-1]).move_to(ORIGIN).shift([0,0,1])

        for mobj in [pyramid_blue, pyramid_green, pyramid_purple]:
            cuboid += mobj

        cuboid.shift([-.25, -.25,0])
        self.add(cuboid)

        top_triangle = VGroup(
            pyramid_purple.layers[-1].submobjects[0], pyramid_purple.layers[-1].submobjects[1], pyramid_purple.layers[-1].submobjects[2],
            pyramid_purple.layers[-2].submobjects[0], pyramid_purple.layers[-2].submobjects[1],
            pyramid_purple.layers[-3].submobjects[0],
        )

        top_triangle.stretch(.5, 2).shift([0,0,-.25])

        top_copy_static = top_triangle.copy().shift([0,0,.4])
        self.add(top_copy_static)

        top_copy = top_copy_static.copy()

        top_copy_static.set_opacity(0)
        self.play(top_copy.animate.shift([0,0,.3]))

        self.play(Rotate(top_copy, 180 * DEGREES, [0,0,1]))
        self.play(top_copy.animate.shift([1,0,-.7]))

        self.wait(3)

        self.play(FadeOut(top_copy), top_copy_static.animate.set_opacity(1))