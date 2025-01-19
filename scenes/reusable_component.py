from manim.mobject.geometry.polygram import Square
from manim.utils.color.core import ManimColor
from manim.utils.color.manim_colors import *

class MySquare(Square):
    def __init__(
        self,
        fill_color: ManimColor = GREEN_B,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.set_fill(fill_color, opacity=0.5)
