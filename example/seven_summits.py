import matplotlib.pyplot as plt

from mountainplot import Mountain, mountainplot

SEVEN_SUMMITS = [
    Mountain(name='Everest', height=8848 , level=0.56,
             color='lime', text_color='white'),
    Mountain(name='Aconcagua', height=6960, level=0.15,
             color='lime', text_color='white'),
    Mountain(name='Kilimanjaro', height=6194, level=0.87,
             color='lime', text_color='white'),
    Mountain(name='Elbrus', height=5642, level=0.45,
             color='lime', text_color='white'),
    Mountain(name='Vinson', height=4897, level=0.91,
             color='lime', text_color='white'),
    Mountain(name='Carstensz Pyramid', height=4884,
             level=0.33, color='lime', text_color='white'),
    Mountain(name='Mt. Blanc', height=4807, level=0.33,
             color='lime', text_color='white'),
    Mountain(name='Mt. Kosciuszko', height=2228,
             level=0.77, color='lime', text_color='white'),
]


def main():
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    ax.axes.get_xaxis().set_visible(False)
    mountainplot(ax, SEVEN_SUMMITS)
    plt.box(False)
    plt.show()


if __name__ == "__main__":
    main()
