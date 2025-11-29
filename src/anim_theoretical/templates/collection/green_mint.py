from ...my_imports import *
from ...objects import *

# GREEN MINT TEMPLATE
# Fresh minty green palette with light background

green_mint = {
    "bg_color": "#F0FFF4",  # Very light mint background
    "brane_color": "#22543D",  # Deep green for branes
    "brane_text_color": WHITE,  # White text on branes
    "brane_fill_opa": 0.08,  # Light fill
    "brane_stroke_w": 1,  # Medium stroke
    "vacuum_color": "#38A169",  # Medium green vacuum
    "vacuum_fill_opa": 0.08,  # Light fill
    "vacuum_stroke_w": 1,  # Medium stroke
    "vacuum_text_color": "#22543D",  # Deep green text in vacuum
    "corner_rad": 0.07,  # Rounded corners
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#22543D",  # Deep green arrows
    "bh_color": "#9AE6B4",  # Light green for black holes
    "bh_fill_opa": 0.08,  # Light opacity
    "string_color": "#C6F6D5",  # Lightest green for strings
    "field_top_color": "#22543D",  # Deep green for field tops
}

# Apply background
config.background_color = green_mint["bg_color"]

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
