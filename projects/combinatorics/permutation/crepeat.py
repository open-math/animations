from manim import *

config.disable_caching = True
config.frame_size = (800, 200)

class PCircle(VMobject):
    def __init__(self, num_elements: int, elem_shift: int = 0, **kwargs):
        super().__init__(**kwargs)

        self.circle = Circle(2, WHITE, stroke_width=15)
        self.elements = VGroup()
        self.labels = VGroup()

        for i in range(num_elements):
            angle = -1 * i * (360 / num_elements) * DEGREES
            point = self.circle.point_at_angle(angle)

            element = Circle(.75, GREEN if i - elem_shift == 0 else WHITE, fill_opacity=1)
            element.move_to(point)
            self.elements.add(element)

            label = Tex(f'$\\mathbf{(i - elem_shift) % num_elements + 1}$', color=BLACK, font_size=70, z_index=100)
            label.move_to(point)
            label.add_updater(lambda mob, elem=element: mob.move_to(elem))
            self.labels.add(label)

        self.add(
            self.circle,
            self.elements,
            self.labels,
        )

class MoveRotate(Animation):
    def __init__(self, mob: Mobject, distance: float, angle: float, about_point, **kwargs):
        self.distance = distance
        self.angle = angle
        self.about_point = about_point
        self.original = mob.copy()
        super().__init__(mob, rate_func=linear, **kwargs)
    
    def interpolate_mobject(self, alpha: float) -> None:
        new_mob = self.original.copy()
        new_mob.rotate(interpolate(0, self.angle*DEGREES, alpha), about_point=self.about_point)
        new_mob.shift([interpolate(0, self.distance, alpha), 0, 0])

        self.mobject.become(new_mob)

###
###
###

class CircleRepeat(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(1.9)

        num_elements = 4
        pcircles = VGroup(*[PCircle(num_elements, i) for i in range(num_elements)])
        pcircles.arrange(RIGHT, 1.5)

        move_distance = pcircles[1].get_center()[0] - pcircles[0].get_center()[0]

        _pc = PCircle(num_elements)
        _pc.move_to(pcircles[0])

        self.play(Write(_pc))

        for i in range(num_elements - 1):
            self.wait(.5)
            self.add(pcircles[i])
            self.play(MoveRotate(VGroup(_pc.circle, _pc.elements), move_distance, -1 * 360 / num_elements, _pc.circle.get_center()))

        self.wait(3)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)