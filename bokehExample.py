from bokeh.plotting import figure, output_file, show

#fill in code from profile ellipsoidal height offset single script

#bokeh shows same result
'''
#p = figure(title="test", plot_width=300, plot_height=300)
#p.multi_line(xs=[distList, disList], ys=[elevOrigList, elevNewList], color=['red','green'])


p = figure(title="test", width = 800, height = 800)
p.xaxis.axis_label = 'Distance to Benchmark'
p.yaxis.axis_label = 'Elevation'

p.line(x=distList, y=elevOrigList)
p.line(x=distList, y=elevNewList)

show(p)
'''
