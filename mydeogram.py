import numpy as np
import matplotlib.pyplot as plt

#x = np.linspace(-5, 5, 100)
#y = np.sin(x)
def statis(x,y):
    fig, ax = plt.subplots()

    #  Сплошная линия ('-' или 'solid',
    #  установлен по умолчанию):
    ax.plot(x, y,
            linestyle = '-',
            linewidth = 1,
            color = 'crimson')


    fig.set_figwidth(12)
    fig.set_figheight(6)
    fig.set_facecolor('linen')
    ax.set_facecolor('ivory')
    ax.set_ylabel('Проценты')
    ax.set_title('Процент побед на каждую игру')

    plt.show()



