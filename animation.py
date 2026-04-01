from manim import *

class StoryScene(Scene):
    def construct(self):
        text1 = Text("Once upon a time")
        self.play(Write(text1))
        self.wait(2)

        text2 = Text("There was a boy named Rambabu")
        self.play(Transform(text1, text2))
        self.wait(2)

        text3 = Text("He worked hard")
        self.play(Transform(text1, text3))
        self.wait(2)

        text4 = Text("He became successful")
        self.play(Transform(text1, text4))
        self.wait(2)
