# Travelling-salesman-problem

## greedy()

> Greedy algorithm that is trying to find shortest way throw all vertices.
> 
- parameter: graph: list
- return type: string

> At each iteration we choose shortest edge connected to vertex that has not visited
> 

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
