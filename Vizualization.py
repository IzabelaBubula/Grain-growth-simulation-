import matplotlib.pyplot as plt


def get_lists(points):
    x = []
    y = []
    z = []
    c = []
    for i in range(len(points)):
        x.append(points[i].x)
        y.append(points[i].y)
        z.append(points[i].z)
        c.append(points[i].colour)
    return x, y, z, c


def show_whole_shape(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x, y, z, col = get_lists(points)

    import numpy as np
    for i in range(125):
        r = np.random.randint(100)
        col[i] = r;

    # Create a 3D scatter plot
    ax.scatter(x, y, z, c=col)

    # Set labels for the axes
    # ax.set_xlabel('X Label')
    # ax.set_ylabel('Y Label')
    # ax.set_zlabel('Z Label')

    # Show the plot
    # plt.axis('off')
    ax.grid(False)
    plt.show()