import importlib
import sys

try:
    from template_registry import ACTIVE_TEMPLATE
except ImportError:
    ACTIVE_TEMPLATE = None

__all__ = ["import_template"]

def import_template(module_name: str):
    """
    Import a chosen template, synced globally with beanim if used together.
    """
    global ACTIVE_TEMPLATE
    already_set = False
    # Detect external setting via registry (set by beanim or another import)
    if 'template_registry' in sys.modules:
        registry = sys.modules['template_registry']
        if hasattr(registry, 'ACTIVE_TEMPLATE') and registry.ACTIVE_TEMPLATE:
            module_name = registry.ACTIVE_TEMPLATE
            already_set = True
        else:
            registry.ACTIVE_TEMPLATE = module_name
    else:
        ACTIVE_TEMPLATE = module_name
    allowed_modules = [
        "cosmic_dawn", 
        "quantum_dusk", 
        "dark_energy",
        "green_mint",
        "blue_ice",
        "red_autumn",
        "beamer_blue",
        "beamer_green",
        "default_template"
    ]
    if module_name in allowed_modules:
        module_path = f"anim_theoretical.templates.collection.{module_name}"
        print(f"Using '{module_name}' template for string cosmology visualizations!")
    else:
        print(f"Template '{module_name}' does not exist. Using default template instead.")
        module_path = "anim_theoretical.templates.collection.default_template"
    importlib.import_module(module_path)
    if not already_set:
        import importlib.util
        spec = importlib.util.find_spec("template_registry")
        if spec is not None:
            module = importlib.util.module_from_spec(spec)
            module.ACTIVE_TEMPLATE = module_name
