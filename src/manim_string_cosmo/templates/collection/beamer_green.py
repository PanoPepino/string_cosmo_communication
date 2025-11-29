from ...my_imports import *
from ...objects import *

# BEAMER GREEN TEMPLATE
# Professional green theme inspired by classic Beamer presentations

beamer_green = {
    "bg_color": "#FFFFFF",  # White background
    "brane_color": "#096E30",  # Deep green for branes
    "brane_text_color": WHITE,  # White text on branes
    "brane_fill_opa": 0.4,  # High fill opacity
    "brane_stroke_w": 0.5,  # Thin stroke
    "vacuum_color": "#09AC7B",  # Medium green vacuum
    "vacuum_fill_opa": 0.5,  # High fill
    "vacuum_stroke_w": 0.5,  # Thin stroke
    "vacuum_text_color": WHITE,  # White text in vacuum
    "corner_rad": 0.1,  # Rounded corners
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#096E30",  # Deep green arrows
    "bh_color": "#0AD46C",  # Light green for black holes
    "bh_fill_opa": 0.9,  # High opacity
    "string_color": "#C6FF7C",  # Lightest green for strings
    "field_top_color": "#096E30",  # Deep green for field tops
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
    string_color=beamer_green["string_color"],
    field_top_color=beamer_green["field_top_color"],
)
