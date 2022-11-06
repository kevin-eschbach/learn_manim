from manim import *
import numpy as np


# manim getting started
class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


# manim example
class ToyExample(Scene):
    def construct(self):
        orange_square = Square(color=ORANGE, fill_opacity=0.5)
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.add(orange_square)
        self.play(ReplacementTransform(orange_square, blue_circle, run_time=3))
        small_dot = Dot()
        small_dot.add_updater(lambda mob: mob.next_to(blue_circle, DOWN))
        self.play(Create(small_dot))
        self.play(blue_circle.animate.shift(RIGHT))
        self.wait()
        self.play(FadeOut(blue_circle, small_dot))


# youtube tutorial I
class Test(Scene):
    def construct(self):
        # create square and let the animation run for 3 sec
        square = Square(side_length=4, stroke_color= GREEN, fill_color=BLUE, fill_opacity=.6)
        self.play(Create(square), run_time=3)
        # wait 1 sek before finishing scene
        self.wait(duration=1)


# YT tutorial II
class TextScene(Scene):
    def construct(self):
        name = Tex("Hello World").to_edge(UL, buff=.5)
        sq = Square(side_length=.4, fill_color=RED, fill_opacity=.6).shift(LEFT * 3)
        tri = Triangle().scale(.4).to_corner(DR)
        self.play(Write(name))
        self.play(DrawBorderThenFill(sq), run_time=2)
        self.play(Create(tri))

        self.play(name.animate.to_edge(DR), tri.animate.to_edge(UL), run_time=3)
        self.play(sq.animate.rotate(PI * .5))
        self.wait(3)


# YT tutorial III
class ReadTheLib(Scene):
    def construct(self):
        ax = Axes()
        rect = Rectangle().scale(.1)
        circ = Circle().to_edge(DR).scale(.3)
        arrow = always_redraw(lambda: Line(start=rect.get_bottom(), end=circ.get_top()).add_tip())
        self.play(Create(ax))
        self.play(Create(VGroup(rect, circ, arrow)))
        self.play(rect.animate.to_edge(UP), circ.animate.scale(3.))
        self.wait(2)

class Updaters(Scene):
    def construct(self):
        num = MathTex("\mathcal{O}(n^2)")
        box = always_redraw(lambda : SurroundingRectangle(num, color=BLUE, fill_opacity=.4, fill_color=RED, buff=2))
        name = always_redraw(lambda : Tex("Get shitfaced").next_to(box, DR))
        self.play(Create(VGroup(box, num, name)))
        self.play(num.animate.shift(LEFT * 2))
        self.wait(2)


class Tracker(Scene):
    def construct(self):
        tracker = ValueTracker(0)
        number_line = NumberLine()
        point = Vector(DOWN).next_to(number_line.n2p(tracker.get_value()), UP)
        label = MathTex("x").add_updater(lambda m: m.next_to(point, UP)).next_to(point, UP)
        num = DecimalNumber(tracker.get_value()).move_to(DR).add_updater(lambda m: m.set_value(tracker.get_value()))
        point.add_updater(
            lambda m: m.next_to(
                number_line.n2p(tracker.get_value()), UP))

        self.add(number_line, point, label, num)
        tracker += 1.5
        self.wait(1)
        tracker -= 3
        self.wait(.5)
        self.play(tracker.animate.set_value(5))
        self.wait(1)
        self.play(tracker.animate.increment_value(-2))
        self.wait(1)
