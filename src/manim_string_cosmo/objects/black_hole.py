from ..my_imports import *
from .brane_general import *

__all__ = ["Black_Hole"]


class Black_Hole(Brane_General, VGroup):
    """
    Create a black hole group that can potentially emit a brane.

    This class visualizes different types of black holes in string cosmology,
    including fragmentation scenarios (AdS fragmentation à la Maldacena) and
    spinning black holes. The expanding bubble is always the last (``[-1]``) element
    of the object.

    :param bh_size: Size (radius) of the black hole. Default is ``brane_radius`` from
        :class:`Brane_General` (typically 1).
    :type bh_size: float

    :param bh_color: Color of the black hole. Default is ``BLACK``.
    :type bh_color: ParsableManimColor

    :param bh_fill_opa: Fill opacity of the black hole. Default is ``0.8``.
    :type bh_fill_opa: float

    :param bh_type: Type of black hole visualization. Options:
        - ``"fragmentation"``: Shows Q > T text, representing brane nucleation via AdS fragmentation.
        - ``"spinning"``: Shows theta and mu parameters for a rotating black hole.
        - ``"none"``: Empty black hole without text labels.
        Default is ``"none"``.
    :type bh_type: str

    :param kwargs: Additional keyword arguments passed to :class:`Brane_General` and :class:`VGroup`.

    .. note::

       The expanding bubble (brane) is always accessible as the last element (``[-1]``) of the object.
       See :class:`Brane_General` for additional inherited parameters.

    **Example usage:**

    .. code-block:: python

        from manim import *
        from manim_string_cosmo import Black_Hole

        class Example_Black_Hole(Scene):
            def construct(self):
                bh_sp = Black_Hole(bh_type="spinning")
                bh_frag = Black_Hole(bh_type="fragmentation")
                bh = Black_Hole()
                bh_group = VGroup(bh_sp, bh_frag, bh).arrange(RIGHT, buff=3)
                bh_group.scale_to_fit_width(config.frame_width-1)
                self.add(bh_group)
                self.play(AnimationGroup(*[x.nucleate() for x in bh_group]))
                self.play(AnimationGroup(*[x.expand() for x in bh_group]))
    """

    def __init__(
        self,
        bh_size: float = Brane_General().brane_radius,
        bh_color: ParsableManimColor = BLACK,
        bh_fill_opa: float = 0.8,
        bh_type: str = "none",
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.bh_type = bh_type
        # Geometry

        bh = Circle(
            radius=bh_size,
            color=bh_color,
            fill_opacity=bh_fill_opa,
            stroke_width=self.brane_stroke_w,
        ).set_z_index(3)
        self.brane = Circle(
            radius=bh_size,
            color=self.brane_color,
            fill_opacity=self.brane_fill_opa,
            stroke_width=1,
        )
        self.theta_path = Circle(
            radius=bh_size - (bh_size * 3 / 10),
            color=WHITE,
            fill_opacity=0,
            stroke_width=0,
        )

        # Text
        qt = (
            MathTex("Q > T", font_size=35 * bh_size, color=self.brane_text_color)
            .move_to(bh.get_center())
            .set_z_index(8)
        )
        self.mu = (
            MathTex("\\mu", font_size=35 * bh_size, color=self.brane_text_color)
            .move_to(bh.get_center())
            .set_z_index(7)
        )
        self.theta = (
            MathTex("\\theta", font_size=35 * bh_size, color=self.brane_text_color)
            .move_to(self.theta_path.get_right())
            .set_z_index(7)
        )

        if self.bh_type == "spinning":
            self.add(self.brane, bh, self.mu, self.theta, self.theta_path)
        if self.bh_type == "fragmentation":
            self.add(self.brane, bh, qt)
        if self.bh_type == "none":
            self.add(self.brane, bh)

    def nucleate(
        self, rt: float = 0.5, rf: float = linear, scaling: float = 1.1
    ) -> Animation:
        """
        Animate the nucleation of a brane through the black hole horizon.

        :param rt: Run time of the animation. Default is ``0.5``.
        :type rt: float

        :param rf: Rate function controlling animation timing. Default is ``linear``.
        :type rf: function

        :param scaling: Scaling factor for the brane during nucleation. Default is ``1.1``.
        :type scaling: float

        :return: Animation showing brane nucleation through the horizon.
        :rtype: AnimationGroup
        """
        return AnimationGroup(
            self.brane.animate(run_time=rt, rate_func=rf).scale(scaling)
        )

    def expand(
        self, rt: float = 3, rf: float = linear, scaling: float = 2.5
    ) -> Animation:
        """
        Animate the expansion of the nucleated brane.

        For spinning black holes (``bh_type="spinning"``), this also animates the
        theta parameter moving along its circular path.

        :param rt: Run time of the animation. Default is ``3``.
        :type rt: float

        :param rf: Rate function controlling animation timing. Default is ``linear``.
        :type rf: function

        :param scaling: Scaling factor for the brane expansion. Default is ``2.5``.
        :type scaling: float

        :return: Animation showing brane expansion. For spinning type, includes theta motion.
        :rtype: AnimationGroup
        """
        if self.bh_type == "spinning":
            return AnimationGroup(
                self.brane.animate(run_time=rt, rate_func=rf).scale(scaling),
                MoveAlongPath(self.theta, self.theta_path, run_time=rt, rate_func=rf),
            )

        else:
            return AnimationGroup(
                self.brane.animate(run_time=rt, rate_func=rf).scale(scaling)
            )
