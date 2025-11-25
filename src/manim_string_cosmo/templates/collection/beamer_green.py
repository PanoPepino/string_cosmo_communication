from ...my_imports import *
from ...objects import *

# BEAMER GREEN TEMPLATE
# Professional green theme inspired by classic Beamer presentations
# Clean white background with deep green accents for scientific presentations

beamer_green = {
    "bg_color": "#FFFFFF",  # Clean white background
    "text_color": "#0B5B30",  # Deep green text
    "brane_color": "#096E30",  # Deep green for branes
    "brane_color_2": "#09AC7B",  # Medium green accent
    "brane_text_color": WHITE,  # White text on branes for contrast
    "brane_fill_opa": 0.9,  # Strong opacity for visibility
    "brane_stroke_w": 0.5,  # Thin stroke for clean look
    "vacuum_color": "#0AD46C",  # Vibrant green for vacuum
    "vacuum_fill_opa": 0.9,  # Strong fill
    "vacuum_stroke_w": 0.5,  # Thin stroke
    "vacuum_text_color": BLACK,  # Dark text for contrast
    "corner_rad": 0.1,  # Slight rounding
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#096E30",  # Deep green arrows
    "bh_color": "#042815",  # Very dark green for black holes
    "bh_fill_opa": 0.9,  # Nearly opaque
    "bubble_string_color": "#C6FF7C",  # Light yellow-green for strings
    "bubble_field_color": "#09AC7B",  # Medium green for fields
}

# Apply background
config.background_color = beamer_green["bg_color"]

# Set defaults for string cosmology classes
Brane_General.set_default(
    brane_color=beamer_green["brane_color"],
    brane_fill_opa=beamer_green["brane_fill_opa"],
    brane_text_color=beamer_green["brane_text_color"],
    brane_stroke_w=beamer_green["brane_stroke_w"],
)

Vacuum_General.set_default(
    vacuum_color=beamer_green["vacuum_color"],
    vacuum_fill_opa=beamer_green["vacuum_fill_opa"],
    vacuum_stroke_w=beamer_green["vacuum_stroke_w"],
    vacuum_text_color=beamer_green["vacuum_text_color"],
    corner_rad=beamer_green["corner_rad"],
    corner_rad_direction=beamer_green["corner_rad_direction"],
)

AdS_Jc.set_default(
    arrow_color=beamer_green["arrow_color"]
)

Black_Hole.set_default(
    bh_color=beamer_green["bh_color"],
    bh_fill_opa=beamer_green["bh_fill_opa"],
)

Bubble.set_default(
    string_color=beamer_green["bubble_string_color"],
    field_top_color=beamer_green["bubble_field_color"],
)
