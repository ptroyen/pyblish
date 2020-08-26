import matplotlib.pyplot as plt


fig, ax = plt.subplots()

ax.set_xlim(0, 1920-1)
ax.set_ylim(0, 1080-1)

x,y = [0], [0]
# create empty plot
points, = ax.plot([], [], 'o')

# cache the background
background = fig.canvas.copy_from_bbox(ax.bbox)

def on_move(event):
    # append event's data to lists
    x.append(event.xdata)
    y.append(event.ydata)
    # update plot's data  
    points.set_data(x,y)
    # restore background
    fig.canvas.restore_region(background)
    # redraw just the points
    ax.draw_artist(points)
    # fill in the axes rectangle
    fig.canvas.blit(ax.bbox)



fig.canvas.mpl_connect("motion_notify_event", on_move)
plt.show()

print(y)