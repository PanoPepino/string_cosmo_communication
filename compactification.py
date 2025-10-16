from manim import *


class Compactification(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-PI, PI, 1],
            faded_line_ratio=5
        )
        frame = SurroundingRectangle(plane, buff=0, color=WHITE, stroke_width=3)
        plane.add(frame)

        plane2 = plane.copy()

        plane.prepare_for_nonlinear_transform()

        def map1(point):
            z = R3_to_complex(point)
            X, Y = float(np.real(z)), float(np.imag(z))
            w = X + np.cos(Y)*0.3 + 1j * np.sin(Y)
            return complex_to_R3(w)

        plane2.prepare_for_nonlinear_transform()
        plane2.apply_complex_function(
            lambda z: np.exp(z)
        )

        self.add(plane, frame)
        self.play(
            plane.animate.apply_function(
                lambda p: map1(p)
            ),
            run_time=3
        )
        self.wait()
        self.play(Transform(plane, plane2), run_time=3)
        self.wait()
