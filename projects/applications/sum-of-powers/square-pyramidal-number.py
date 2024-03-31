from manim import *

config.frame_size = (550 * 3, 480 * 3)

class SquarePyramidalNumber(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(theta=-45 * DEGREES, phi=60 * DEGREES, zoom=1.5)

        #

        pyramid = VGroup()

        layers = 5
        cube_size = .9
        cube_size_h = cube_size / 2

        for z in range(layers):
            for x in range(z):
                for y in range(z):
                    # Adding cube
                    cube = Cube(side_length=cube_size, fill_opacity=1, fill_color=BLUE_D)
                    cube.move_to([x,-y,-z])
                    pyramid += cube

                    # Ensure the last cube in layer
                    if (x == y and y == z-1):
                        arrow_start_pos = cube.get_center() + [cube_size_h,-cube_size_h,cube_size_h + .05]

                        arrow_to_xz = Arrow3D(resolution=8,start=arrow_start_pos, end=[-cube_size_h, arrow_start_pos[1], arrow_start_pos[2]])
                        arrow_to_yz = Arrow3D(resolution=8,start=arrow_start_pos, end=[arrow_start_pos[0], cube_size_h, arrow_start_pos[2]])

                        arrow_to_xz.set_shade_in_3d(True)
                        arrow_to_yz.set_shade_in_3d(True)

                        label_num = "n" if z == layers-1 else z

                        if (z-1 > 0):
                            xza_label = Tex(f"$ {label_num} $").move_to(arrow_to_xz.get_center() + [0,0,.25]).rotate(90 * DEGREES, [1,0,0]).set_shade_in_3d(True)
                            yza_label = Tex(f"$ {label_num} $").move_to(arrow_to_yz.get_center() + [0,0,.25]).rotate(90 * DEGREES, [1,0,0]).rotate(90 * DEGREES, [0,0,1]).set_shade_in_3d(True)

                            pyramid += xza_label
                            pyramid += yza_label

                        pyramid += arrow_to_xz
                        pyramid += arrow_to_yz

                        label = Tex(f"$ {label_num}^2 $")
                        label.set_shade_in_3d(True)
                        label.move_to(cube)
                        label.shift([0,0,cube_size_h + .2])
                        label.rotate(45 * DEGREES, [0,0,1]).rotate(90 * DEGREES, [1,1,0])
                        pyramid += label

        pyramid.shift([-2.5,2.5,2.15]).scale(1.2)

        self.play(Rotate(pyramid, 360 * DEGREES, run_time=10, rate_func=linear))