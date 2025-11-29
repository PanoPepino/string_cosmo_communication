from ...my_imports import *
from ...objects import *
from ...tables_and_plots import *
from manim_slides.templates import TexFontTemplates

# RED AUTUMN TEMPLATE
# Warm autumn palette with rich red and orange tones

red_autumn = {
    "bg_color": "#FFF5EB",  # Warm cream background
    "brane_color": "#C0392B",  # Deep red for branes
    "brane_text_color": WHITE,  # White text on branes
    "brane_fill_opa": 0.05,  # Very light fill
    "brane_stroke_w": 1,  # Standard stroke
    "vacuum_color": "#D35400",  # Burnt orange vacuum
    "vacuum_fill_opa": 0.05,  # Very light fill
    "vacuum_stroke_w": 1,  # Standard stroke
    "vacuum_text_color": "#C0392B",  # Deep red text in vacuum
    "corner_rad": 0.05,  # Slightly rounded corners
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#C0392B",  # Deep red arrows
    "bh_color": "#E67E22",  # Warm orange for black holes
    "bh_fill_opa": 0.9,  # High opacity
    "string_color": "#C0392B",  # Deep red for strings
    "field_top_color": "#C0392B",  # Deep red for field tops
    "tex_temp": TexFontTemplates.droid_serif,  # Font for Tex and MathTex
}

# Apply background
config.background_color = red_autumn["bg_color"]

# Set TeX font defaults
Tex.set_default(tex_template=red_autumn['tex_temp'])
MathTex.set_default(tex_template=red_autumn['tex_temp'])

# Set defaults for string cosmology classes
Brane_General.set_default(
    brane_color=red_autumn["brane_color"],
    brane_fill_opa=red_autumn["brane_fill_opa"],
    brane_text_color=red_autumn["brane_text_color"],
    brane_stroke_w=red_autumn["brane_stroke_w"],
)

Vacuum_General.set_default(
    vacuum_color=red_autumn["vacuum_color"],
    vacuum_fill_opa=red_autumn["vacuum_fill_opa"],
    vacuum_stroke_w=red_autumn["vacuum_stroke_w"],
    vacuum_text_color=red_autumn["vacuum_text_color"],
    corner_rad=red_autumn["corner_rad"],
    corner_rad_direction=red_autumn["corner_rad_direction"],
)

AdS_Jc.set_default(
    arrow_color=red_autumn["arrow_color"]
)

Black_Hole.set_default(
    bh_color=red_autumn["bh_color"],
    bh_fill_opa=red_autumn["bh_fill_opa"],
)

Bubble.set_default(
    string_color=red_autumn["string_color"],
    field_top_color=red_autumn["field_top_color"],
)

Table_General.set_default(
    text_color=red_autumn["brane_color"],
    hlight_1_color=red_autumn["brane_color"],
    hlight_2_color=red_autumn["vacuum_color"],
    hlight_3_color=red_autumn["bh_color"],
    decorator_color=red_autumn["arrow_color"],
    decorator_stroke_w=red_autumn["brane_stroke_w"],
    corner_rad=red_autumn["corner_rad"],
    corner_rad_direction=red_autumn["corner_rad_direction"],
    stroke_w=red_autumn["brane_stroke_w"],
    stroke_opa=1,
    fill_opa=red_autumn["brane_fill_opa"],
)

Plot_General.set_default(
    func_main_color=red_autumn["brane_color"],
    func_2_color=red_autumn["vacuum_color"],
    func_3_color=red_autumn["bh_color"],
    text_color=red_autumn["brane_text_color"],
    axis_opacity=0.5,
    axis_stroke=red_autumn["brane_stroke_w"],
    decorator_presence="box",
    decorator_color=red_autumn["arrow_color"],
    decorator_stroke_w=red_autumn["brane_stroke_w"],
    corner_rad=red_autumn["corner_rad"],
    corner_rad_direction=red_autumn["corner_rad_direction"],
    fill_opa=red_autumn["brane_fill_opa"],
    stroke_w=red_autumn["brane_stroke_w"],
    stroke_opa=1,
    tightness=0.3,
)
