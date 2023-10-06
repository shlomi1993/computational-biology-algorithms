# File: style.py
# Content: Fonts, colors and scale for easy controlling the theme (like CSS).


class Fonts:
    def __init__(self):
        self.regular = ('Consolas', 12)
        self.io = ('Consolas', 17)
        self.bold = ('Consolas', 12, 'bold')
        self.big = ('Consolas', 16)
        self.small = ('Consolas', 10)


class Colors:
    def __init__(self):
        self.app = '#302c34'
        self.io_bg = '#282c34'
        self.io_text = '#ffffff'
        self.button = '#3d424b'
        self.button_prime = '#568af2'
        self.notes = '#C2FCF7'
        self.outlines = '#57737A'
        self.highlight = '#1f7db7'
        self.black = '#040F0F'
        self.white = '#ffffff'


# This instances can be accessed from the whole program.
fonts = Fonts()
colors = Colors()

# This scale helps to determine the colors of the clusters in the assignments.
scale = {
    0: '#ffffff',
    1: '#9e0142',
    2: '#d53e4f',
    3: '#f46d43',
    4: '#fdae61',
    5: '#fee08b',
    6: '#e6f598',
    7: '#abdda4',
    8: '#66c2a5',
    9: '#3288bd',
    10: '#5e4fa2'
}
