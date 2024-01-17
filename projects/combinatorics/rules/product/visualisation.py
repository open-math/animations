from manim import *

config.frame_size = (800, 230)

class Visualisation(MovingCameraScene):
    def construct(self):
        g_pizzas =          VGroup()
        g_pizza_labels =    VGroup()
        g_numbers =         VGroup()
        g_signs =           VGroup()
        g_global =          VGroup(g_pizzas, g_pizza_labels, g_numbers, g_signs)

        for i in range(4):
            pizza = Circle(1, color=WHITE).set_stroke(WHITE, 6).move_to(RIGHT * (3.5 * i))
            g_pizzas += pizza

            pizza_label = Tex(f"$P_{i+1}$", font_size=60).move_to(pizza.get_center())
            g_pizza_labels += pizza_label

            number = Text(str(5-i), font_size=60).move_to(pizza.get_center())
            g_numbers += number

        for i in range(3):
            sign = Tex("$\\times$", font_size=80, color=GREY).move_to(RIGHT * (i * 3.5 + 1.75))
            g_signs += sign

        g_global.move_to(ORIGIN)
        g_global.to_edge(UP, 2.5)

        answer = Tex("$= \\textbf{120}$", font_size=80, color=GREEN).next_to(g_pizzas, RIGHT * 1.7).set_opacity(0)
        self.add(answer)

        self.play(
            Create(g_pizzas),
            LaggedStart(*(Write(pizza_label) for pizza_label in g_pizza_labels), lag_ratio=.25)
        )
        self.wait(.5)

        self.play(g_pizza_labels.animate.shift(DOWN * 2).set_color(BLUE), run_time=.5)
        self.play(LaggedStart(*(Write(number) for number in g_numbers), lag_ratio=.25))
        self.wait(.5)

        self.play(
            LaggedStart(*(Write(sign) for sign in g_signs), lag_ratio=.15),
            answer.animate.set_opacity(1),
            self.camera.frame.animate.set_width((g_global + answer).width * 1.15).move_to((g_global + answer))
        )
        self.wait(3)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
