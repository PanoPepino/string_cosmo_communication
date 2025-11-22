from ...my_imports import *
from ...objects import *

# QUANTUM DUSK TEMPLATE
# Deep purples and blues representing quantum phenomena and twilight string landscapes

quantum_dusk = {
    "bg_color": "#E8E5F2",  # Light lavender background
    "text_color": "#1A1033",  # Deep purple-black for text
    "brane_color": "#6B4C9A",  # Royal purple for branes
    "brane_text_color": "#F0EDF5",  # Light text on branes
    "brane_fill_opa": 0.18,  # Moderate transparency
    "brane_stroke_w": 2.2,  # Medium-bold stroke
    "vacuum_color": "#2A1F5C",  # Deep space purple for vacuum
    "vacuum_fill_opa": 0.15,  # Ethereal fill
    "vacuum_stroke_w": 1.5,  # Medium stroke
    "vacuum_text_color": "#1A1033",  # Dark text in vacuum
    "corner_rad": 0.12,  # Slightly rounded corners
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#8B72C2",  # Medium purple arrows
    "bh_color": "#0A0415",  # Nearly black for black holes
    "bh_fill_opa": 0.95,  # Very opaque
}

# Apply background
config.background_color = quantum_dusk["bg_color"]

# Set defaults for string cosmology classes
Brane_General.set_default(
    brane_color=quantum_dusk["brane_color"],
    brane_fill_opa=quantum_dusk["brane_fill_opa"],
    brane_text_color=quantum_dusk["brane_text_color"],
    brane_stroke_w=quantum_dusk["brane_stroke_w"],
)

Vacuum_General.set_default(
    vacuum_color=quantum_dusk["vacuum_color"],
    vacuum_fill_opa=quantum_dusk["vacuum_fill_opa"],
    vacuum_stroke_w=quantum_dusk["vacuum_stroke_w"],
    vacuum_text_color=quantum_dusk["vacuum_text_color"],
    corner_rad=quantum_dusk["corner_rad"],
    corner_rad_direction=quantum_dusk["corner_rad_direction"],
)

AdS_Jc.set_default(
    arrow_color=quantum_dusk["arrow_color"]
)

Black_Hole.set_default(
    bh_color=quantum_dusk["bh_color"],
    bh_fill_opa=quantum_dusk["bh_fill_opa"],
)

Bubble.set_default(
    string_color=quantum_dusk["arrow_color"],
    field_top_color=quantum_dusk["brane_color"],
)
