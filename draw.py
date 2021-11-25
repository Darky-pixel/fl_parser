import matplotlib.pyplot as plt




def draw():
    fig, ax = plt.subplots()

    ax.step([1, 2], [1, 2], linewidth=2.5)
    ax.step([1, 2], [1, 4], linewidth=2.5)

    ax.set(xlim=(0, 8), ylim=(0, 8))

    plt.show()


if __name__ == "__main__":
    draw()