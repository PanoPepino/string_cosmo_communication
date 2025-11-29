from ..my_imports import *

__all__ = ["Brane_General"]


class Brane_General(VGroup):
    """
    Base class providing common initialization parameters for brane objects.

    This is a mock-up class to centralize all input parameters related to branes
    and associated objects, including color, size, opacity, and stroke properties.

    :param brane_color: Filling color of the brane. Default is ``RED``.
    :type brane_color: ParsableManimColor

    :param brane_radius: Initial size (radius) of the brane. Default is ``1``.
    :type brane_radius: float

    :param brane_fill_opa: Fill opacity of the brane. Note that fill opacity may vary
        when representing different AdS scales. Default is ``0.1``.
    :type brane_fill_opa: float

    :param brane_stroke_w: Stroke width of the brane border. Default is ``0.2``.
    :type brane_stroke_w: float

    :param brane_text_color: Color of text elements associated with the brane. Default is ``WHITE``.
    :type brane_text_color: ParsableManimColor

    :param kwargs: Additional keyword arguments passed to :class:`VGroup`.

    .. note::

       This class is designed to be inherited by other brane-related classes
       to ensure consistent parameter handling across different brane representations.
    """

    def __init__(
        self,
        brane_color: ParsableManimColor = RED,
        brane_radius: float = 1,
        brane_fill_opa: float = 0.1,
        brane_stroke_w: float = 0.2,
        brane_text_color: ParsableManimColor = WHITE,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.brane_color = brane_color
        self.brane_fill_opa = brane_fill_opa
        self.brane_radius = brane_radius
        self.brane_text_color = brane_text_color
        self.brane_stroke_w = brane_stroke_w
