def main():
    with open('input.txt') as f:
        data = [i.split('-') for i in f.read().splitlines()]
    
    graph = make_graph(data)
    total = dfs('start', [], graph, False)

    print(total)


def dfs(node, seen, graph, visited_twice):
    '''
    Recursive Depth-First Search. If path is viable return 1,
    else return 0, then add to total count and return the count.
    '''
    
    seen = seen[:] # make a copy of list seen

    if node == 'end':
        return 1
    if node == 'start' and 'start' in seen:
        return 0
    if node.islower() and node in seen:
        if not visited_twice:
            visited_twice = True
        else:
            return 0

    seen.append(node)
    count = 0

    for i in graph[node]:
        count += dfs(i, seen, graph, visited_twice)

    return count


def make_graph(data):
    '''Returns a dict containing adjacent nodes'''

    graph = {}

    for nodes in data:
        ls, rs = nodes[0], nodes[1]
        if ls not in graph:
            graph[ls] = [rs]
        else:
            graph[ls].append(rs)
        
        if rs not in graph:
            graph[rs] = [ls]
        else:
            graph[rs].append(ls)
    
    return graph


if __name__ == '__main__':
    main()