from manim import *

config.frame_size = (800, 230)

class Visualisation2(MovingCameraScene):
    def construct(self):
        #
        #
        #
        self.next_section("Number examples")

        numbers = [
            [1,5,3,8],
            [4,9,3,2],
            [8,7,3,4],
            [1,1,3,1],
            [9,9,3,7],
        ]

        pgroup = []
        for number in numbers:
            group = self.get_number_group(number).scale(4).arrange(RIGHT, 1.5)

            if (len(pgroup) == 0):
                self.play(Write(group))
                pgroup = group
                continue

            self.play(Transform(pgroup, group, replace_mobject_with_target_in_scene = True), run_time = .75)
            pgroup = group

        labels = []
        for i, label in enumerate([Tex("$D_1$"), Tex("$D_2$"), Tex("$D_3$"), Tex("$D_4$")]):
            label.set_color(BLUE)
            label.font_size = 50
            label.next_to(pgroup[i], DOWN, .75)
            labels.append(label)

        self.play(
            LaggedStart(
                *(FadeIn(label, shift=UP) for label in labels),
                lag_ratio=.25
            ),
            run_time = .75
        )
        self.wait(.5)

        #
        #
        #
        self.next_section("Filling product rule")

        squares = VGroup(*[Square().set_stroke(WHITE, 6).move_to(pgroup[i]) for i in range(4)]).arrange(RIGHT, 1.75)
        self.play(
            Transform(pgroup, squares, replace_mobject_with_target_in_scene = True),
            *(label.animate.next_to(squares[i], DOWN, .75) for i, label in enumerate(labels)),
            self.camera.frame.animate.move_to(squares + VGroup(*labels))
        )

        values = []
        for i, val in enumerate([9, 10, 1, 10]):
            values.append(Text(str(val), font_size=60).move_to(squares[i]))

        self.play(
            LaggedStart(
                *(Write(val) for val in values),
                lag_ratio=.25
            )
        )
        self.wait(.5)

        #
        #
        #
        self.next_section("Signs and answer")

        signs = []
        for i in range(3):
            sign = MathTex("\\times", font_size=80, color=GREY)
            sign.next_to(squares[i], RIGHT, .7)
            signs.append(sign)

        answer = MathTex("= \\textbf{900}", font_size=80, color=GREEN).next_to(squares[3], RIGHT, .35).set_opacity(0)

        g_global = VGroup(*squares, *labels, answer)

        self.play(
            LaggedStart(
                *(Write(sign) for sign in signs),
                lag_ratio=.25
            ),
            answer.animate.set_opacity(1),
            self.camera.frame.animate.set_width(g_global.width + .25).move_to(g_global)
        )
        self.wait(3)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)

    def get_number_group(self, num_arr: list):
        return VGroup(
            *(
                MathTex(str(num)) for num in num_arr
            )
        )