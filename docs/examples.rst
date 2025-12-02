Quick Guide
===========

This guide will walk you through the basics of **String Cosmo Communication**. Like `Beanim <https://github.com/PanoPepino/beanim>`_, the package for creating Beamer-like slides, we'll start with the available templates and colors, then build a presentation showcasing string theory and cosmology concepts.

----

Available Templates
-------------------

String Cosmo comes equipped with nine different templates to homogenize the look of your slides:

* 🌅 **cosmic_dawn** - Warm sunrise colors for early universe scenarios
* 🌌 **quantum_dusk** - Elegant purple-lavender theme for quantum effects
* ⚫ **dark_energy** - Dark theme with bright cyan accents
* 🌿 **green_mint** - Fresh mint green theme
* 🧊 **blue_ice** - Cool blue color scheme
* 🍂 **red_autumn** - Warm autumn colors
* 🔵 **beamer_blue** - Classic Beamer style in blue
* 🟢 **beamer_green** - Classic Beamer style in green
* 🎨 **default_template** - Clean black and white design

Template Gallery
^^^^^^^^^^^^^^^^

.. raw:: html

   <div style="margin: 20px 0;">

     <!-- quantum_dusk -->
     <div style="margin-bottom: 40px;">
       <h3 style="color: white; padding: 5px; text-align: center; margin-bottom: 15px; border-radius: 5px;">🌌 quantum_dusk</h3>
       <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_1_quantum_dusk.png" alt="quantum_dusk slide 1" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_2_quantum_dusk.png" alt="quantum_dusk slide 2" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
       </div>
     </div>

     <!-- dark_energy -->
     <div style="margin-bottom: 40px;">
       <h3 style="color: white; padding: 5px; text-align: center; margin-bottom: 15px; border-radius: 5px;">⚫ dark_energy</h3>
       <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_1_dark_energy.png" alt="dark_energy slide 1" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_2_dark_energy.png" alt="dark_energy slide 2" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
       </div>
     </div>

     <!-- green_mint -->
     <div style="margin-bottom: 40px;">
       <h3 style="color: white; padding: 5px; text-align: center; margin-bottom: 15px; border-radius: 5px;">🌿 green_mint</h3>
       <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_1_green_mint.png" alt="green_mint slide 1" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_2_green_mint.png" alt="green_mint slide 2" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
       </div>
     </div>

     <!-- blue_ice -->
     <div style="margin-bottom: 40px;">
       <h3 style="color: white; padding: 5px; text-align: center; margin-bottom: 15px; border-radius: 5px;">🧊 blue_ice</h3>
       <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_1_blue_ice.png" alt="blue_ice slide 1" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_2_blue_ice.png" alt="blue_ice slide 2" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
       </div>
     </div>

     <!-- red_autumn -->
     <div style="margin-bottom: 40px;">
       <h3 style="color: white; padding: 5px; text-align: center; margin-bottom: 15px; border-radius: 5px;">🍂 red_autumn</h3>
       <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_1_red_autumn.png" alt="red_autumn slide 1" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_2_red_autumn.png" alt="red_autumn slide 2" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
       </div>
     </div>

     <!-- beamer_blue -->
     <div style="margin-bottom: 40px;">
       <h3 style="color: white; padding: 5px; text-align: center; margin-bottom: 15px; border-radius: 5px;">🔵 beamer_blue</h3>
       <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_1_beamer_blue.png" alt="beamer_blue slide 1" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_2_beamer_blue.png" alt="beamer_blue slide 2" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
       </div>
     </div>

     <!-- beamer_green -->
     <div style="margin-bottom: 40px;">
       <h3 style="color: white; padding: 5px; text-align: center; margin-bottom: 15px; border-radius: 5px;">🟢 beamer_green</h3>
       <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_1_beamer_green.png" alt="beamer_green slide 1" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_2_beamer_green.png" alt="beamer_green slide 2" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
       </div>
     </div>

     <!-- default_template -->
     <div style="margin-bottom: 40px;">
       <h3 style="color: white; padding: 5px; text-align: center; margin-bottom: 15px; border-radius: 5px;">🎨 default_template</h3>
       <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_1_default_template.png" alt="default_template slide 1" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
         <div style="text-align: center;">
           <p style="font-weight: bold; margin-bottom: 8px;"></p>
           <img src="_static/media/images/Generic_Slide_2_default_template.png" alt="default_template slide 2" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"/>
         </div>
       </div>
     </div>

   </div>

----

Step 1: Import and Setup
-------------------------

These templates can be called by importing them at the preamble of your ``file.py`` to work with Manim:

.. code-block:: python

    from manim import *
    from manim_string_cosmo import * 
    
    # Choose your template
    import_template_string_cosmo('cosmic_dawn')

    class String_Cosmology_Presentation(Scene):
        def construct(self):
            # Your presentation code here
            pass

----

Step 2: Define Your Objects
-----------------------------------------

Before building the animation script, define all the objects you'll use. String Cosmo provides specialized objects for visualizing string theory and braneworld scenarios. For example.

* **Bubble()** - Vacuum bubble universes with various content types:
  
  - ``bubble_type="empty"`` - Empty bubble
  - ``bubble_type="radiation"`` - Radiation-filled bubble
  - ``bubble_type="em"`` - Electromagnetic field content
  - ``bubble_type="strings"`` - String attaching to the brane
  - ``bubble_type="GW"`` - Gravitational waves

* **Black_Hole()** - Higher-dimensional black holes:
  
  - ``bh_type="spinning"`` - Rotating 5D black hole from 10D background
  - ``bh_type="fragmentation"`` - AdS Fragmentation


* **AdS_Jc()** - Anti-de Sitter junction configurations:
  
  - ``vacua_type="DB"`` - Dark Bubble configuration
  - ``vacua_type="RS"`` - Randall-Sundrum configuration


* **More objects** - To find in the `Documentation <https://github.com/PanoPepino/string_cosmo_communication>`


.. note::
   You can define all objects in a separate ``objects.py`` file and import them into your main script for better organization.

----

Step 3: Build Your String Cosmology Presentation
-------------------------------------------------

Here's a complete example showing how to create a presentation about bubble nucleation and braneworld scenarios:

.. code-block:: python

    from manim import *
    from manim_string_cosmo import *
    from manim_slides import *

    import_template_string_cosmo('dark_energy')


    class Bubble_Cosmology_Presentation(Slide):
        def construct(self):

            # ============================================
            # Object Definition
            # ============================================

            bubble_empty = Bubble(bubble_type="em")
            bubble_radiation = Bubble(bubble_type="radiation")
            bubble_strings = Bubble(bubble_type="strings")

            bubbles = VGroup(bubble_empty, bubble_radiation, bubble_strings)\
            .arrange(RIGHT, buff=1).scale_to_fit_width(config.frame_width-1)

            bh_spinning = Black_Hole(bh_type="spinning")
            bh_fragment = Black_Hole(bh_type="fragmentation")

            black_holes = VGroup(bh_spinning, bh_fragment).arrange(RIGHT, buff=10).scale_to_fit_width(config.frame_width-5)

            ads_db = AdS_Jc(vacua_type="DB")
            ads_rs = AdS_Jc(vacua_type="RS")

            ads_configs = VGroup(ads_db, ads_rs)\
            .arrange(RIGHT, aligned_edge=DOWN, buff=1)\
            .scale_to_fit_width(config.   frame_width-1)

            # ============================================
            # SLIDE 1: BUBBLE ANIMATION
            # ============================================

            self.play(AnimationGroup(
                *[bubble.fade_in_bulk() for bubble in bubbles]
            ))
            self.next_slide(loop=True)
            self.play(AnimationGroup(
                *[bubble.create_bubble() for bubble in bubbles]
            ))
            self.wait()
            self.next_slide(loop=True)
            self.play(AnimationGroup(
                *[bubble.expand_bubble() for bubble in bubbles]
            ))
            self.wait()

            # ============================================
            # SLIDE 2: BLACK HOLE ANIMATION
            # ============================================

            self.next_slide(auto_next=True)
            self.play(FadeOut(bubbles))
            self.wait()
            self.play(FadeIn(black_holes))
            self.wait()

            self.next_slide(loop=True)
            self.play(AnimationGroup(
                *[bh.nucleate() for bh in black_holes]
            ))
            self.wait()
            self.next_slide(loop=True)
            self.play(AnimationGroup(
                *[bh.expand() for bh in black_holes]
            ))

            # ============================================
            # SLIDE 3: AdS JUNCTION CONFIGURATIONS
            # ============================================

            self.next_slide(auto_next=True)
            self.play(FadeOut(black_holes))
            self.wait()
            self.play(AnimationGroup(
                *[config.fade_in() for config in ads_configs]
            ))

            self.next_slide(loop=True)
            self.play(ads_rs.show_symmetry(rt=3))
            self.wait()
            self.play(ads_rs.restore_symmetry())
            self.wait()

            self.next_slide(loop=True)
            self.play(AnimationGroup(
                *[config.fade_in_arrow() for config in ads_configs]
            ))
            self.wait()
            self.play(AnimationGroup(
                ads_db.show_n_vector_db(rt=3),
                ads_rs.show_n_vector_rs(rt=3)
            ))
            self.wait()

            self.next_slide()
            self.play(FadeOut(ads_configs))



Step 4: Render Your Animation
------------------------------

Render the animation using the standard ``manim`` command:

.. code-block:: bash

    manim -pql file_name.py Bubble_Cosmology_Presentation

Options:

* ``-p`` - Play the video after rendering
* ``-ql`` - Quality low (faster rendering for testing)
* ``-qh`` - Quality high (for final presentations)

For presentations with manim-slides integration, you will need to add ``self.next_slide()`` stops and render as discussed in `Manim Slides documentation <https://manim-slides.eertmans.be/latest/>`_

.. code-block:: bash

    manim-slides render file_name.py Bubble_Cosmology_Presentation
    manim-slides present Bubble_Cosmology_Presentation


The final result should look like:

.. raw:: html

    <div style="position:relative;padding-bottom:56.25%;">
        <iframe
            loading="lazy"
            style="width:100%;height:100%;position:absolute;left:0px;top:0px; border: 2px solid #000000ff; border-radius: 8px;"
            frameborder="0"
            width="100%"
            height="100%"
            allowfullscreen
            allow="autoplay"
            src="https://panopepino.github.io/web_page/main_page/presentations/2025_12_string_cosmo/BCP.html">
        </iframe>
    </div>




Next Steps
----------

Now that you've created your first string cosmology animation, explore more advanced features:

* 🔧 Learn about all object types and their parameters in the :doc:`api/modules` section
* 🎨 Experiment with different templates to match your presentation style
* 💡 Create your own sketches and animations to improve this package!

.. tip::
   **Pro tip:** Start with simple single-object animations to understand the physics, then build up to complex multi-object scenarios. The template system ensures visual consistency across all your animations.

