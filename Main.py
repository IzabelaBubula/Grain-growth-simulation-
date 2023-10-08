import Points as Pt
import App.App as App


# creating consts
X_L = 5
Y_L = 5
Z_L = 5

points = Pt.create_the_grid(X_L, Y_L, Z_L)  # creating table of points

App.open_app(points)
# Viz.show_whole_shape(points)

