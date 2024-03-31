from manim import *
import numpy as np

class Pyramid(VMobject):
    def __init__(self, layers_num: int, color: ManimColor, z_index: int, **kwargs):
        super().__init__(**kwargs)

        self.layers = []
        self.coords = np.zeros((layers_num + 1 , layers_num + 1 , layers_num + 1), VMobject)
        cube_size = .9

        for z in range(layers_num + 1):
            layer = VGroup()
            self.layers.append(layer)

            for x in range(z):
                for (y) in range(z):
                    cube = Cube(side_length=cube_size, fill_color=color, fill_opacity=1)
                    cube.move_to([x,y,z])
                    self.coords[x,y,z] = cube
                    layer += cube
                    layer.set_z_index(z_index + layers_num - z)
                    self.add(layer)