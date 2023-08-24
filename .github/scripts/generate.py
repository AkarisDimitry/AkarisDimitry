import sys
import random
import svgwrite
from svgwrite import cm, mm

def create_svg(dest, color, background):
    dwg = svgwrite.Drawing(dest, profile='tiny')
    
    pattern = dwg.pattern(size=(10,10), patternUnits="userSpaceOnUse", id="pattern")
    pattern.add(dwg.rect((0,0), (10,10), fill=background))
    pattern.add(dwg.path(d="M-1,1 l2,-2 M0,10 l10,-10 M9,11 l2,-2", stroke=color, strokeWidth=0.5))
    dwg.defs.add(pattern)

    # background will be transparent if not set
    # background = "#ffffff"
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill="url(#pattern)"))

    return dwg

def generate_svg(name, color="#e4e2e2", background="#ffffff"):
    dwg = create_svg(name, color, background)
    dwg.save()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "snake.svg"
    
    generate_svg(name)
