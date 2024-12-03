from manim import *

class FocusScene(Scene):
    def construct(self):
        # Set the background color to black
        self.camera.background_color = BLACK

        # Step 1: Create the "FOCUS" text
        text = Text("FOCUS", font_size=100, font="Istok Web", color="#06760D", weight="BOLD")
        text.move_to(ORIGIN)

        # Display the text
        self.play(Write(text))
        self.wait(1)

        # Step 2: Create the dot for the 'C' (to resemble a pupil)
        dot = Circle(radius=0.4, color="#06760D", fill_opacity=1)
        dot.move_to(text[2].get_center())  # Position the dot at the 'C'

        # Step 3: Create an eye-shaped arc for the other letters
        left_arc = Arc(
            radius=2.5,              # Wider radius for the left side of the eye shape
            start_angle=PI,          # Starts from the bottom
            angle=-PI / 2,           # Curves upward to the left
            color="#06760D",         # Dark green color
            stroke_width=10,         # Thicker stroke for better visibility
        )
        right_arc = Arc(
            radius=2.5,              # Wider radius for the right side of the eye shape
            start_angle=0,           # Starts from the bottom
            angle=PI / 2,            # Curves upward to the right
            color="#06760D",         # Dark green color
            stroke_width=10,         # Thicker stroke for better visibility
        )

        # Step 4: Create the transformation animations
        # First, transform the 'F' and 'O' into the left side of the arc
        self.play(
            Transform(text[0], left_arc),  # 'F' transforms into the left arc
            Transform(text[1], left_arc),  # 'O' transforms into the left arc
            Transform(text[3], right_arc),  # 'U' transforms into the right arc
            Transform(text[4], right_arc),  # 'S' transforms into the right arc
            Transform(text[2], dot),
            run_time=1
        )

        # Wait a moment
        self.wait(1)

        # Step 5: Create the single arc that merges the left and right arcs
        full_arc = Arc(
            radius=2.5,
            start_angle=PI,              # Starts from the left side
            angle=-PI,                   # Full arc
            color="#06760D",             # Dark green color
            stroke_width=10,             # Thicker stroke for better visibility
        )

        # Step 7: Animate the arc collapsing into a straight line
        self.play(
            text.animate.stretch_to_fit_height(0).move_to(ORIGIN),  # Shrink the object and keep the bottom fixed
            run_time=0.25
        )

        # Wait before finishing the scene
        self.play(FadeOut(text))

