from ...my_imports import *
from ...objects import *

# BLUE ICE TEMPLATE
# Cool cyan-blue palette with icy tones

blue_ice = {
    "bg_color": "#F1F8FF",  # Light icy blue background
    "brane_color": "#003E7C",  # Deep blue for branes
    "brane_text_color": WHITE,  # White text on branes
    "brane_fill_opa": 0.05,  # Very light fill
    "brane_stroke_w": 1,  # Medium stroke
    "vacuum_color": "#7973B8",  # Purple-blue vacuum
    "vacuum_fill_opa": 0.05,  # Very light fill
    "vacuum_stroke_w": 1,  # Medium stroke
    "vacuum_text_color": "#003E7C",  # Deep blue text in vacuum
    "corner_rad": 0.05,  # Slightly rounded corners
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#003E7C",  # Deep blue arrows
    "bh_color": "#A0BCFC",  # Light blue for black holes
    "bh_fill_opa": 0.05,  # Very light opacity
    "string_color": "#7CDAFF",  # Bright cyan for strings
    "field_top_color": "#003E7C",  # Deep blue for field tops
}

# Apply background
config.background_color = blue_ice["bg_color"]

# Set defaults for string cosmology classes
Brane_General.set_default(
    brane_color=blue_ice["brane_color"],
    brane_fill_opa=blue_ice["brane_fill_opa"],
    brane_text_color=blue_ice["brane_text_color"],
    brane_stroke_w=blue_ice["brane_stroke_w"],
)

Vacuum_General.set_default(
    vacuum_color=blue_ice["vacuum_color"],
    vacuum_fill_opa=blue_ice["vacuum_fill_opa"],
    vacuum_stroke_w=blue_ice["vacuum_stroke_w"],
    vacuum_text_color=blue_ice["vacuum_text_color"],
    corner_rad=blue_ice["corner_rad"],
    corner_rad_direction=blue_ice["corner_rad_direction"],
)

AdS_Jc.set_default(
    arrow_color=blue_ice["arrow_color"]
)

Black_Hole.set_default(
    bh_color=blue_ice["bh_color"],
    bh_fill_opa=blue_ice["bh_fill_opa"],
)

Bubble.set_default(
    string_color=blue_ice["string_color"],
    field_top_color=blue_ice["field_top_color"],
)
