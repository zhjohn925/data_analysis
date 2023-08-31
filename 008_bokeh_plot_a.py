from bokeh.plotting import figure, output_file, show
import numpy as np

option = 2

output_file("demo.html")

if option == 1:
    p = figure(width=400, height=400, title='line')
    p.line([1,2,3,4,5], [6,7,8,9,10], line_width=2)
else :
    p = figure(title="Boken Example", x_axis_label='X_value', y_axis_label='Y_value')
    x = np.linspace(0, 10, 30)
    y1 = np.sin(x)
    y2 = np.cos(x)
    p.line(x, y1, legend_label="y=sin(x)")
    p.circle(x, x, legend_label="y=x", fill_color="green", size=5)
    p.line(x, y2, legend_label="y=cos", line_width=3, line_color="red")

show(p)
