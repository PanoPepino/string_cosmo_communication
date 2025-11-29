from ...my_imports import *
from ...objects import *

# COSMIC DAWN TEMPLATE
# Vibrant energy-themed palette with dark cosmic background

cosmic_dawn = {
    "bg_color": "#1A1A2E",  # Deep cosmic background
    "brane_color": "#FF6B6B",  # Bright coral for branes
    "brane_text_color": "#1A1A2E",  # Dark text on branes
    "brane_fill_opa": 0.15,  # Light fill
    "brane_stroke_w": 1.5,  # Medium-thick stroke
    "vacuum_color": "#FFD93D",  # Golden yellow vacuum
    "vacuum_fill_opa": 0.15,  # Light fill
    "vacuum_stroke_w": 1.5,  # Medium-thick stroke
    "vacuum_text_color": "#1A1A2E",  # Dark text in vacuum
    "corner_rad": 0.08,  # Rounded corners
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#FF6B6B",  # Coral arrows
    "bh_color": "#6BCB77",  # Bright green for black holes
    "bh_fill_opa": 0.15,  # Light opacity
    "string_color": "#4D96FF",  # Bright blue for strings
    "field_top_color": "#FF6B6B",  # Coral for field tops
}

# Apply background
config.background_color = cosmic_dawn["bg_color"]

# Set defaults for string cosmology classes
Brane_General.set_default(
    brane_color=cosmic_dawn["brane_color"],
    brane_fill_opa=cosmic_dawn["brane_fill_opa"],
    brane_text_color=cosmic_dawn["brane_text_color"],
    brane_stroke_w=cosmic_dawn["brane_stroke_w"],
)

Vacuum_General.set_default(
    vacuum_color=cosmic_dawn["vacuum_color"],
    vacuum_fill_opa=cosmic_dawn["vacuum_fill_opa"],
    vacuum_stroke_w=cosmic_dawn["vacuum_stroke_w"],
    vacuum_text_color=cosmic_dawn["vacuum_text_color"],
    corner_rad=cosmic_dawn["corner_rad"],
    corner_rad_direction=cosmic_dawn["corner_rad_direction"],
)

AdS_Jc.set_default(
    arrow_color=cosmic_dawn["arrow_color"]
)

Black_Hole.set_default(
    bh_color=cosmic_dawn["bh_color"],
    bh_fill_opa=cosmic_dawn["bh_fill_opa"],
)

Bubble.set_default(
    string_color=cosmic_dawn["string_color"],
    field_top_color=cosmic_dawn["field_top_color"],
)
