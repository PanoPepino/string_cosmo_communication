<div align="center">

# String Cosmology Communication

**A Manim library for visualizing string theory and braneworld cosmology**

<a href="https://www.buymeacoffee.com/panopepino" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="35" />
</a>

[Documentation](https://panopepino.github.io/string_cosmo_communication/) • [Examples](#examples) • [Installation](#installation)

</div>


## 📚 About String Cosmology Communication

This repository contains **String Cosmology Communication** (formerly mtheoretical), a Manim library designed for creating animations and visualizations of string theory and braneworld cosmology concepts.

The package provides skecthed objects and templates to help researchers communicate complex string theoretical physics ideas.

> **⚠️ Important Note**  
> The package is imported as **manim_string_cosmo_communication** in your Python files. However, documentation and the repository use the name **string_cosmo_communication** for clarity.



## ✨ Key Features

### String Cosmology Objects

- **🌌 Branes**: Domain walls, D-branes, and brane configurations
- **🌠 Vacuum States**: Different vacuum configurations and transitions
- **💥 Bubble Universes**: Nucleation and bubble evolution
- **⚫ Black Holes**: Higher-dimensional black holes
- **🔴 AdS Spaces**: Anti-de Sitter spaces and junction conditions

### Template System

- **9 Professional Templates**: Optimized for scientific presentations
- **Easy Switching**: Change entire color scheme with one command
- **Consistent Styling**: All objects automatically adapt to template
- **Light & Dark Themes**: Choose backgrounds that work for your presentation

Available templates:
- `cosmic_dawn` - Warm sunrise colors for early universe
- `quantum_dusk` - Deep purples for quantum effects
- `dark_energy` - Dark cosmic themes
- `green_mint`, `blue_ice`, `red_autumn` - Classic color palettes
- `beamer_blue`, `beamer_green` - Professional presentation themes
- `default_template` - Black and white fallback



## Examples

### Basic Usage

```python
from manim import *
from anim_theoretical import *

# Import a template for consistent styling
import_template('cosmic_dawn')

class StringCosmologyScene(Scene):
    def construct(self):
        # Create a bubble universe
        bubble = Bubble(bubble_type="empty")
        
        # Create a brane
        brane = Brane_General()
        
        # Animate
        self.play(Create(bubble))
        self.play(FadeIn(brane))
        self.wait()
```

### Template Comparison

<div align="center">
  <sub><i>Template comparison images will be added soon</i></sub>
</div>




### Install String Cosmology Communication

### Prerequisites

Make sure you have:
- Python 3.8 or higher
- [Manim Community Edition](https://docs.manim.community/en/stable/installation.html)
- Git

To **install** this library:

```bash
git clone https://github.com/PanoPepino/string_cosmo_communication

pip install string_cosmo_communication/ .
```

To **use** in your Manim files:

```python
from manim import *
from manim_string_cosmo import *
```

For detailed usage instructions and API reference, visit the [📚 documentation](https://panopepino.github.io/string_cosmo_communication/).


## Template System

Quickly change the entire look of your animations:

```python
# At the beginning of your script
import_template('beamer_blue')  # Professional blue theme

# All subsequent objects will use this template
class MyScene(Scene):
    def construct(self):
        bubble = Bubble()      # Automatically styled
        brane = Brane_General()  # Automatically styled
        # ...
```

See the [Template Guide](https://panopepino.github.io/string_cosmo_communication/) for detailed information on all available templates.


## Contributing

Contributions are welcome! Whether you:

- Have ideas for new cosmological objects
- Want to add color templates
- Found bugs or have suggestions
- Want to improve documentation

Please open an issue or submit a pull request on [GitHub](https://github.com/PanoPepino/string_cosmo_communication/issues).


## 💖 Support My Work

If you find this project helpful, consider supporting its development. Thank you!

<p align="center">
  <a href="https://www.buymeacoffee.com/panopepino" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="50" />
  </a>
</p>


<!--

TO DO:

- Return for beanim and string_cosmo the import function to normal state. Change name so that import_beanim import_string_cosmo are for each them. 
- Double check that templates created for beanim and string_cosmo make sense in colouring and stuff.

>

<!--
Log of changes:

- 2025/11/25: Removed. Quite complicated.
- 2025/11/25: Changed color template stuff so that it can inherit template from beanim if used with that package.

>