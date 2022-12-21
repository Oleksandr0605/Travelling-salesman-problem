"""
Module for solving the travelling salesman problem
"""
import csv
import copy
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

def greedy(graph1):
    """
    Greedy alghorithm that finds approximate shortest hamiltonian cycle
    """
    graph = copy.deepcopy(graph1)
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

def exact(graph: list):
    """
    Finds cycle of minimum lenght
    >>> exact([[0, 3, 1, 2], [3, 0, 3, 4], [1, 3, 0, 20], [2, 4, 20, 0]])
    'path = [1, 4, 2, 3, 1], length = 10'
    """
    dct = {}
    for i in range(len(graph)):
        dct[i] = chr(65 + i)
    # print(dct)

    start = 0
    end = 0

    start_points = list(dct.keys())
    start_points.remove(start)

    global memory
    memory = []

    def find_min(graph, start, points, end, result = []):
        """
        Finds cycle of minimum lenght
        """
        if len(points) == 1:
            path = f'{dct[start]} {dct[points[0]]} {dct[end]}'
            if graph[points[0]][end] * graph[start][end] != 0:
                # print([path, graph[start][points[0]] + graph[points[0]][end] ])
                return [path, graph[start][points[0]] + graph[points[0]][end] ]
            else:
                # print([f'No {path}', float('inf')])
                return  [f'No {path}', float('inf')]
        else:
            for i in points:
                new_points = [item for item in points if item != i]
                special_marking = ''.join(str(dct[el]) for el in new_points)
                path = f'{dct[start]} {special_marking} {dct[i]}+{dct[end]}'
                if graph[i][end] != 0:
                    result.append([path , find_min(graph, start, new_points, i, [])[1] + graph[i][end]])
                else:
                    result.append([f'No {path}' , float('inf')])
            
            answer = min(result, key = lambda x: x[1])
            memory.append(answer[0])
            
            return answer
    
    answer = find_min(graph, start, start_points, end, result = [])

    def decode(memory, answer):
        """
        Decodes answer that find_min returns
        """
        work_list = reversed(memory)
        length = len(answer[0])
        sign = '+A'
        result = []
        result_modified = ''
        for i in work_list:
            if len(i) == length and sign in i:
                sign = '+' + i[-3]
                length -= 1
                result = [i] + result
                if len(i) == 7:
                    break
            else:
                continue
        result_modified = result[0]
        for j in result[1:]:
            result_modified += j[-1]
        return result_modified.replace('+', '').replace(' ', '')
    
    def letters_into_numbers(dictionary, answer_in_letters):
        """
        Turns letter-styled answer into numbers list
        """
        result = []
        reverce_dct = dict((v, k) for k, v in dictionary.items())
        for i in answer_in_letters:
            result.append(reverce_dct[i] + 1)
        return result
    
    if answer[1] == float('inf'):
        return 'No such way'
    else:
        return f'path = {letters_into_numbers(dct, decode(memory, answer))}, length = {answer[1]}'

# matrixes for tests
# matrix = [[0, 3, 1, 2], [3, 0, 3, 4], [1, 3, 0, 20], [2, 4, 20, 0]]
# matrix = [[0, 3, 2, 1, 1], [3, 0, 2, 1, 0], [2, 2, 0, 5, 2], [1, 1, 5, 0, 3], [1, 0, 2, 3, 0]]
# matrix = [[0, 3, 2, 1, 0], [3, 0, 2, 1, 0], [2, 2, 0, 5, 0], [1, 1, 5, 0, 0], [0, 0, 0, 0, 0]]
# matrix = [[0, 3, 2, 1, 1, 3], [3, 0, 2, 1, 0, 0], [2, 2, 0, 5, 2, 2], [1, 1, 5, 0, 3, 0], [1, 0, 2, 3, 0, 0], [3, 0, 2, 0, 0]]

# print(exact(matrix))


def main():
    """
    """
    graph = read_file("graph.csv")
    # print(graph)
    print(greedy(graph))
    print(exact(graph))


if __name__ == "__main__":
    # import doctest
    # print(doctest.testmod())
    main()