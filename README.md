# Travelling-salesman-problem

## read_csv()

> In this function we need to implement reading from a file. We are given a csv file. By convention, in this file, the first column of the edge is the first vertex, the second is the second, and the third is the weight of the edge. To implement this function, we created a graph.csv file, the content of which looks like this:
> 

```css
csv file
1,2,3
1,3,2
1,4,1
1,5,1
2,1,3
2,3,2
2,4,1
2,5,0
3,4,5
3,5,2
4,5,3
5,3,2
```

- [[0, 3, 2, 1, 1], [3, 0, 2, 1, 0], [2, 2, 0, 5, 2], [1, 1, 5, 0, 3], [1, 0, 2, 3, 0]]

> Next, in order to develop the following functions, we decided that we need to represent the graph as an adjacency matrix for a weighted graph. Because, in the next function, we will need to find the shortest Hamiltonian cycle, and it is easiest to do this when the graph is specified in this way. Therefore, our function must return the matrix as a list of lists.
> 

Author: Yaryna Petruniv

Helpers: Oleksandr Ivaniuk 

```python
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
```

## greedy()

> Greedy algorithm that is trying to find shortest way throw all vertices.
> 
- parameter: graph: list
- return type: string

> At each iteration we choose shortest edge connected to vertex that has not visited
> 

Aurthor: Oleksandr Ivaniuk 

```python
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
```

## exact()

> This function implements the Held-Karp algorithm for finding a solution to the traveling salesman problem. At each call of a function we make list of points through which we need to go shorter therefore we will reach the end.
> 
- parameter: graph: list
- return type: string

> Graph is matrix that represents values of edges. Function also has an option to return result in letters. Instruction to this can be found in code.
> 

Author: Ustym Hentosh

```python
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
        # # if you want result in letters uncomment row below
        # return f'dictionary = {dct}, path = {decode(memory, answer)}, length = {answer[1]}'
        return f'path = {letters_into_numbers(dct, decode(memory, answer))}, length = {answer[1]}'
```

## time_test()

> Function tests time of execution of exact and greedy algorithms. It calls each algo 10000 times in order to get more precise result.
> 
- parameters function: int (0 or 1)
- return type: float

```python
def time_test(function=0):
    '''
    Test time execution time of function
    If function = 0, runs greedy algorithm time test
    If function = 1, runs exact algorithm time test
    '''
    greedy_alg = timeit.timeit(stmt='''greedy([[0, 3, 2, 1, 1], [3, 0, 2, 1, 0], [2, 2, 0, 5, 2],
                                       [1, 1, 5, 0, 3], [1, 0, 2, 3, 0]])''',
                               setup='from __main__ import greedy',
                               number=10000)
    exact_alg = timeit.timeit(stmt='''exact([[0, 3, 2, 1, 1], [3, 0, 2, 1, 0], [2, 2, 0, 5, 2],
                                      [1, 1, 5, 0, 3], [1, 0, 2, 3, 0]])''',
                               setup='from __main__ import exact',
                               number=10000)
    if function:
        return exact_alg
    else:
        return greedy_alg
```

| Member | Contribution |
| --- | --- |
| Oleksandr Ivaniuk  | greedy, presentation, report |
| Yaryna Petruniv | read_csv, presentation, report |
| Ustym Hentosh | exact, presentation, report |
| Taras Lysun | hard thinking, presentation, time_test |
| Anna Yaremko | presentation |
