from ...my_imports import *
from ...objects import *
from ...tables_and_plots import *
from manim_slides.templates import TexFontTemplates

# QUANTUM DUSK TEMPLATE
# Dusky purple theme with warm accent colors

quantum_dusk = {
    "bg_color": "#2D1B3D",  # Deep dusky purple background
    "brane_color": "#D4A5A5",  # Dusty rose for branes
    "brane_text_color": "#2D1B3D",  # Dark text on branes
    "brane_fill_opa": 0.4,  # Medium fill
    "brane_stroke_w": 1,  # Standard stroke
    "vacuum_color": "#C49B9B",  # Warm mauve vacuum
    "vacuum_fill_opa": 0.4,  # Medium fill
    "vacuum_stroke_w": 1,  # Standard stroke
    "vacuum_text_color": "#2D1B3D",  # Dark text in vacuum
    "corner_rad": 0.08,  # Rounded corners
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#D4A5A5",  # Dusty rose arrows
    "bh_color": "#E8C4C4",  # Light pink for black holes
    "bh_fill_opa": 0.9,  # High opacity
    "string_color": "#D4A5A5",  # Dusty rose for strings
    "field_top_color": "#D4A5A5",  # Dusty rose for field tops
    "tex_temp": TexFontTemplates.droid_serif,  # Font for Tex and MathTex
}

# Apply background
config.background_color = quantum_dusk["bg_color"]

# Set TeX font defaults
Tex.set_default(tex_template=quantum_dusk['tex_temp'])
MathTex.set_default(tex_template=quantum_dusk['tex_temp'])

# Set defaults for string cosmology classes
Brane_General.set_default(
    brane_color=quantum_dusk["brane_color"],
    brane_fill_opa=quantum_dusk["brane_fill_opa"],
    brane_text_color=quantum_dusk["brane_text_color"],
    brane_stroke_w=quantum_dusk["brane_stroke_w"],
)

Vacuum_General.set_default(
    vacuum_color=quantum_dusk["vacuum_color"],
    vacuum_fill_opa=quantum_dusk["vacuum_fill_opa"],
    vacuum_stroke_w=quantum_dusk["vacuum_stroke_w"],
    vacuum_text_color=quantum_dusk["vacuum_text_color"],
    corner_rad=quantum_dusk["corner_rad"],
    corner_rad_direction=quantum_dusk["corner_rad_direction"],
)

AdS_Jc.set_default(
    arrow_color=quantum_dusk["arrow_color"]
)

Black_Hole.set_default(
    bh_color=quantum_dusk["bh_color"],
    bh_fill_opa=quantum_dusk["bh_fill_opa"],
)

Bubble.set_default(
    string_color=quantum_dusk["string_color"],
    field_top_color=quantum_dusk["field_top_color"],
)

Table_General.set_default(
    text_color=quantum_dusk["brane_color"],
    hlight_1_color=quantum_dusk["brane_color"],
    hlight_2_color=quantum_dusk["vacuum_color"],
    hlight_3_color=quantum_dusk["bh_color"],
    decorator_color=quantum_dusk["arrow_color"],
    decorator_stroke_w=quantum_dusk["brane_stroke_w"],
    corner_rad=quantum_dusk["corner_rad"],
    corner_rad_direction=quantum_dusk["corner_rad_direction"],
    stroke_w=quantum_dusk["brane_stroke_w"],
    stroke_opa=1,
    fill_opa=quantum_dusk["brane_fill_opa"],
)

Plot_General.set_default(
    func_main_color=quantum_dusk["brane_color"],
    func_2_color=quantum_dusk["vacuum_color"],
    func_3_color=quantum_dusk["bh_color"],
    text_color=quantum_dusk["brane_text_color"],
    axis_opacity=0.5,
    axis_stroke=quantum_dusk["brane_stroke_w"],
    decorator_presence="box",
    decorator_color=quantum_dusk["arrow_color"],
    decorator_stroke_w=quantum_dusk["brane_stroke_w"],
    corner_rad=quantum_dusk["corner_rad"],
    corner_rad_direction=quantum_dusk["corner_rad_direction"],
    fill_opa=quantum_dusk["brane_fill_opa"],
    stroke_w=quantum_dusk["brane_stroke_w"],
    stroke_opa=1,
    tightness=0.3,
)
