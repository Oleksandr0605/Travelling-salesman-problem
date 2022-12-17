"""
Module for solving the travelling salesman problem
"""
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

def greedy(graph):
    """
    Greedy alghorithm that finds approximate shortest hamiltonian cycle
    """
    curr_pos = 0
    verticals_lst = [1]
    while len(verticals_lst) != len(graph)+1:
        min_elm = float('inf')
        min_ind = 0
        for ind_row, elm in enumerate(graph[curr_pos]):
            if elm < min_elm and elm != 0 and ind_row+1 not in verticals_lst:
                min_elm = elm
                min_ind = ind_row
        if min_elm == float('inf') and graph[0][curr_pos] != 0:
            min_elm = graph[0][curr_pos]
        elif min_elm == float('inf'):
            return "do not find a way" 
        verticals_lst.append(min_ind+1)
        graph[curr_pos][min_ind] = 0
        graph[min_ind][curr_pos] = 0
        curr_pos = min_ind
    return  verticals_lst

def exact():
    """
    """
    pass

def main():
    """
    """
    graph = read_file("graph.csv")
    print(greedy(graph))


if __name__ == "__main__":
    main()