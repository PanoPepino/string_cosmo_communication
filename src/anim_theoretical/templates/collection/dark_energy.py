from ...my_imports import *
from ...objects import *

# DARK ENERGY TEMPLATE
# Dark space theme with vibrant cyan energy accents

dark_energy = {
    "bg_color": "#0D1B2A",  # Deep space blue-black background
    "brane_color": "#00D9FF",  # Bright cyan for branes
    "brane_text_color": "#0D1B2A",  # Dark text on branes
    "brane_fill_opa": 0.05,  # Light fill
    "brane_stroke_w": 1,  # Medium stroke
    "vacuum_color": "#00FFC6",  # Bright teal vacuum
    "vacuum_fill_opa": 0.05,  # Light fill
    "vacuum_stroke_w": 1,  # Medium stroke
    "vacuum_text_color": "#E0E1DD",  # Light gray text in vacuum
    "corner_rad": 0.05,  # Slightly rounded corners
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#00D9FF",  # Bright cyan arrows
    "bh_color": "#1B263B",  # Space blue for black holes
    "bh_fill_opa": 0.05,  # Light opacity
    "string_color": "#E0E1DD",  # Light gray for strings
    "field_top_color": "#00D9FF",  # Bright cyan for field tops
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
    string_color=dark_energy["string_color"],
    field_top_color=dark_energy["field_top_color"],
)
