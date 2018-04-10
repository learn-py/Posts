from matplotlib import pyplot


def main():

    pyplot.plot([1, 3, 5, 7], [1, 2, 3, 4], label="Basic Line")

    pyplot.xlabel('x')
    pyplot.ylabel('y')
    pyplot.title('A Basic Plot')
    pyplot.legend()
    pyplot.show()


if __name__ == '__main__':
    main()
