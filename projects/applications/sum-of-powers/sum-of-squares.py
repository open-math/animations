from manim import *
from pyramid import Pyramid

class SumOfSquares(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(theta=-45 * DEGREES, phi=60 * DEGREES, zoom=.85)

        #

        cuboid = VGroup()

        pyramid_blue = Pyramid(3, BLUE_D, 100).rotate(180 * DEGREES, [-1,1,0]).rotate(90 * DEGREES, [0,0,1]).move_to(ORIGIN)
        pyramid_green = Pyramid(3, GREEN_D, 300).rotate(90 * DEGREES, [0,1,0]).rotate(90 * DEGREES, [-1,0,0]).move_to(ORIGIN).shift([1,0,0])
        pyramid_purple = Pyramid(3, PURPLE_C, 200).rotate(90 * DEGREES, [0,1,0]).rotate(90 * DEGREES, [0,0,-1]).move_to(ORIGIN).shift([0,0,1])

        pyramid_blue2 = Pyramid(3, BLUE_D, 90).rotate(-90 * DEGREES, [1,0,0]).rotate(180 * DEGREES, [0,1,0]).move_to(ORIGIN).shift([1,0,3])
        pyramid_green2 = Pyramid(3, GREEN_D, 500).rotate(-90 * DEGREES, [0,1,0]).move_to(ORIGIN).shift([0,0,4])
        pyramid_purple2 = Pyramid(3, PURPLE_C, 600).rotate(90 * DEGREES, [0,0,1]).move_to(ORIGIN).shift([1,0,4])

        for mobj in [pyramid_blue, pyramid_green, pyramid_purple, pyramid_blue2, pyramid_green2, pyramid_purple2]:
            cuboid += mobj

        cuboid.shift([0,0,-1.75]).shift([-.35,-.35,0])

        for pyramid in [pyramid_blue, pyramid_green, pyramid_purple, pyramid_blue2, pyramid_green2, pyramid_purple2]:
            for layer in pyramid.layers:
                layer.set_opacity(0)
                self.add(layer)
                self.play(layer.animate.set_opacity(1), run_time=1)

        # Rotating

        self.wait(1)
        self.play(Rotate(cuboid, 360 * DEGREES, [0,0,1]), rate_func=linear, run_time=5)
        self.wait(1)

        # Clearing scene

        self.play(*[FadeOut(mob) for mob in self.mobjects])