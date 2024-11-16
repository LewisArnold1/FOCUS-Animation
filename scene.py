from manim import *

class FocusScene(Scene):
    def construct(self):
        # Set the background color to white
        self.camera.background_color = WHITE

        # Step 1: Create the "FOCUS" text
        text = Text("FOCUS", font_size=72, font="Istok Web", color="#06760D")
        text.move_to(ORIGIN)

        # Display the text
        self.play(Write(text))
        self.wait(1)

        # Step 2: Create the dot for the 'C' (to resemble a pupil)
        dot = Circle(radius=0.3, color="#06760D")
        dot.move_to(text[1].get_center())  # Position the dot at the 'C'

        # Step 3: Create an eye-shaped arc for the other letters
        eye_arc = Arc(
            radius=2.5,              # Wider radius for an eye shape
            start_angle=PI,          # Starts from the bottom
            angle=-PI,               # Curves upward
            color="#06760D",         # Dark green color
            stroke_width=10,         # Thicker stroke for better visibility
        )
        eye_arc.stretch_to_fit_width(6)  # Stretch horizontally to mimic an eye shape
        eye_arc.move_to(ORIGIN)  # Position the arc below the text

        # Step 4: Create the transformation
        # First, transform the 'C' into the dot
        self.play(Transform(text[1], dot))  # The 'C' will transform into the dot
        self.wait(1)

        # Then, transform the other letters into the eye arc shape
        self.play(
            Transform(text[0], eye_arc),  # Transform 'F' to the arc
            Transform(text[2], eye_arc),  # Transform 'U' to the arc
            Transform(text[3], eye_arc),  # Transform 'S' to the arc
            run_time=2
        )

        # Wait before finishing the scene
        self.wait(2)

