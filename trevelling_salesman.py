def read_file(file):
    """
    Read a csv file where each line represents two connected vertexes
    and length between them. The first column of each line is the first vertex,
    the second one is the next vertex, whereas the third column represents the
    length of the rib between them.
    >>> read_file("graph.csv")
    [[0, 3, 2, 1, 1], [3, 0, 2, 1, 0], [2, 2, 0, 5, 2], [1, 1, 5, 0, 3], [1, 0, 2, 3, 0]]
    """
    final_result = []
    my_edges = []
    with open(file, 'r') as file:
        graph = "".join(file.readlines()).split('\n')
        for line in graph:
            my_edges.append(line[0:3])
        for elements in my_edges:
            to_del = elements[::-1]
            if to_del in my_edges:
                index = my_edges.index(to_del)
                my_edges.remove(to_del)
                del graph[index]
        verticle = 1
        flag = 1
        length = 1
        while len(final_result) < length:
            edges = []
            for line in graph:
                line = line.split(',')
                for element in line[0:2]:
                    if int(element) == verticle:
                        edges.append(int(line[2]))
            edges.insert(verticle - 1, 0)
            final_result.append(edges)
            verticle += 1
            if flag:
                length = len(edges)
                flag = 0
        return final_result

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
    main()