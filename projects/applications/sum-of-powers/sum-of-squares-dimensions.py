from manim import *
from pyramid import Pyramid

class SumOfSquaresDimensions(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(theta=-45 * DEGREES, phi=60 * DEGREES, zoom=.75)

        #

        cuboid = VGroup()

        pyramid_blue = Pyramid(3, BLUE_D, 100).rotate(180 * DEGREES, [-1,1,0]).rotate(90 * DEGREES, [0,0,1]).move_to(ORIGIN)
        pyramid_green = Pyramid(3, GREEN_D, 300).rotate(90 * DEGREES, [0,1,0]).rotate(90 * DEGREES, [-1,0,0]).move_to(ORIGIN).shift([1,0,0])
        pyramid_purple = Pyramid(3, PURPLE_C, 200).rotate(90 * DEGREES, [0,1,0]).rotate(90 * DEGREES, [0,0,-1]).move_to(ORIGIN).shift([0,0,1])

        pyramid_blue2 = Pyramid(3, BLUE_D, 90).rotate(-90 * DEGREES, [1,0,0]).rotate(180 * DEGREES, [0,1,0]).move_to(ORIGIN).shift([1,0,3])
        pyramid_green2 = Pyramid(3, GREEN_D, 500).rotate(-90 * DEGREES, [0,1,0]).move_to(ORIGIN).shift([0,0,4])
        pyramid_purple2 = Pyramid(3, PURPLE_C, 600).rotate(90 * DEGREES, [0,0,1]).move_to(ORIGIN).shift([1,0,4])

        length_arrow_n = Arrow3D(start=[0,-3,0], end=[3,-3,0], color=BLUE_D, resolution=8)
        length_arrow_1 = Arrow3D(start=[3,-3,0], end=[4,-3,0], color=GREEN_D, resolution=8)

        length_label_n = Tex("$n$", color=BLUE_D).move_to(length_arrow_n.get_center()).shift([0,-.5,0])
        length_label_1 = Tex("$1$", color=GREEN_D).move_to(length_arrow_1.get_center()).shift([0,-.5,0])

        width_arrow = Arrow3D(start=[4,-3,0], end=[4,0,0], color=GREEN_D, resolution=8)

        width_label = Tex("$n$", color=GREEN_D).move_to(width_arrow.get_center()).shift([.5,0,0]).rotate(90 * DEGREES, [0,0,1])

        height_arrow_green = Arrow3D(start=[4,0,0], end=[4,0,2.8], color=GREEN_D, resolution=8)
        height_arrow_blue = Arrow3D(start=[4,0,2.8], end=[4,0,5.6], color=BLUE_D, resolution=8)
        height_arrow_purple = Arrow3D(start=[4,0,5.6], end=[4,0,6.4], color=PURPLE_C, resolution=8)

        height_label_green = Tex("$n$", color=GREEN_D).move_to(height_arrow_green.get_center()).shift([.5,0,0]).rotate(90 * DEGREES, [1,0,0])
        height_label_blue = Tex("$n$", color=BLUE_D).move_to(height_arrow_blue.get_center()).shift([.5,0,0]).rotate(90 * DEGREES, [1,0,0])
        height_label_purple = Tex("$1$", color=PURPLE_C).move_to(height_arrow_purple.get_center()).shift([.5,0,0]).rotate(90 * DEGREES, [1,0,0])

        for mobj in [pyramid_blue,
                     pyramid_green,
                     pyramid_purple,
                     pyramid_blue2,
                     pyramid_green2,
                     pyramid_purple2,

                     length_arrow_n,
                     length_arrow_1,
                     width_arrow,
                     height_arrow_green,
                     height_arrow_blue,
                     height_arrow_purple,
                     
                     length_label_n,
                     length_label_1,
                     width_label,
                     height_label_green,
                     height_label_blue,
                     height_label_purple]:
            cuboid += mobj

        cuboid.shift([0,0,-1.25]).shift([-.35,-.35,0])

        self.add(cuboid)