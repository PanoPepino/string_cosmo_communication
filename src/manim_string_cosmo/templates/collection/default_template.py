from ...my_imports import *
from ...objects import *

# DEFAULT TEMPLATE (Black & White)
# Classic monochrome styling for presentations

default_template = {
    "bg_color": WHITE,  # White background
    "text_color": BLACK,  # Black text
    "brane_color": RED,  # Classic red for branes
    "brane_text_color": WHITE,  # White text on branes
    "brane_fill_opa": 0.1,  # Light fill
    "brane_stroke_w": 0.2,  # Thin stroke
    "vacuum_color": RED,  # Red vacuum
    "vacuum_fill_opa": 0.2,  # Light fill
    "vacuum_stroke_w": 0.2,  # Thin stroke
    "vacuum_text_color": WHITE,  # White text in vacuum
    "corner_rad": 0,  # Sharp corners
    "corner_rad_direction": [0, 0, 0, 0],  # No rounding
    "arrow_color": WHITE,  # White arrows
    "bh_color": BLACK,  # Black for black holes
    "bh_fill_opa": 0.8,  # Standard opacity
}

# Apply background
config.background_color = default_template["bg_color"]

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
    string_color=BLUE,
    field_top_color=BLUE,
)
