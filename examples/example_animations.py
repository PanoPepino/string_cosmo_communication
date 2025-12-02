from manim import *
from manim_beanim import *
from matplotlib import table
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

        bubbles = VGroup(bubble_empty, bubble_radiation, bubble_strings).arrange(
            RIGHT, buff=1).scale_to_fit_width(config.frame_width-1)

        bh_spinning = Black_Hole(bh_type="spinning")
        bh_fragment = Black_Hole(bh_type="fragmentation")

        black_holes = VGroup(bh_spinning, bh_fragment).arrange(RIGHT, buff=10).scale_to_fit_width(config.frame_width-5)

        ads_db = AdS_Jc(vacua_type="DB")
        ads_rs = AdS_Jc(vacua_type="RS")

        ads_configs = VGroup(ads_db, ads_rs).arrange(RIGHT, aligned_edge=DOWN,
                                                     buff=1).scale_to_fit_width(config.frame_width-1)

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


class Beanim_and_String_Cosmo(Scene):
    def construct(self):
        aa = Title_Section(content="Your Test Title goes here")
        bb = Underbar(content=['test', 'here', 'there', 'never'])
        cc = Bubble("em").scale(0.7)

        self.add(aa, bb, cc)


class Generic_Slide_1(Scene):
    def construct(self):
        bubble_empty = Bubble(bubble_type="em")
        bubble_radiation = Bubble(bubble_type="radiation")
        bubble_strings = Bubble(bubble_type="strings")
        bubble_gw = Bubble(bubble_type="GW")

        bubbles = VGroup(bubble_empty, bubble_radiation, bubble_strings, bubble_gw).arrange_in_grid(
            2, 2, buff=1).scale_to_fit_height(config.frame_height-1)

        self.play(AnimationGroup(
            *[bub.fade_in_bulk() for bub in bubbles]
        ))
        # self.next_slide(loop=True)
        self.play(AnimationGroup(
            *[bub.create_bubble() for bub in bubbles]
        ))
        self.wait()
        # self.next_slide(loop=True)
        self.play(AnimationGroup(
            *[bub.expand_bubble() for bub in bubbles]
        ))


class Generic_Slide_2(Scene):
    def construct(self):
        table_bh = Table_Bh_Embedding("together").shift(UP).scale_to_fit_width(config.frame_width-2)
        bh = Black_Hole(bh_type="spinning").next_to(table_bh, DOWN, buff=2)
        self.add(table_bh, bh)
        self.play(bh.nucleate())
        self.play(bh.expand())


class Example_Bubble(Scene):
    def construct(self):
        bubble_types = ["empty", "radiation", "em", "strings", "GW"]
        bubble_group = Group(*[Bubble(bubble_type=style).scale(0.4)
                               for style in bubble_types])
        bubble_group.arrange_in_grid(2, 3)

        self.play(AnimationGroup(*[x.fade_in_bulk() for x in bubble_group]))
        self.play(AnimationGroup(*[x.create_bubble() for x in bubble_group]))
        self.play(AnimationGroup(*[x.expand_bubble() for x in bubble_group]))
