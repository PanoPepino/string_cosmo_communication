from ...my_imports import *
from ...objects import *

# QUANTUM DUSK TEMPLATE
# Dusky purple theme with warm accent colors

quantum_dusk = {
    "bg_color": "#2D3748",  # Dark slate background
    "brane_color": "#9F7AEA",  # Purple for branes
    "brane_text_color": "#2D3748",  # Dark text on branes
    "brane_fill_opa": 0.18,  # Light fill
    "brane_stroke_w": 1.3,  # Medium stroke
    "vacuum_color": "#FC8181",  # Coral pink vacuum
    "vacuum_fill_opa": 0.18,  # Light fill
    "vacuum_stroke_w": 1.3,  # Medium stroke
    "vacuum_text_color": "#2D3748",  # Dark text in vacuum
    "corner_rad": 0.09,  # Rounded corners
    "corner_rad_direction": [1, 1, 1, 1],  # All corners rounded
    "arrow_color": "#9F7AEA",  # Purple arrows
    "bh_color": "#F6AD55",  # Orange for black holes
    "bh_fill_opa": 0.18,  # Light opacity
    "string_color": "#68D391",  # Green for strings
    "field_top_color": "#9F7AEA",  # Purple for field tops
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
    string_color=quantum_dusk["string_color"],
    field_top_color=quantum_dusk["field_top_color"],
)
