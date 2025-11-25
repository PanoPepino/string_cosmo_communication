from ...my_imports import *
from ...objects import *

# BEAMER BLUE TEMPLATE
# Professional blue theme inspired by classic Beamer presentations
# Clean white background with deep blue accents for scientific presentations

beamer_blue = {
    "bg_color": "#FFFFFF",  # Clean white background
    "text_color": BLACK,  # Black text for clarity
    "brane_color": "#003E7C",  # Deep blue for branes
    "brane_color_2": "#297ACB",  # Medium blue accent
    "brane_text_color": WHITE,  # White text on branes for contrast
    "brane_fill_opa": 0.9,  # Strong opacity for visibility
    "brane_stroke_w": 0.5,  # Thin stroke for clean look
    "vacuum_color": "#A0CBFC",  # Light blue for vacuum
    "vacuum_fill_opa": 0.9,  # Strong fill
    "vacuum_stroke_w": 0.5,  # Thin stroke
    "vacuum_text_color": BLACK,  # Dark text in light vacuum
    "corner_rad": 0.1,  # Slight rounding
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#003E7C",  # Deep blue arrows
    "bh_color": "#001A33",  # Very dark blue for black holes
    "bh_fill_opa": 0.9,  # Nearly opaque
    "bubble_string_color": "#97DDF9",  # Light cyan for strings
    "bubble_field_color": "#297ACB",  # Medium blue for fields
}

# Apply background
config.background_color = beamer_blue["bg_color"]

# Set defaults for string cosmology classes
Brane_General.set_default(
    brane_color=beamer_blue["brane_color"],
    brane_fill_opa=beamer_blue["brane_fill_opa"],
    brane_text_color=beamer_blue["brane_text_color"],
    brane_stroke_w=beamer_blue["brane_stroke_w"],
)

Vacuum_General.set_default(
    vacuum_color=beamer_blue["vacuum_color"],
    vacuum_fill_opa=beamer_blue["vacuum_fill_opa"],
    vacuum_stroke_w=beamer_blue["vacuum_stroke_w"],
    vacuum_text_color=beamer_blue["vacuum_text_color"],
    corner_rad=beamer_blue["corner_rad"],
    corner_rad_direction=beamer_blue["corner_rad_direction"],
)

AdS_Jc.set_default(
    arrow_color=beamer_blue["arrow_color"]
)

Black_Hole.set_default(
    bh_color=beamer_blue["bh_color"],
    bh_fill_opa=beamer_blue["bh_fill_opa"],
)

Bubble.set_default(
    string_color=beamer_blue["bubble_string_color"],
    field_top_color=beamer_blue["bubble_field_color"],
)
