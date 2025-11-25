import importlib

from ..my_imports import *

__all__ = ["import_string_cosmo_template"]


def import_string_cosmo_template(module_name: str):
    """
    Import a chosen template to standardize styling for string cosmology visualizations.

    This function loads a predefined color and styling template that will be applied
    to all subsequent string_cosmo objects created in the scene. It helps maintain visual
    consistency across string theory and cosmology animations.

    :param module_name: Name of the template to import. Must be one of the allowed templates.
    :type module_name: str

    :raises ModuleNotFoundError: If the specified template module cannot be found.

    .. note::

       This function should be called before defining your Scene class to ensure
       the template is properly loaded before any string_cosmo objects are created.

    **Available templates:**
        - ``"cosmic_dawn"``
        - ``"quantum_dusk"``
        - ``"dark_energy"``
        - ``"green_mint"``
        - ``"blue_ice"``
        - ``"red_autumn"``
        - ``"beamer_blue"``
        - ``"beamer_green"``
        - ``"default_template"`` (fallback)

    **Example usage:**

    .. code-block:: python

        from manim_string_cosmo import *

        import_string_cosmo_template('cosmic_dawn')

        class MyScene(Scene):
            def construct(self):
                # Your string_cosmo objects will now use the selected template
                pass
    """
    allowed_modules = [
        "cosmic_dawn",
        "quantum_dusk",
        "dark_energy",
        "green_mint",
        "blue_ice",
        "red_autumn",
        "beamer_blue",
        "beamer_green"
    ]

    # Import base template
    if module_name in allowed_modules:
        module_path = f"manim_string_cosmo.templates.collection.{module_name}"
        print(f"Using '{module_name}' template for string cosmology!")
    else:
        print(f"Template '{module_name}' does not exist. Using default template instead!")
        module_path = "manim_string_cosmo.templates.collection.default_template"

    importlib.import_module(module_path)
