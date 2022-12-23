# Travelling-salesman-problem

## exact()

> This function implements the Held-Karp algorithm for finding a solution to the traveling salesman problem.
> 
- parameter: graph: list
- return type: string

> graph is matrix that represents values of edges. Function also has an option to return result in letters. Instruction to this can be found in code.
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
