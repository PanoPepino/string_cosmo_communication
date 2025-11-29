from ..my_imports import *

__all__ = ["Table_General"]


class Table_General(VMobject):
    """
    Base class for all table objects providing common formatting and styling parameters.

    This class centralizes common input parameters for table creation in the string cosmology
    library, ensuring consistent styling across different table types through inheritance.
    It handles text colors, highlighting options, decorators, and corner styling.

    :param text_color: Primary color for table text content.
    :type text_color: ParsableManimColor, default=WHITE

    :param hlight_1_color: Primary highlight color for emphasizing specific cells.
    :type hlight_1_color: ParsableManimColor, default=GREEN

    :param hlight_2_color: Secondary highlight color for cell emphasis.
    :type hlight_2_color: ParsableManimColor, default=RED

    :param hlight_3_color: Tertiary highlight color for cell emphasis.
    :type hlight_3_color: ParsableManimColor, default=BLUE

    :param decorator_color: Color of the table border/frame decorator.
    :type decorator_color: ParsableManimColor, default=WHITE

    :param decorator_stroke_w: Stroke width of the decorator frame.
    :type decorator_stroke_w: float, default=1

    :param corner_rad: Base radius for rounded corners on table cells and decorators.
    :type corner_rad: float, default=0

    :param corner_rad_direction: List specifying which corners to round [UL, UR, DR, DL].
        Each element is multiplied by `corner_rad` to determine final corner radius.
    :type corner_rad_direction: list, default=[0, 0, 0, 0]

    :param stroke_w: General stroke width for table lines.
    :type stroke_w: float, default=1

    :param stroke_opa: Stroke opacity for table borders and dividers.
    :type stroke_opa: float, default=1

    :param fill_opa: Fill opacity for highlighted cells and backgrounds.
    :type fill_opa: float, default=0.3

    :param kwargs: Additional keyword arguments passed to :class:`VMobject`.

    .. seealso::

       - :class:`Table_Energy_Scales`
       - :class:`Table_Summary`
       - :class:`Table_BH_Embedding`

    **Example usage:**

    .. code-block:: python

        from manim import *
        from manim_string_cosmo import *

        class TableExample(Scene):
            def construct(self):
                # Create tables and arrange them
                table_group = VGroup(
                    Table_Summary_Induce(),
                    Table_Energy_Scales()
                ).arrange(RIGHT)

                table_group.scale_to_fit_width(config.frame_width - 1)
                self.add(table_group)
    """

    def __init__(
        self,
        text_color: ParsableManimColor = WHITE,
        hlight_1_color: ParsableManimColor = GREEN,
        hlight_2_color: ParsableManimColor = RED,
        hlight_3_color: ParsableManimColor = BLUE,
        decorator_color: ParsableManimColor = WHITE,
        decorator_stroke_w: float = 1,
        corner_rad: float = 0,
        corner_rad_direction: list = [0, 0, 0, 0],
        stroke_w: float = 1,
        stroke_opa: float = 1,
        fill_opa: float = 0.3,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.text_color = text_color
        self.hlight_1_color = hlight_1_color
        self.hlight_2_color = hlight_2_color
        self.hlight_3_color = hlight_3_color
        self.corner_rad = list(corner_rad * np.array(corner_rad_direction))
        self.decorator_color = decorator_color
        self.decorator_stroke_w = decorator_stroke_w
        self.stroke_w = stroke_w
        self.stroke_opa = stroke_opa
        self.fill_opa = fill_opa
