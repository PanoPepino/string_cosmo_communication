from ...my_imports import *
from ...objects import *
from ...tables_and_plots import *
from manim_slides.templates import TexFontTemplates

# DARK ENERGY TEMPLATE
# Deep purple theme with dark cosmic background

dark_energy = {
    "bg_color": "#0F0F1E",  # Deep space background
    "brane_color": "#9D4EDD",  # Vibrant purple for branes
    "brane_text_color": "#F8F8FF",  # Ghostwhite text on branes
    "brane_fill_opa": 0.4,  # Medium fill
    "brane_stroke_w": 1.5,  # Medium-thick stroke
    "vacuum_color": "#C77DFF",  # Light purple vacuum
    "vacuum_fill_opa": 0.4,  # Medium fill
    "vacuum_stroke_w": 1.5,  # Medium-thick stroke
    "vacuum_text_color": "#F8F8FF",  # Ghostwhite text in vacuum
    "corner_rad": 0.08,  # Rounded corners
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#9D4EDD",  # Purple arrows
    "bh_color": "#E0AAFF",  # Pale purple for black holes
    "bh_fill_opa": 0.4,  # Medium opacity
    "string_color": "#C77DFF",  # Light purple for strings
    "field_top_color": "#9D4EDD",  # Vibrant purple for field tops
    "tex_temp": TexFontTemplates.droid_serif,  # Font for Tex and MathTex
}

# Apply background
config.background_color = dark_energy["bg_color"]

# Set TeX font defaults
Tex.set_default(tex_template=dark_energy['tex_temp'])
MathTex.set_default(tex_template=dark_energy['tex_temp'])

# Set defaults for string cosmology classes
Brane_General.set_default(
    brane_color=dark_energy["brane_color"],
    brane_fill_opa=dark_energy["brane_fill_opa"],
    brane_text_color=dark_energy["brane_text_color"],
    brane_stroke_w=dark_energy["brane_stroke_w"],
)

Vacuum_General.set_default(
    vacuum_color=dark_energy["vacuum_color"],
    vacuum_fill_opa=dark_energy["vacuum_fill_opa"],
    vacuum_stroke_w=dark_energy["vacuum_stroke_w"],
    vacuum_text_color=dark_energy["vacuum_text_color"],
    corner_rad=dark_energy["corner_rad"],
    corner_rad_direction=dark_energy["corner_rad_direction"],
)

AdS_Jc.set_default(
    arrow_color=dark_energy["arrow_color"]
)

Black_Hole.set_default(
    bh_color=dark_energy["bh_color"],
    bh_fill_opa=dark_energy["bh_fill_opa"],
)

Bubble.set_default(
    string_color=dark_energy["string_color"],
    field_top_color=dark_energy["field_top_color"],
)

Table_General.set_default(
    text_color=dark_energy["brane_color"],
    hlight_1_color=dark_energy["brane_color"],
    hlight_2_color=dark_energy["vacuum_color"],
    hlight_3_color=dark_energy["bh_color"],
    decorator_color=dark_energy["arrow_color"],
    decorator_stroke_w=dark_energy["brane_stroke_w"],
    corner_rad=dark_energy["corner_rad"],
    corner_rad_direction=dark_energy["corner_rad_direction"],
    stroke_w=dark_energy["brane_stroke_w"],
    stroke_opa=1,
    fill_opa=dark_energy["brane_fill_opa"],
)

Plot_General.set_default(
    func_main_color=dark_energy["brane_color"],
    func_2_color=dark_energy["vacuum_color"],
    func_3_color=dark_energy["bh_color"],
    text_color=dark_energy["brane_text_color"],
    axis_opacity=0.5,
    axis_stroke=dark_energy["brane_stroke_w"],
    decorator_presence="box",
    decorator_color=dark_energy["arrow_color"],
    decorator_stroke_w=dark_energy["brane_stroke_w"],
    corner_rad=dark_energy["corner_rad"],
    corner_rad_direction=dark_energy["corner_rad_direction"],
    fill_opa=dark_energy["brane_fill_opa"],
    stroke_w=dark_energy["brane_stroke_w"],
    stroke_opa=1,
    tightness=0.3,
)
