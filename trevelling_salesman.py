import csv
def read_file(file):
    """
    Read a csv file where each line represents two connected vertexes
    and length between them. The first column of each line is the first vertex,
    the second one is the next vertex, whereas the third column represents the
    length of the rib between them.
    """
    with open(file, "r", encoding="utf-8") as fff:
        csvreader = csv.reader(fff)
        mas = []
        for row in csvreader:
            mas.append(row)
    mxm = 0
    for lst in mas:
        if int(lst[0]) > mxm:
            mxm = int(lst[0])
        if int(lst[1]) > mxm:
            mxm = int(lst[1])
    matrix = []
    for ind in range(mxm):
        _ = []
        for jnd in range(mxm):
            _.append(0)
        matrix.append(_)
    for lst in mas:
        matrix[int(lst[0])-1][int(lst[1])-1] = int(lst[2])
        matrix[int(lst[1])-1][int(lst[0])-1] = int(lst[2])
    return matrix

def greedy():
    """
    """
    pass

def exact():
    """
    """
    pass

def main():
    """
    """
    pass


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    main()