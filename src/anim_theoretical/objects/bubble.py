from os import path

from ..my_imports import *
from .brane_general import *
from .vacuum_general import *

__all__ = ["Bubble"]


class Bubble(Brane_General, Vacuum_General, Group):
    """
    Represent Dark Bubble scenarios in 2D with various physical configurations.

    This class visualizes bubble nucleation and expansion in string cosmology,
    supporting multiple physical scenarios including empty vacuum, radiation content,
    electromagnetic fields, strings, gravitational waves, and energy conservation discussions.
    The bubble (brane) is always the 3rd element (index ``[2]``) of the group.

    :param bubble_type: Type of bubble configuration. Options:
        - ``"empty"``: Standard inside/outside configuration with AdS scales k− and k₊.
        - ``"instanton"``: AdS scales replaced by scalar potentials V(φ−) and V(φ₊).
        - ``"radiation"``: Includes matter (mass) inside the bubble.
        - ``"strings"``: Shows radially stretching strings from brane to bulk boundary.
        - ``"GW"``: Displays gravitational wave emission from the brane.
        - ``"em"``: Visualizes electromagnetic B-field on the brane with glow effect.
        - ``"energy_discussion"``: Shows energy bar for discussing energy conservation.
        Default is ``"empty"``.
    :type bubble_type: str

    :param box_height: Height of the vacuum background box. Default is ``6``.
    :type box_height: float

    :param box_width: Width of the vacuum background box. Default is ``8``.
    :type box_width: float

    :param string_color: Color of the strings (for ``bubble_type="strings"``). Default is ``BLUE``.
    :type string_color: ParsableManimColor

    :param string_stroke_w: Stroke width of the strings. Default is ``1.5``.
    :type string_stroke_w: float

    :param field_gradient: Number of gradient layers for the electromagnetic field glow effect.
        Higher values create smoother gradients. Default is ``50``.
    :type field_gradient: float

    :param field_top_color: Color of the electromagnetic field on the brane surface.
        Default is ``BLUE``.
    :type field_top_color: ParsableManimColor

    :param field_bulk_color: Color for bulk electromagnetic field (to be implemented).
        Default is ``PINK``.
    :type field_bulk_color: ParsableManimColor

    :param kwargs: Additional keyword arguments passed to :class:`Brane_General`,
        :class:`Vacuum_General`, and :class:`Group`.

    .. note::

       The bubble (brane) is always the 3rd element (``[2]``) in the internal ``bubble`` group.
       See :class:`Brane_General` and :class:`Vacuum_General` for additional inherited parameters.

    .. attention::

       The ``"em"`` mode currently lacks representation of the B-field in the bulk;
       only the brane surface field is visualized.

    **Example usage:**

    .. code-block:: python

        from manim import *
        from anim_theoretical import Bubble

        class Example_Bubble(Scene):
            def construct(self):
                bubble_types = ["empty", "radiation", "em", "strings", "GW"]
                bubble_group = Group(*[Bubble(bubble_type=style).scale(0.4)
                                       for style in bubble_types])
                bubble_group.arrange_in_grid(2, 3)

                self.play(AnimationGroup(*[x.fade_in_bulk() for x in bubble_group]))
                self.play(AnimationGroup(*[x.create_bubble() for x in bubble_group]))
                self.play(AnimationGroup(*[x.expand_bubble() for x in bubble_group]))

        class Example_Energy_Discussion(Scene):
            def construct(self):
                bub = Bubble(bubble_type="energy_discussion").scale(0.8)
                self.play(bub.fade_in_bulk())
                self.play(bub.fail_creation())
                self.play(bub.create_bubble())
                self.play(bub.expand_bubble())
                self.play(FadeOut(bub))
    """

    def __init__(
        self,
        bubble_type: str = "empty",
        box_height: float = 6,
        box_width: float = 8,
        string_color: ParsableManimColor = BLUE,
        string_stroke_w: float = 1.5,
        field_gradient: float = 50,
        field_top_color: ParsableManimColor = BLUE,
        field_bulk_color: ParsableManimColor = PINK,
        **kwargs,
    ):
        super().__init__(**kwargs)

        # Store bubble type for use in animation methods
        self.bubble_type = bubble_type

        # Geometry Bubbles
        self.background = RoundedRectangle(
            corner_radius=self.corner_rad,
            height=box_height,
            width=box_width,
            stroke_width=self.vacuum_stroke_w,
            color=self.vacuum_color,
            fill_opacity=self.vacuum_fill_opa,
        )
        self.brane = Circle(
            radius=self.brane_radius,
            color=self.brane_color,
            fill_opacity=1.5 * self.brane_fill_opa,
            stroke_width=self.brane_stroke_w,
        )

        # Text
        self.in_text = (
            MathTex("k_{-}", font_size=35, color=self.vacuum_text_color)
            .move_to(self.background.get_center())
            .set_z_index(4)
        )
        self.out_text = (
            MathTex("k_{+}", font_size=35, color=self.vacuum_text_color)
            .move_to(self.background.get_corner(UR) - [0.45, 0.45, 0])
            .set_z_index(4)
        )

        self.in_insta_text = (
            MathTex("V(\\phi_{-})", font_size=35, color=self.vacuum_text_color)
            .move_to(self.background.get_center())
            .set_z_index(4)
        )
        self.out_insta_text = (
            MathTex("V(\\phi_{+})", font_size=35, color=self.vacuum_text_color)
            .move_to(self.background.get_corner(UR) - [0.55, 0.55, 0])
            .set_z_index(4)
        )
        self.radius_line = Line(
            start=self.brane.get_center(),
            end=2.5 * self.brane.point_at_angle(PI / 4),
            color=self.vacuum_text_color,
            stroke_width=self.brane_stroke_w,
        )
        self.radius_text = (
            MathTex("r=a(\\tau)", font_size=30, color=self.vacuum_text_color)
            .rotate(PI / 4)
            .next_to(self.radius_line.get_center(), LEFT, buff=0.05)
        )
        self.radius_info = VGroup(self.radius_line, self.radius_text)

        # matter
        get_mass_path = path.join(path.dirname(__file__), "../figures/weight.svg")
        self.mass = SVGMobject(get_mass_path).scale(0.5)

        # strings
        self.strings = VGroup()
        box_positions = [RIGHT, UR, UP, UL, LEFT, DL, DOWN, DR]
        dots = VGroup(
            *[
                Dot(
                    radius=0,
                    fill_opacity=0,
                    point=self.brane.point_at_angle(i * 360 / 8 * DEGREES),
                )
                for i in range(len(box_positions))
            ]
        )
        self.brane_w_anchor = VGroup(dots, self.brane)

        # Create strings with always_redraw for dynamic positioning
        for angle, position in zip(dots, box_positions):
            if np.linalg.norm(position) > 1:
                string = always_redraw(
                    lambda angle=angle, position=position: Line(
                        start=angle,
                        end=self.background.get_corner(position)
                        - self.cr / 6 * position,
                        stroke_width=string_stroke_w,
                        stroke_color=string_color,
                    )
                )
                self.strings.add(string)
            else:
                string = always_redraw(
                    lambda angle=angle, position=position: Line(
                        start=angle,
                        end=self.background.get_corner(position),
                        stroke_width=string_stroke_w,
                        stroke_color=string_color,
                    )
                )
                self.strings.add(string)

        # Gravitational Waves
        def func_waves(t):
            return (
                (self.brane_radius + 0.01 * np.sin(25 * t)) * np.cos(t),
                (self.brane_radius + 0.01 * np.sin(25 * t)) * np.sin(t),
                0,
            )

        self.brane_waves = ParametricFunction(
            func_waves,
            t_range=(0, 2 * TAU),
            stroke_width=self.brane_stroke_w,
            fill_opacity=self.brane_fill_opa,
        ).set_color(self.brane_color)
        self.waves = ParametricFunction(
            func_waves,
            t_range=(0, 2 * TAU),
            stroke_width=self.brane_stroke_w / 3,
            fill_opacity=0,
        ).set_color(self.brane_color)

        # Extra Fields - Electromagnetism
        def field(
            grad,
            mobject,
            rad=self.brane_radius + 0.6,
            inner_rad=1.05 * self.brane_radius,
            col=field_top_color,
        ):
            glow_group = VGroup()
            for idx in range(grad):
                new_circle = Annulus(
                    inner_radius=inner_rad,
                    outer_radius=inner_rad + idx / grad * (rad - inner_rad),
                    stroke_opacity=0,
                    fill_color=col,
                    fill_opacity=0.75 / grad,
                ).move_to(mobject)
                glow_group.add(new_circle)
            return glow_group

        self.field_glow = field(field_gradient, self.brane)
        self.field_top = Circle(
            radius=1.05 * self.brane_radius,
            color=field_top_color,
            fill_opacity=0,
            stroke_width=4,
        )

        # Energy Discussion
        self.vacuum_tracker = ValueTracker(0.8)
        self.bar_outside = RoundedRectangle(
            corner_radius=self.corner_rad,
            height=0.6,
            width=box_width,
            stroke_width=self.vacuum_stroke_w + 0.2,
            color=self.brane_color,
            fill_opacity=0,
        )
        self.bar_outside.next_to(self.background, DOWN, buff=0.2)
        self.energy_gain = always_redraw(
            lambda: RoundedRectangle(
                corner_radius=self.corner_rad,
                height=0.5,
                width=self.vacuum_tracker.get_value(),
                stroke_width=0.1,
                fill_opacity=self.brane_fill_opa,
            )
            .next_to(self.bar_outside.get_left(), aligned_edge=LEFT, buff=0)
            .set_color(self.bar_outside.get_color())
        )
        self.energy_cost_bubble = DashedVMobject(
            Circle(
                radius=self.brane_radius,
                color=self.brane_color,
                fill_opacity=0,
                stroke_width=self.vacuum_stroke_w + 0.9,
            )
        )

        # Assemble bubble based on type
        if bubble_type == "empty":
            self.bubble = VGroup(
                self.background,
                self.out_text,
                self.brane,
                self.in_text,
                self.radius_info,
            )
            self.add(self.bubble)

        if bubble_type == "instanton":
            self.bubble = VGroup(
                self.background, self.out_insta_text, self.brane, self.in_insta_text
            )
            self.add(self.bubble)

        if bubble_type == "radiation":
            self.in_text.next_to(self.mass, DOWN, buff=0.2)
            self.bubble = VGroup(
                self.background, self.out_text, self.brane, self.in_text, self.mass
            )
            self.add(self.bubble)

        if bubble_type == "GW":
            self.bubble = VGroup(
                self.background, self.out_text, self.brane_waves, self.in_text
            )
            self.add(self.bubble)

        if bubble_type == "strings":
            self.out_text.shift(0.3 * DOWN)
            self.bubble = VGroup(
                self.background,
                self.out_text,
                self.brane_w_anchor,
                self.strings,
                self.in_text,
            )
            self.add(self.bubble)

        if bubble_type == "em":
            self.bubble = VGroup(
                self.background,
                self.out_text,
                self.brane,
                self.in_text,
                self.field_top,
                self.field_glow,
            )
            self.add(self.bubble)

        if bubble_type == "energy_discussion":
            self.fake_brane = self.brane.copy()
            self.bubble = VGroup(
                self.background,
                self.out_text,
                self.fake_brane,
                self.brane,
                self.energy_cost_bubble,
            )
            self.add(self.bubble, self.bar_outside, self.in_text, self.energy_gain)

    def fade_in_bulk(
        self, rt: float = 1, rf: float = linear
    ) -> Animation:
        """
        Fade in the bulk vacuum and outside cosmological constant label.

        For ``bubble_type="energy_discussion"``, this also creates the energy bar
        visualization at the bottom of the scene.

        :param rt: Run time of the animation. Default is ``1``.
        :type rt: float

        :param rf: Rate function controlling animation timing. Default is ``linear``.
        :type rf: function

        :return: Animation showing bulk box and outside text appearance.
        :rtype: Animation or Succession
        """
        if self.bubble_type == "energy_discussion":
            return Succession(
                FadeIn(self.bubble[:2], run_time=rt, rate_func=rf),
                FadeIn(self.bubble[-1], run_time=rt, rate_func=rf),
                Create(
                    VGroup(self.bar_outside, self.energy_gain),
                    run_time=rt,
                    rate_func=rf,
                ),
            )
        else:
            return FadeIn(self.bubble[:2], run_time=rt, rate_func=rf)

    def fail_creation(
        self, rt: float = 3, rf: float = there_and_back_with_pause
    ) -> AnimationGroup:
        """
        Demonstrate failed bubble nucleation due to insufficient energy.

        The brane attempts to nucleate but fails because the energy bar shows
        insufficient energy available for bubble creation.

        :param rt: Run time of the animation. Default is ``3``.
        :type rt: float

        :param rf: Rate function controlling animation timing. Default is
            ``there_and_back_with_pause``.
        :type rf: function

        :return: Animation showing energy accumulation and failed nucleation attempt.
        :rtype: AnimationGroup

        .. note::

           This method only works with ``bubble_type="energy_discussion"``.
        """
        return AnimationGroup(
            self.vacuum_tracker.animate(run_time=rt, rate_func=rf).set_value(2),
            GrowFromCenter(self.bubble[2].scale(0.8), run_time=rt, rate_func=rf),
        )

    def create_bubble(
        self, rt: float = 0.2, rf: float = linear
    ) -> Succession:
        """
        Animate bubble nucleation and display inside vacuum label.

        The animation behavior varies by bubble type:
        - ``"energy_discussion"``: Shows energy bar reaching threshold and successful nucleation.
        - ``"em"``: Creates brane with electromagnetic field visualization.
        - ``"strings"``: Creates brane and attached strings.
        - ``"radiation"``: Creates brane and shows interior matter.
        - Other types: Standard brane creation with inside text.

        :param rt: Run time of the animation. Default is ``0.2``.
        :type rt: float

        :param rf: Rate function controlling animation timing. Default is ``linear``.
        :type rf: function

        :return: Animation sequence for bubble creation with type-specific elements.
        :rtype: Succession
        """
        if self.bubble_type == "energy_discussion":
            return Succession(
                self.vacuum_tracker.animate(run_time=5 * rt, rate_func=rf).set_value(
                    2.5
                ),
                GrowFromCenter(self.bubble[3], run_time=5 * rt, rate_func=rf),
                self.energy_cost_bubble.animate.set_opacity(0),
            )

        if self.bubble_type == "em":
            return Succession(
                GrowFromCenter(self.bubble[2], run_time=rt, rate_func=rf),
                FadeIn(self.bubble[3:-2], run_time=rt, rate_function=rt),
                Create(self.field_top, run_time=rt, rate_function=rf),
                Wait(),
                Create(self.field_glow, run_time=2 * rt, rate_func=rf),
            )

        if self.bubble_type == "strings":
            return Succession(
                GrowFromCenter(self.bubble[2], run_time=rt, rate_func=rf),
                Create(self.strings, run_time=rt, rate_func=rf),
                FadeIn(self.bubble[-1], run_time=rt, rate_function=rt),
            )

        if self.bubble_type == "radiation":
            return Succession(
                GrowFromCenter(self.bubble[2], run_time=rt, rate_func=rf),
                FadeIn(self.bubble[3:], run_time=rt, rate_function=rt),
            )

        else:
            return Succession(
                GrowFromCenter(self.bubble[2], run_time=rt, rate_func=rf),
                FadeIn(self.bubble[3:-1], run_time=rt, rate_function=rt),
            )

    def expand_bubble(
        self, rt: float = 6, rf: float = linear, sca: float = 2.5
    ) -> AnimationGroup:
        """
        Animate bubble expansion with type-specific physical effects.

        The expansion animation varies by bubble type:
        - ``"energy_discussion"``: Shows energy transfer from bar to expanding bubble.
        - ``"GW"``: Displays gravitational wave emission during expansion.
        - ``"em"``: Expands brane with electromagnetic field.
        - ``"strings"``: Stretches strings radially as brane expands.
        - Other types: Standard brane scaling.

        :param rt: Run time of the animation. Default is ``6``.
        :type rt: float

        :param rf: Rate function controlling animation timing. Default is ``linear``.
        :type rf: function

        :param sca: Scaling factor for bubble expansion. Default is ``2.5``.
        :type sca: float

        :return: Animation showing bubble expansion with physical effects.
        :rtype: AnimationGroup or Succession
        """
        if self.bubble_type == "energy_discussion":
            return Succession(
                self.vacuum_tracker.animate(run_time=rt / 3, rate_func=rf).set_value(
                    4.5
                ),
                self.bubble[3].animate(run_time=rt, rate_func=rf).scale(sca),
            )

        if self.bubble_type == "GW":
            return AnimationGroup(
                self.brane_waves.animate(run_time=rt, rate_func=rf).scale(sca),
                Broadcast(
                    self.waves.scale(0.6 * sca),
                    focal_point=self.bubble[2].get_center(),
                    initial_opacity=1,
                    final_opacity=0,
                    n_mobs=15,
                    run_time=rt,
                    rate_func=rf,
                ),
            )

        if self.bubble_type == "em":
            return AnimationGroup(
                self.brane.animate(run_time=rt, rate_func=rf).scale(0.8 * sca),
                self.bubble[-2:].animate(run_time=rt, rate_func=rf).scale(0.8 * sca),
            )

        if self.bubble_type == "strings":
            return AnimationGroup(
                self.brane_w_anchor.animate(run_time=rt, rate_func=rf).scale(sca)
            )

        else:
            return AnimationGroup(
                self.brane.animate(run_time=rt, rate_func=rf).scale(sca)
            )

    def show_radius(self, rt: float = 1, rf: float = linear) -> Succession:
        """
        Display the time-dependent radius label r = a(τ) for the bubble.

        :param rt: Run time of the animation. Default is ``1``.
        :type rt: float

        :param rf: Rate function controlling animation timing. Default is ``linear``.
        :type rf: function

        :return: Animation showing radius line and time-dependent label.
        :rtype: Succession
        """
        return Succession(
            self.in_text.animate.next_to(self.brane.get_center(), DOWN, buff=0.2),
            Create(self.radius_info, run_time=rt, rate_function=rf),
        )
