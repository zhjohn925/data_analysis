from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot
import numpy as np

option = 3

output_file("demo.html")

if option == 1:
    p = figure(width=400, height=400, title='line')
    p.line([1,2,3,4,5], [6,7,8,9,10], line_width=2)
elif option == 2 :
    p = figure(title="Boken Example", x_axis_label='X_value', y_axis_label='Y_value')
    x = np.linspace(0, 10, 30)
    y1 = np.sin(x)
    y2 = np.cos(x)
    p.line(x, y1, legend_label="y=sin(x)")
    p.circle(x, x, legend_label="y=x", fill_color="green", size=5)
    p.line(x, y2, legend_label="y=cos", line_width=3, line_color="red")
    p.triangle(x, x**2, color="black", legend_label="T")
elif option == 3 :
    x = np.linspace(0, 6*np.pi, 100)
    y0 = np.sin(x)
    y1 = np.cos(x)
    y2 = np.sin(x) + np.cos(x) - 1
    s1 = figure(width=400)
    s1.circle(x, y0, size=10, color="navy", alpha=0.5)
    s2 = figure(width=400)
    s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5) 
    s3 = figure(width=400)
    s3.square(x, y2, size=10, color="olive", alpha=0.5)
    p = gridplot([[s1, s2, s3]])  
else :
    pass

show(p)
