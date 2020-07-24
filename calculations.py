from cassius import *

draw(Curve("x**2", xmin=-5., xmax=5., ymin=0., xlabel=u"\u03d5", ylabel=u"V", bottommargin=0.15, xlabeloffset=0.15), width=800, height=500, fileName="potential_quadratic.svg")

draw(Curve("-2.7*x**2 + 0.15*x**4", xmin=-5., xmax=5., ymin=-20, xlabel=u"\u03d5", ylabel=u"V", bottommargin=0.15, xlabeloffset=0.15), width=800, height=500, fileName="potential_mexicanhat.svg")
