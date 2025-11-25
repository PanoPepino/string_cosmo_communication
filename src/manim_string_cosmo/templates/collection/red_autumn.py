from ...my_imports import *
from ...objects import *

red_autumn = {
    "bg_color": "#FAF9F5",
    "text_color": "#81331B",
    "decorator_color": "#81331B",
    "decorator_color_2": "#B87390",
    "decorator_color_3": "#F49191",
    "decorator_color_4": "#FFC67C",
    "corner_rad": -0.05,
    "corner_rad_direction": [1,0,0,0],
    "fill_opa": 0.1,
    "stroke_opa": 0.2
}

config.background_color = red_autumn['bg_color']

Brane_General.set_default(
    brane_color=red_autumn["decorator_color_2"],
    brane_fill_opa=red_autumn["fill_opa"],
    brane_text_color=red_autumn["text_color"],
    brane_stroke_w=2
)
Vacuum_General.set_default(
    vacuum_color=red_autumn["decorator_color_3"],
    vacuum_fill_opa=red_autumn["fill_opa"],
    vacuum_stroke_w=1,
    vacuum_text_color=red_autumn["text_color"],
    corner_rad=red_autumn["corner_rad"],
    corner_rad_direction=red_autumn["corner_rad_direction"]
)

AdS_Jc.set_default(arrow_color=red_autumn["decorator_color"])

Black_Hole.set_default(bh_color=red_autumn["decorator_color_4"], bh_fill_opa=0.9)

Bubble.set_default(string_color=red_autumn["decorator_color_4"], field_top_color=red_autumn["decorator_color_2"])
