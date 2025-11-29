from ...my_imports import *
from ...objects import *

# BEAMER BLUE TEMPLATE
# Professional blue theme inspired by classic Beamer presentations

beamer_blue = {
    "bg_color": "#FFFFFF",  # White background
    "brane_color": "#003E7C",  # Deep blue for branes
    "brane_text_color": WHITE,  # White text on branes
    "brane_fill_opa": 0.9,  # High fill opacity
    "brane_stroke_w": 0.5,  # Thin stroke
    "vacuum_color": "#297ACB",  # Medium blue vacuum
    "vacuum_fill_opa": 0.9,  # High fill
    "vacuum_stroke_w": 0.5,  # Thin stroke
    "vacuum_text_color": WHITE,  # White text in vacuum
    "corner_rad": 0.1,  # Rounded corners
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#003E7C",  # Deep blue arrows
    "bh_color": "#A0CBFC",  # Light blue for black holes
    "bh_fill_opa": 0.9,  # High opacity
    "string_color": "#97DDF9",  # Lightest blue for strings
    "field_top_color": "#003E7C",  # Deep blue for field tops
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
    string_color=beamer_blue["string_color"],
    field_top_color=beamer_blue["field_top_color"],
)
