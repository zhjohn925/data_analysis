from bokeh.plotting import figure, output_file, show

output_file("demo.html")
p = figure(width=400, height=400, title='line')
p.line([1,2,3,4,5], [6,7,8,9,10], line_width=2)

show(p)
