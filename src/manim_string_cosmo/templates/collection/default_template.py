from ...my_imports import *
from ...objects import *
from ...tables_and_plots import *
from manim_slides.templates import TexFontTemplates

# DEFAULT TEMPLATE
# Classic black and white theme with high contrast

default_template = {
    "bg_color": "#000000",  # Black background
    "brane_color": "#FFFFFF",  # White for branes
    "brane_text_color": "#000000",  # Black text on branes
    "brane_fill_opa": 0.2,  # Light fill
    "brane_stroke_w": 1,  # Standard stroke
    "vacuum_color": "#888888",  # Gray vacuum
    "vacuum_fill_opa": 0.2,  # Light fill
    "vacuum_stroke_w": 1,  # Standard stroke
    "vacuum_text_color": "#FFFFFF",  # White text in vacuum
    "corner_rad": 0,  # Sharp corners
    "corner_rad_direction": [0, 0, 0, 0],  # No rounding
    "arrow_color": "#FFFFFF",  # White arrows
    "bh_color": "#CCCCCC",  # Light gray for black holes
    "bh_fill_opa": 0.2,  # Light opacity
    "string_color": "#FFFFFF",  # White for strings
    "field_top_color": "#FFFFFF",  # White for field tops
    "tex_temp": TexFontTemplates.droid_serif,  # Font for Tex and MathTex
}

# Apply background
config.background_color = default_template["bg_color"]

# Set TeX font defaults
Tex.set_default(tex_template=default_template['tex_temp'])
MathTex.set_default(tex_template=default_template['tex_temp'])

# Set defaults for string cosmology classes
Brane_General.set_default(
    brane_color=default_template["brane_color"],
    brane_fill_opa=default_template["brane_fill_opa"],
    brane_text_color=default_template["brane_text_color"],
    brane_stroke_w=default_template["brane_stroke_w"],
)

Vacuum_General.set_default(
    vacuum_color=default_template["vacuum_color"],
    vacuum_fill_opa=default_template["vacuum_fill_opa"],
    vacuum_stroke_w=default_template["vacuum_stroke_w"],
    vacuum_text_color=default_template["vacuum_text_color"],
    corner_rad=default_template["corner_rad"],
    corner_rad_direction=default_template["corner_rad_direction"],
)

AdS_Jc.set_default(
    arrow_color=default_template["arrow_color"]
)

Black_Hole.set_default(
    bh_color=default_template["bh_color"],
    bh_fill_opa=default_template["bh_fill_opa"],
)

Bubble.set_default(
    string_color=default_template["string_color"],
    field_top_color=default_template["field_top_color"],
)

Table_General.set_default(
    text_color=default_template["brane_color"],
    hlight_1_color=default_template["brane_color"],
    hlight_2_color=default_template["vacuum_color"],
    hlight_3_color=default_template["bh_color"],
    decorator_color=default_template["arrow_color"],
    decorator_stroke_w=default_template["brane_stroke_w"],
    corner_rad=default_template["corner_rad"],
    corner_rad_direction=default_template["corner_rad_direction"],
    stroke_w=default_template["brane_stroke_w"],
    stroke_opa=1,
    fill_opa=default_template["brane_fill_opa"],
)

Plot_General.set_default(
    func_main_color=default_template["brane_color"],
    func_2_color=default_template["vacuum_color"],
    func_3_color=default_template["bh_color"],
    text_color=default_template["brane_text_color"],
    axis_opacity=0.5,
    axis_stroke=default_template["brane_stroke_w"],
    decorator_presence="box",
    decorator_color=default_template["arrow_color"],
    decorator_stroke_w=default_template["brane_stroke_w"],
    corner_rad=default_template["corner_rad"],
    corner_rad_direction=default_template["corner_rad_direction"],
    fill_opa=default_template["brane_fill_opa"],
    stroke_w=default_template["brane_stroke_w"],
    stroke_opa=1,
    tightness=0.3,
)
