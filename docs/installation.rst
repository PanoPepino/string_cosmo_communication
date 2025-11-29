Installation
============

Prerequisites
-------------

Before installing String Cosmology Communication, make sure you have:

- Python 3.8 or higher
- Manim Community Edition installed
- Git (for cloning the repository)

Installing Manim
----------------

If you don't have Manim installed yet, follow the official installation guide:

`Manim Community Installation Guide <https://docs.manim.community/en/stable/installation.html>`_


Installing String Cosmology Communication
------------------------------------------

To install the String Cosmology Communication library:

1. Clone the repository:

.. code-block:: bash

   git clone https://github.com/PanoPepino/string_cosmo_communication

2. Install the package:

.. code-block:: bash

   pip install string_cosmo_communication/ .


Usage
-----

To use the library in your Manim scripts:

.. code-block:: python

   from manim import *
   from manim_string_cosmo import *

   # Import a template (optional but recommended)
   import_template('cosmic_dawn')

   class MyStringScene(Scene):
       def construct(self):
           bubble = Bubble(bubble_type="empty")
           brane = Brane_General()
           self.add(bubble, brane)


Verifying Installation
----------------------

To verify that the installation was successful, try running a simple test:

.. code-block:: python

   from manim_string_cosmo import *
   print("String Cosmology Communication installed successfully!")

If no errors appear, you're ready to start creating string cosmology animations!


Troubleshooting
---------------

If you encounter any issues during installation:

1. Make sure all prerequisites are installed
2. Check that you're using a compatible Python version
3. Try updating pip: ``pip install --upgrade pip``
4. Report persistent issues on `GitHub Issues <https://github.com/PanoPepino/string_cosmo_communication/issues>`_
