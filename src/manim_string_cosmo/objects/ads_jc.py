from ..my_imports import *
from .brane_general import *
from .vacuum_general import *

__all__ = ["AdS_Jc"]


class AdS_Jc(Vacuum_General, Brane_General, VGroup):
    """
    Represent vacuum discussions for Randall-Sundrum (RS) and Dark Bubble (DB) models.

    This class visualizes the brane-vacuum system with arrows to illustrate normal
    orientation changes across the brane. It includes animations for demonstrating
    Z₂ symmetry (RS case) and normal vector behavior in both models. The arrow
    element is always the last (``[-1]``) entry in the group.

    :param vacua_type: Type of vacuum configuration. Options:
        - ``"RS"``: Randall-Sundrum model with Z₂ symmetry.
        - ``"DB"``: Dark Bubble model with asymmetric vacua.
        Default is ``"DB"``.
    :type vacua_type: str

    :param arrow_color: Color of the normal vector arrow. Default is ``WHITE``.
    :type arrow_color: ParsableManimColor

    :param kwargs: Additional keyword arguments passed to :class:`Vacuum_General`,
        :class:`Brane_General`, and :class:`VGroup`.

    .. note::

       See :class:`Vacuum_General` and :class:`Brane_General` for additional
       inherited parameters related to vacuum and brane appearance.

    **Example usage:**

    .. code-block:: python

        from manim import *
        from manim_string_cosmo import AdS_Jc

        class Example_AdS_Jc(Scene):
            def construct(self):
                show_db = AdS_Jc(vacua_type="DB")
                show_rs = AdS_Jc(vacua_type="RS")
                show = VGroup(show_db, show_rs).arrange(RIGHT, aligned_edge=DOWN, buff=0.2)
                show.scale_to_fit_width(config.frame_width-2)

                self.play(AnimationGroup(*[x.fade_in() for x in show]))
                self.play(AnimationGroup(*[x.fade_in_arrow() for x in show]))
                self.play(show[1].show_symmetry(rt=5))
                self.play(show[1].restore_symmetry())
                self.play(AnimationGroup(show[0].show_n_vector_db(rt=5),
                                         show[1].show_n_vector_rs(rt=5)))
                self.play(show.animate.shift(2*UP))
                self.play(FadeOut(show))
    """

    def __init__(
        self, vacua_type: str = "DB", arrow_color: ParsableManimColor = WHITE, **kwargs
    ):
        super().__init__(**kwargs)

        # Geometry (RS)
        self.brane = Line(
            start=[0, -2, 0],
            end=[0, 2.2, 0],
            color=self.brane_color,
            stroke_width=self.brane_stroke_w + 1,
        )
        self.adskpRS = RoundedRectangle(
            corner_radius=self.corner_rad,
            height=4,
            width=4,
            stroke_width=self.vacuum_stroke_w,
            color=self.vacuum_color,
            fill_opacity=self.vacuum_fill_opa,
        )
        self.adskmRS = self.adskpRS.copy().flip()
        self.adskpRS.next_to(self.brane, RIGHT, buff=0.1, aligned_edge=DOWN)
        self.adskmRS.next_to(self.brane, LEFT, buff=0.1, aligned_edge=DOWN)

        # Text (RS)
        self.in_text_RS = (
            MathTex("\\Lambda_{5D}= -6 k_{-}^{2}", color=self.vacuum_text_color)
            .move_to(self.adskmRS.get_center())
            .shift(0.5 * DOWN)
        )
        self.out_text_RS = (
            self.in_text_RS.copy().move_to(self.adskpRS.get_center()).shift(0.5 * DOWN)
        )
        self.sym = MathTex("\\mathbb{Z}_{2}", color=self.brane_color).move_to(
            self.brane.get_corner(UL) + [0.3, 0.1, 0]
        )

        # Geometry (DB)
        self.adskpDB = RoundedRectangle(
            corner_radius=self.corner_rad,
            height=4,
            width=4,
            stroke_width=self.vacuum_stroke_w,
            color=self.vacuum_color,
            fill_opacity=self.vacuum_fill_opa,
        )
        self.adskmDB = RoundedRectangle(
            corner_radius=self.corner_rad,
            height=4,
            width=4,
            stroke_width=self.vacuum_stroke_w,
            color=self.vacuum_color,
            fill_opacity=self.vacuum_fill_opa + 0.3,
        ).flip()
        self.adskpDB.next_to(self.brane, RIGHT, buff=0.1, aligned_edge=DOWN)
        self.adskmDB.next_to(self.brane, LEFT, buff=0.1, aligned_edge=DOWN)

        # Text (DB)
        in_text_DB = (
            self.in_text_RS.copy().move_to(self.adskmDB.get_center()).shift(0.5 * DOWN)
        )
        self.out_text_DB = (
            MathTex("\\Lambda_{5D}= -6 k_{+}^{2}", color=self.vacuum_text_color)
            .move_to(self.adskpDB.get_center())
            .shift(0.5 * DOWN)
        )

        # Arrows
        self.arrowRS = Arrow(
            max_stroke_width_to_length_ratio=8,
            color=arrow_color,
            start=LEFT,
            end=[0.3, 0, 0],
        ).move_to(self.adskmRS.get_left())
        self.arrowDB = (
            self.arrowRS.copy().set_color(arrow_color).move_to(self.adskmDB.get_left())
        )

        if vacua_type == "RS":
            self.object = VGroup(
                self.brane,
                self.adskmRS,
                self.in_text_RS,
                self.adskpRS,
                self.out_text_RS,
                self.sym,
                self.arrowRS,
            )
            self.add(self.object)

        if vacua_type == "DB":
            self.object = VGroup(
                self.brane,
                self.adskmDB,
                in_text_DB,
                self.adskpDB,
                self.out_text_DB,
                self.arrowDB,
            )
            self.add(self.object)

    # Animations #
    @override_animation(FadeIn)
    def fade_in(
        self, rt: float = 1, rf: float = linear
    ) -> Animation:
        """
        Fade in the vacuum-brane system without the arrow.

        This method overrides the default :class:`FadeIn` animation to prevent
        scaling issues when adding elements to a group after initialization.

        :param rt: Run time of the animation. Default is ``1``.
        :type rt: float

        :param rf: Rate function controlling animation timing. Default is ``linear``.
        :type rf: function

        :return: FadeIn animation of all group elements except the arrow.
        :rtype: Animation
        """
        return FadeIn(self.object[:-1], run_time=rt, rate_function=rf)

    def fade_in_arrow(
        self, rt: float = 2, rf: float = linear
    ) -> Animation:
        """
        Fade in the normal vector arrow.

        :param rt: Run time of the animation. Default is ``2``.
        :type rt: float

        :param rf: Rate function controlling animation timing. Default is ``linear``.
        :type rf: function

        :return: FadeIn animation of the arrow element.
        :rtype: Animation
        """
        return FadeIn(self.object[-1], run_time=rt, rate_func=rf)

    def show_symmetry(
        self, rt: float = 2, rf=linear
    ) -> Succession:
        """
        Demonstrate Z₂ symmetry by folding the outside vacuum.

        This animation removes the outside vacuum and rotates the inside vacuum
        about the brane to simulate the Z₂ symmetry operation.

        :param rt: Run time of the animation. Default is ``2``.
        :type rt: float

        :param rf: Rate function controlling animation timing. Default is ``linear``.
        :type rf: function

        :return: Animation showing Z₂ symmetry folding.
        :rtype: Succession

        .. note::

           This method only works with RS-type (``vacua_type="RS"``). The Dark Bubble
           model has distinct inside and outside vacua without this symmetry.
        """
        return Succession(
            FadeOut(self.object[-3], run_time=rt / 2, rate_func=rf),
            Rotate(
                self.object[-4],
                about_point=self.object[0].get_center(),
                axis=[0, -1, 0],
                run_time=rt / 2,
                rate_func=rf,
            ),
        )

    def restore_symmetry(self, rt: float = 2, rf=linear) -> Succession:
        """
        Restore the original vacuum configuration after symmetry demonstration.

        :param rt: Run time of the animation. Default is ``2``.
        :type rt: float

        :param rf: Rate function controlling animation timing. Default is ``linear``.
        :type rf: function

        :return: Animation restoring the unfolded configuration.
        :rtype: Succession
        """
        return Succession(
            Rotate(
                self.object[-4],
                about_point=self.object[0].get_center(),
                axis=[0, 1, 0],
                run_time=rt / 2,
                rate_func=rf,
            ),
            FadeIn(self.object[-3], run_time=rt / 2, rate_func=rf),
        )

    def show_n_vector_rs(self, rt: float = 2, rf=linear) -> Succession:
        """
        Show the behavior of the normal vector across vacua in the RS model.

        Demonstrates how the normal vector changes orientation when crossing
        the brane in the Randall-Sundrum scenario with Z₂ symmetry.

        :param rt: Run time of the animation. Default is ``2``.
        :type rt: float

        :param rf: Rate function controlling animation timing. Default is ``linear``.
        :type rf: function

        :return: Animation showing normal vector evolution across the brane.
        :rtype: Succession
        """
        center = self.object[0].get_center()

        return Succession(
            self.object[-1].animate(rate_func=rf).move_to(center).build(),
            Rotate(self.object[-1], angle=PI, about_point=center, rate_func=rf),
            self.object[-1]
            .animate(rate_func=rf)
            .rotate(PI)
            .move_to(self.object.get_right()),
            run_time=rt,
            rate_func=rf,
        )

    def show_n_vector_db(self, rt: float = 2, rf=linear) -> Succession:
        """
        Show the behavior of the normal vector across vacua in the DB model.

        Demonstrates how the normal vector maintains consistent orientation
        in the Dark Bubble model where vacua have distinct properties.

        :param rt: Run time of the animation. Default is ``2``.
        :type rt: float

        :param rf: Rate function controlling animation timing. Default is ``linear``.
        :type rf: function

        :return: Animation showing normal vector behavior in asymmetric vacua.
        :rtype: Succession
        """
        return Succession(
            self.object[-1].animate(rate_func=rf).move_to(self.object.get_right()),
            run_time=rt,
            rate_func=rf,
        )
