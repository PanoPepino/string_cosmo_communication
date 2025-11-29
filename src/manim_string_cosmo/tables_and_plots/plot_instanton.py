from ..my_imports import *
from .plot_general import *

__all__ = ["Plot_Instanton"]


class Plot_Instanton(Plot_General, Group):
    """
    Create a visual representation of an instanton potential with false and true minima.

    This class inherits from :class:`Plot_General` and produces a plot showing a double-well
    potential landscape characteristic of instanton configurations in quantum field theory.
    The plot includes labeled minima (V+ and V-) and an interactive field position indicator
    that can be animated to demonstrate tunneling processes.

    :param kwargs: Keyword arguments passed to :class:`Plot_General` for styling configuration.

    .. note::

       The axis and labels are stored as the 0-th element of the group when accessed.

       To scale the graph with respect to its center:
       ``plot.scale(3, about_point=plot.ax_ins.c2p(0, 0, 0))``

    .. seealso::

       - :class:`Plot_General` - Base class providing styling parameters
       - :class:`Plot_Quantum` - Related quantum mechanical plot

    **Example usage:**

    .. code-block:: python

        from manim import *
        from manim_string_cosmo import *

        class InstantonExample(Scene):
            def construct(self):
                # Create instanton plot in bottom-left corner
                p_ins = Plot_Instanton().to_corner(DL)

                # Add the plot axes and potential
                self.add(p_ins[0])

                # Animate field position appearing
                self.play(p_ins.fade_in_field_position())

                # Demonstrate tunneling/decay process
                self.play(p_ins.decay())
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ax_ins = (
            NumberPlane(
                x_range=[-2.1, 2.1, 1],
                y_range=[-1, 1.5, 1],
                tips=False,
                background_line_style={"stroke_opacity": 0},
            )
            .set_color(self.text_color)
            .set(stroke_opacity=self.axis_opacity)
        )
        lab_ax_ins = self.ax_ins.get_axis_labels(
            x_label=MathTex("\phi", font_size=20, color=self.func_main_color),
            y_label=MathTex("V(\phi)", font_size=25, color=self.func_main_color),
        )
        lab_ax_ins[1].shift(0.2 * DOWN)
        lab_ax_ins[0].shift(0.2 * LEFT)
        self.ax_ins.y_axis.set_opacity(self.axis_opacity).set(
            stroke_width=self.axis_stroke
        )
        self.ax_ins.x_axis.set_opacity(self.axis_opacity).set(
            stroke_width=self.axis_stroke
        )

        # Potential and labels
        pot_ins = self.ax_ins.plot(
            lambda x: (-2 * x**2 + (x - 0.1) ** 4 + 0.64),
            color=self.func_main_color,
            stroke_width=self.axis_stroke,
            use_smoothing=True,
            x_range=[-1.3, 1.6],
        )
        t_label = self.ax_ins.get_T_label(
            x_val=-0.845649,
            graph=pot_ins,
            label=MathTex("V_{+}", font_size=20, color=self.func_main_color),
            triangle_size=0,
        )
        t_label.shift(0.6 * UP + 0.05 * RIGHT)
        t_label_2 = self.ax_ins.get_T_label(
            x_val=1.15,
            graph=pot_ins,
            label=MathTex("V_{-}", font_size=20, color=self.func_main_color),
            triangle_size=0,
        )
        t_label_2[0].shift(0.20 * DOWN)
        t_label_2[-1].shift(30 * UP)

        minima_labels = VGroup(t_label, t_label_2)

        self.field_position = Dot(
            color=self.decorator_color, stroke_width=self.stroke_w, fill_opacity=1
        )
        self.tracker_ins = ValueTracker(-0.845649)
        self.field_position.add_updater(
            lambda y: y.move_to(self.ax_ins.c2p(self.tracker_ins.get_value(), 0))
        )

        if self.decorator_presence == "box":
            box = SurroundingRectangle(
                self.ax_ins,
                corner_radius=self.corner_rad,
                color=self.decorator_color,
                fill_opacity=self.fill_opa,
                buff=self.tightness,
                stroke_width=self.decorator_stroke_w,
            )
            self.initial_show = VGroup(
                self.ax_ins, lab_ax_ins, pot_ins, minima_labels, box
            )
            self.add(self.initial_show, self.field_position)
        else:
            self.initial_show = VGroup(self.ax_ins, lab_ax_ins, pot_ins, minima_labels)
            self.add(self.initial_show, self.field_position)

    def fade_in_field_position(self, rt: float = 0.5, rf: float = linear) -> Animation:
        """
        Animate the field position indicator fading into view.

        This method creates a fade-in animation for the dot representing the current
        field position in the potential landscape.

        :param rt: Animation runtime in seconds.
        :type rt: float, default=0.5

        :param rf: Rate function controlling animation timing (e.g., ``linear``, ``smooth``).
        :type rf: function, default=linear

        :returns: Animation showing the field position indicator fading in.
        :rtype: Animation

        **Example:**

        .. code-block:: python

            plot = Plot_Instanton()
            self.play(plot.fade_in_field_position(rt=1.0, rf=smooth))
        """
        return FadeIn(self.field_position, run_time=rt, rate_func=rf)

    def decay(self, rt: float = 0.5, rf: float = linear) -> Animation:
        """
        Animate the tunneling/decay process from false vacuum to true vacuum.

        This method creates an animation showing the field position transitioning
        from the false vacuum (V+) to the true vacuum (V-), representing quantum
        tunneling through the potential barrier.

        :param rt: Animation runtime in seconds.
        :type rt: float, default=0.5

        :param rf: Rate function controlling animation timing.
        :type rf: function, default=linear

        :returns: Animation describing the tunneling process in the potential.
        :rtype: Animation

        **Example:**

        .. code-block:: python

            plot = Plot_Instanton()
            # Quick decay animation
            self.play(plot.decay(rt=0.3, rf=rush_into))

            # Smooth, slower decay
            self.play(plot.decay(rt=2.0, rf=smooth))
        """
        return self.tracker_ins.animate(run_time=rt, rate_func=rf).set_value(0.7)
