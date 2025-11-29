from ..my_imports import *

__all__ = ["Plot_General"]


class Plot_General(Group):
    """
    Base class for all plot objects providing common styling and configuration parameters.

    This class serves as a foundation for various plot types in the string cosmology package,
    centralizing visual properties such as colors, opacity, decorators, and stroke settings.
    All plot-specific classes inherit from this to ensure consistent appearance across
    different visualization types.

    :param func_main_color: Primary function curve color.
    :type func_main_color: ParsableManimColor, default=GREEN

    :param func_2_color: Secondary function curve color.
    :type func_2_color: ParsableManimColor, default=RED

    :param func_3_color: Tertiary function curve color.
    :type func_3_color: ParsableManimColor, default=BLUE

    :param text_color: Color for text labels and annotations.
    :type text_color: ParsableManimColor, default=WHITE

    :param axis_opacity: Opacity level for axis lines.
    :type axis_opacity: float, default=0.5

    :param axis_stroke: Stroke width for axis lines.
    :type axis_stroke: float, default=1

    :param decorator_presence: Style of decorator around the plot. Options include:
        ``"box"`` for a surrounding rectangle, or ``"no"`` for plain presentation.
    :type decorator_presence: str, default="box"

    :param decorator_color: Color of the decorator frame.
    :type decorator_color: ParsableManimColor, default=WHITE

    :param decorator_stroke_w: Stroke width of the decorator frame.
    :type decorator_stroke_w: float, default=1

    :param corner_rad: Base radius for rounded corners on decorators.
    :type corner_rad: float, default=0

    :param corner_rad_direction: List specifying which corners to round [UL, UR, DR, DL].
        Each element is multiplied by `corner_rad` to determine final radius.
    :type corner_rad_direction: list, default=[0, 0, 0, 0]

    :param fill_opa: Fill opacity for decorator backgrounds.
    :type fill_opa: float, default=0.1

    :param stroke_w: General stroke width for plot elements.
    :type stroke_w: float, default=1

    :param stroke_opa: Stroke opacity for plot elements.
    :type stroke_opa: float, default=1

    :param tightness: Buffer distance between plot content and decorator frame.
    :type tightness: float, default=0.3

    :param kwargs: Additional keyword arguments passed to :class:`Group`.

    .. note::

       To scale any graph with respect to its center, use:
       ``graph.scale(3, about_point=graph.ax_ins.c2p(0, 0, 0))``

    .. seealso::

       - :class:`Plot_Instanton`
       - :class:`Plot_Quantum`
       - :class:`Plot_Tension`

    **Example usage:**

    .. code-block:: python

        from manim import *
        from manim_string_cosmo import *

        class PlotExample(Scene):
            def construct(self):
                # Create a custom plot with specific colors
                plot = Plot_General(
                    func_main_color=BLUE,
                    text_color=YELLOW,
                    decorator_presence="box",
                    corner_rad=0.1,
                    corner_rad_direction=[1, 1, 1, 1]
                )
                self.add(plot)
    """

    def __init__(
        self,
        func_main_color: ParsableManimColor = GREEN,
        func_2_color: ParsableManimColor = RED,
        func_3_color: ParsableManimColor = BLUE,
        text_color: ParsableManimColor = WHITE,
        axis_opacity: float = 0.5,
        axis_stroke: float = 1,
        decorator_presence: str = "box",
        decorator_color: ParsableManimColor = WHITE,
        decorator_stroke_w: float = 1,
        corner_rad: float = 0,
        corner_rad_direction: list = [0, 0, 0, 0],
        fill_opa: float = 0.1,
        stroke_w: float = 1,
        stroke_opa: float = 1,
        tightness: float = 0.3,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.func_main_color = func_main_color
        self.func_2_color = func_2_color
        self.func_3_color = func_3_color
        self.text_color = text_color
        self.axis_opacity = axis_opacity
        self.axis_stroke = axis_stroke
        self.decorator_presence = decorator_presence
        self.decorator_color = decorator_color
        self.decorator_stroke_w = decorator_stroke_w
        self.corner_rad = list(corner_rad * np.array(corner_rad_direction))
        self.fill_opa = fill_opa
        self.stroke_w = stroke_w
        self.stroke_opa = stroke_opa
        self.tightness = tightness
