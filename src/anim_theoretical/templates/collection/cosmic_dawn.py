from ...my_imports import *
from ...objects import *

# COSMIC DAWN TEMPLATE
# Warm sunrise colors representing the dawn of the universe and early cosmological eras

cosmic_dawn = {
    "bg_color": "#FFF5E6",  # Soft cream background like early morning light
    "text_color": "#2C1810",  # Deep brown for text
    "brane_color": "#FF6B35",  # Warm orange-red for branes
    "brane_text_color": "#2C1810",  # Dark text on branes
    "brane_fill_opa": 0.15,  # Light transparency
    "brane_stroke_w": 2.5,  # Bold stroke for visibility
    "vacuum_color": "#7C3238",  # Deep red for vacuum
    "vacuum_fill_opa": 0.12,  # Subtle fill
    "vacuum_stroke_w": 1.2,  # Medium stroke
    "vacuum_text_color": "#2C1810",  # Dark text in vacuum
    "corner_rad": 0.15,  # Rounded corners
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#FF6B35",  # Orange arrows
    "bh_color": "#1A0B0B",  # Very dark for black holes
    "bh_fill_opa": 0.9,  # Nearly opaque
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
    string_color=cosmic_dawn["brane_color"],
    field_top_color=cosmic_dawn["arrow_color"],
)
