from ...my_imports import *
from ...objects import *

blue_ice = {
    "bg_color": "#F1F8FF",
    "text_color": "#003E7C",
    "decorator_color": "#003E7C",
    "decorator_color_2": "#7973B8",
    "decorator_color_3": "#A0BCFC",
    "decorator_color_4": "#7CDAFF",
    "corner_rad": 0.05,
    "corner_rad_direction": [1,1,1,1],
    "fill_opa": 0.05,
    "stroke_opa": 1
}

config.background_color = blue_ice['bg_color']

Brane_General.set_default(
    brane_color=blue_ice["decorator_color_2"],
    brane_fill_opa=blue_ice["fill_opa"],
    brane_text_color=blue_ice["text_color"],
    brane_stroke_w=2
)
Vacuum_General.set_default(
    vacuum_color=blue_ice["decorator_color_3"],
    vacuum_fill_opa=blue_ice["fill_opa"],
    vacuum_stroke_w=1,
    vacuum_text_color=blue_ice["text_color"],
    corner_rad=blue_ice["corner_rad"],
    corner_rad_direction=blue_ice["corner_rad_direction"]
)

AdS_Jc.set_default(arrow_color=blue_ice["decorator_color"])

Black_Hole.set_default(bh_color=blue_ice["decorator_color_4"], bh_fill_opa=0.9)

Bubble.set_default(string_color=blue_ice["decorator_color_4"], field_top_color=blue_ice["decorator_color_2"])
