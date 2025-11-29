from ...my_imports import *
from ...objects import *

# RED AUTUMN TEMPLATE
# Warm autumn palette with red and orange tones

red_autumn = {
    "bg_color": "#FAF9F5",  # Warm off-white background
    "brane_color": "#81331B",  # Deep rust red for branes
    "brane_text_color": WHITE,  # White text on branes
    "brane_fill_opa": 0.1,  # Light fill
    "brane_stroke_w": 1,  # Standard stroke
    "vacuum_color": "#B87390",  # Mauve-pink vacuum
    "vacuum_fill_opa": 0.1,  # Light fill
    "vacuum_stroke_w": 1,  # Standard stroke
    "vacuum_text_color": "#81331B",  # Rust text in vacuum
    "corner_rad": -0.05,  # Slightly inward corners
    "corner_rad_direction": [1, 0, 0, 0],  # Only upper-left corner
    "arrow_color": "#81331B",  # Rust arrows
    "bh_color": "#F49191",  # Light coral for black holes
    "bh_fill_opa": 0.1,  # Light opacity
    "string_color": "#FFC67C",  # Peachy orange for strings
    "field_top_color": "#81331B",  # Rust for field tops
}

# Apply background
config.background_color = red_autumn["bg_color"]

# Set defaults for string cosmology classes
Brane_General.set_default(
    brane_color=red_autumn["brane_color"],
    brane_fill_opa=red_autumn["brane_fill_opa"],
    brane_text_color=red_autumn["brane_text_color"],
    brane_stroke_w=red_autumn["brane_stroke_w"],
)

Vacuum_General.set_default(
    vacuum_color=red_autumn["vacuum_color"],
    vacuum_fill_opa=red_autumn["vacuum_fill_opa"],
    vacuum_stroke_w=red_autumn["vacuum_stroke_w"],
    vacuum_text_color=red_autumn["vacuum_text_color"],
    corner_rad=red_autumn["corner_rad"],
    corner_rad_direction=red_autumn["corner_rad_direction"],
)

AdS_Jc.set_default(
    arrow_color=red_autumn["arrow_color"]
)

Black_Hole.set_default(
    bh_color=red_autumn["bh_color"],
    bh_fill_opa=red_autumn["bh_fill_opa"],
)

Bubble.set_default(
    string_color=red_autumn["string_color"],
    field_top_color=red_autumn["field_top_color"],
)
