from manim import * 
class CuadradoEnCirculo(Scene):
    def construct(self):
        C = Circle()
        P = Square()
        self.add(C,P) 
        self.play(Transform(C,P))
        self.wait(3)