"""
Write a Python function that prints out the first n rows of the Pascal's triangle.
"""


def foo(layers):
    pascal = {}

    for layer in range(layers+1):
        row = layer + 1
        content = ''
        pascal[row] = []
        if row == 1:
            pascal[row].append(row)
            content = str(row)
        else:
            for col in range(row):
                if 0 < col < row:
                    content += ' '
                if col == 0 or col == layer:
                    pascal[row].append(1)
                else:
                    pascal[row].append(pascal[row-1][col-1] + pascal[row-1][col])
                content += '{:s}'.format(str(pascal[row][col]))
        output(content, row, layers+1)


def output(content, row, rows):
    print (' ' * (rows - row)) + content


def bar(layers):
    trow = [1]
    y = [0]
    for x in range(max(layers, 0)):
        output(str(trow), x, layers+1)
        trow = [l + r for l, r in zip(trow + y, y + trow)]
    return layers >= 1
