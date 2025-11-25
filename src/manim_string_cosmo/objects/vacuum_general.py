from ..my_imports import *

__all__ = ["Vacuum_General"]


class Vacuum_General(VGroup):
    """
    Base class providing common initialization parameters for vacuum objects.

    This class centralizes all input parameters related to the color, shape,
    and appearance of vacuum representations in string cosmology visualizations.

    :param vacuum_color: Color of the vacuum representation. Default is ``RED``.
    :type vacuum_color: ParsableManimColor

    :param vacuum_fill_opa: Fill opacity of the vacuum. Default is ``0.2``.
    :type vacuum_fill_opa: float

    :param vacuum_stroke_w: Stroke width of the vacuum border. Default is ``0.2``.
    :type vacuum_stroke_w: float

    :param vacuum_text_color: Color of text elements associated with the vacuum. Default is ``WHITE``.
    :type vacuum_text_color: ParsableManimColor

    :param corner_rad: Corner radius of the surrounding box. Default is ``0``.
    :type corner_rad: float

    :param corner_rad_direction: List of four integers controlling which corners of the
        surrounding rectangle get rounded: [top-left, top-right, bottom-right, bottom-left].
        Default is ``[0, 0, 0, 0]``.
    :type corner_rad_direction: list[int]

    :param kwargs: Additional keyword arguments passed to :class:`VGroup`.

    .. note::

       This class is designed to be inherited by other vacuum-related classes
       to ensure consistent parameter handling across different vacuum representations.
    """

    def __init__(
        self,
        vacuum_color: ParsableManimColor = RED,
        vacuum_fill_opa: float = 0.2,
        vacuum_stroke_w: float = 0.2,
        vacuum_text_color: ParsableManimColor = WHITE,
        corner_rad: float = 0,
        corner_rad_direction: list = [0, 0, 0, 0],
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.vacuum_color = vacuum_color
        self.vacuum_fill_opa = vacuum_fill_opa
        self.vacuum_stroke_w = vacuum_stroke_w
        self.corner_rad = list(corner_rad * np.array(corner_rad_direction))
        self.vacuum_text_color = vacuum_text_color
        self.cr = (
            corner_rad  # To give the scalar value when displaying strings in the bubble
        )
