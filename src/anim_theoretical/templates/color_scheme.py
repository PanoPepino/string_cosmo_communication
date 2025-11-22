import importlib

from ..my_imports import *

__all__ = ["import_template"]


def import_template(module_name: str):
    """
    Import a chosen template to standardize styling across all string cosmology objects.

    This function loads a predefined color and styling template that will be applied
    to all subsequent string cosmology visualization objects created in the scene.
    It helps maintain visual consistency across presentations and animations.

    :param module_name: Name of the template to import. Must be one of the allowed templates.
    :type module_name: str

    :raises ModuleNotFoundError: If the specified template module cannot be found.

    .. note::

       This function should be called at the beginning of your script before defining
       your Scene class to ensure the template is properly loaded before any objects
       are created.

    **Available templates:**
        - ``"cosmic_dawn"`` - Warm sunrise colors for cosmological scenarios
        - ``"quantum_dusk"`` - Deep purples and blues for quantum/string effects
        - ``"dark_energy"`` - Dark backgrounds with energy-themed accents
        - ``"default_template"`` (fallback) - Black and white default styling

    **Example usage:**

    .. code-block:: python

        from manim import *
        from anim_theoretical import *

        import_template('cosmic_dawn')

        class MyCosmologyScene(Scene):
            def construct(self):
                # Your string cosmology objects will now use the selected template
                bubble = Bubble(bubble_type="empty")
                self.add(bubble)
    """
    allowed_modules = ["cosmic_dawn", "quantum_dusk", "dark_energy"]

    # Import template
    if module_name in allowed_modules:
        module_path = f"anim_theoretical.templates.collection.{module_name}"
        print(f"Using '{module_name}' template for string cosmology visualizations!")
    else:
        print(f"Template '{module_name}' does not exist. Using default template instead.")
        module_path = "anim_theoretical.templates.collection.default_template"

    importlib.import_module(module_path)
