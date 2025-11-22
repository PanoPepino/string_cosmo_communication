from ...my_imports import *
from ...objects import *

green_mint = {
    "bg_color": "#F2FFFB",
    "text_color": "#006661",
    "decorator_color": "#006661",
    "decorator_color_2": "#7DB873",
    "decorator_color_3": "#0AD46C",
    "decorator_color_4": "#C6FF7C",
    "corner_rad": 0.1,
    "corner_rad_direction": [1, 1, 0, 1],
    "fill_opa": 0.1,
    "stroke_opa": 0.5
}

config.background_color = green_mint['bg_color']

Brane_General.set_default(
    brane_color=green_mint["decorator_color_2"],
    brane_fill_opa=green_mint["fill_opa"],
    brane_text_color=green_mint["text_color"],
    brane_stroke_w=2
)
Vacuum_General.set_default(
    vacuum_color=green_mint["decorator_color_3"],
    vacuum_fill_opa=green_mint["fill_opa"],
    vacuum_stroke_w=1,
    vacuum_text_color=green_mint["text_color"],
    corner_rad=green_mint["corner_rad"],
    corner_rad_direction=green_mint["corner_rad_direction"]
)

AdS_Jc.set_default(arrow_color=green_mint["decorator_color"])

Black_Hole.set_default(bh_color=green_mint["decorator_color_4"], bh_fill_opa=0.9)

Bubble.set_default(string_color=green_mint["decorator_color_4"],
                  field_top_color=green_mint["decorator_color_2"])
