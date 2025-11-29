from ...my_imports import *
from ...objects import *
from ...tables_and_plots import *
from manim_slides.templates import TexFontTemplates

# GREEN MINT TEMPLATE
# Fresh minty green palette with light background

green_mint = {
    "bg_color": "#F0FFF4",  # Mint cream background
    "brane_color": "#22543D",  # Deep green for branes
    "brane_text_color": WHITE,  # White text on branes
    "brane_fill_opa": 0.05,  # Very light fill
    "brane_stroke_w": 1,  # Standard stroke
    "vacuum_color": "#48BB78",  # Fresh green vacuum
    "vacuum_fill_opa": 0.05,  # Very light fill
    "vacuum_stroke_w": 1,  # Standard stroke
    "vacuum_text_color": "#22543D",  # Deep green text in vacuum
    "corner_rad": 0.05,  # Slightly rounded corners
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#22543D",  # Deep green arrows
    "bh_color": "#9AE6B4",  # Light mint for black holes
    "bh_fill_opa": 0.9,  # High opacity
    "string_color": "#22543D",  # Deep green for strings
    "field_top_color": "#22543D",  # Deep green for field tops
    "tex_temp": TexFontTemplates.droid_serif,  # Font for Tex and MathTex
}

# Apply background
config.background_color = green_mint["bg_color"]

# Set TeX font defaults
Tex.set_default(tex_template=green_mint['tex_temp'])
MathTex.set_default(tex_template=green_mint['tex_temp'])

# Set defaults for string cosmology classes
Brane_General.set_default(
    brane_color=green_mint["brane_color"],
    brane_fill_opa=green_mint["brane_fill_opa"],
    brane_text_color=green_mint["brane_text_color"],
    brane_stroke_w=green_mint["brane_stroke_w"],
)

Vacuum_General.set_default(
    vacuum_color=green_mint["vacuum_color"],
    vacuum_fill_opa=green_mint["vacuum_fill_opa"],
    vacuum_stroke_w=green_mint["vacuum_stroke_w"],
    vacuum_text_color=green_mint["vacuum_text_color"],
    corner_rad=green_mint["corner_rad"],
    corner_rad_direction=green_mint["corner_rad_direction"],
)

AdS_Jc.set_default(
    arrow_color=green_mint["arrow_color"]
)

Black_Hole.set_default(
    bh_color=green_mint["bh_color"],
    bh_fill_opa=green_mint["bh_fill_opa"],
)

Bubble.set_default(
    string_color=green_mint["string_color"],
    field_top_color=green_mint["field_top_color"],
)

Table_General.set_default(
    text_color=green_mint["brane_color"],
    hlight_1_color=green_mint["brane_color"],
    hlight_2_color=green_mint["vacuum_color"],
    hlight_3_color=green_mint["bh_color"],
    decorator_color=green_mint["arrow_color"],
    decorator_stroke_w=green_mint["brane_stroke_w"],
    corner_rad=green_mint["corner_rad"],
    corner_rad_direction=green_mint["corner_rad_direction"],
    stroke_w=green_mint["brane_stroke_w"],
    stroke_opa=1,
    fill_opa=green_mint["brane_fill_opa"],
)

Plot_General.set_default(
    func_main_color=green_mint["brane_color"],
    func_2_color=green_mint["vacuum_color"],
    func_3_color=green_mint["bh_color"],
    text_color=green_mint["brane_text_color"],
    axis_opacity=0.5,
    axis_stroke=green_mint["brane_stroke_w"],
    decorator_presence="box",
    decorator_color=green_mint["arrow_color"],
    decorator_stroke_w=green_mint["brane_stroke_w"],
    corner_rad=green_mint["corner_rad"],
    corner_rad_direction=green_mint["corner_rad_direction"],
    fill_opa=green_mint["brane_fill_opa"],
    stroke_w=green_mint["brane_stroke_w"],
    stroke_opa=1,
    tightness=0.3,
)
