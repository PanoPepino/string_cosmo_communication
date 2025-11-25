from ...my_imports import *
from ...objects import *

# DARK ENERGY TEMPLATE
# Dark backgrounds with vibrant energy-themed accents for modern cosmology presentations

dark_energy = {
    "bg_color": "#0D1B2A",  # Deep space blue-black background
    "text_color": "#E0E1DD",  # Light gray for text
    "brane_color": "#00D9FF",  # Bright cyan for branes (energy signature)
    "brane_text_color": "#0D1B2A",  # Dark text on bright branes
    "brane_fill_opa": 0.2,  # Glowing effect
    "brane_stroke_w": 2.8,  # Bold stroke for visibility on dark background
    "vacuum_color": "#1B263B",  # Slightly lighter space blue for vacuum
    "vacuum_fill_opa": 0.25,  # More visible on dark background
    "vacuum_stroke_w": 1.8,  # Thicker stroke for visibility
    "vacuum_text_color": "#E0E1DD",  # Light text in vacuum
    "corner_rad": 0.18,  # More rounded for modern look
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#00FFC6",  # Bright teal arrows
    "bh_color": "#000000",  # Pure black for black holes
    "bh_fill_opa": 1.0,  # Completely opaque
}

# Apply background
config.background_color = dark_energy["bg_color"]

# Set defaults for string cosmology classes
Brane_General.set_default(
    brane_color=dark_energy["brane_color"],
    brane_fill_opa=dark_energy["brane_fill_opa"],
    brane_text_color=dark_energy["brane_text_color"],
    brane_stroke_w=dark_energy["brane_stroke_w"],
)

Vacuum_General.set_default(
    vacuum_color=dark_energy["vacuum_color"],
    vacuum_fill_opa=dark_energy["vacuum_fill_opa"],
    vacuum_stroke_w=dark_energy["vacuum_stroke_w"],
    vacuum_text_color=dark_energy["vacuum_text_color"],
    corner_rad=dark_energy["corner_rad"],
    corner_rad_direction=dark_energy["corner_rad_direction"],
)

AdS_Jc.set_default(
    arrow_color=dark_energy["arrow_color"]
)

Black_Hole.set_default(
    bh_color=dark_energy["bh_color"],
    bh_fill_opa=dark_energy["bh_fill_opa"],
)

Bubble.set_default(
    string_color=dark_energy["arrow_color"],
    field_top_color=dark_energy["brane_color"],
)
