
def earliest_ancestor(ancestors, starting_node):
    graph = {}
    for ancestor in ancestors:
        # Load each relationship with children as parents
        # and parents as children so we can easily travel
        # up the tree instead of downA
        if ancestor[1] in graph:
            graph[ancestor[1]].append(ancestor[0])
        else:
            graph[ancestor[1]] = [ancestor[0]]

    # Return -1 if the starting node has no ancestors
    if starting_node is None or not starting_node in graph:
        return -1

    def find_longest_path(node, path=None):
        if path is None:
            path = [node]

        longest_path = path
        if node in graph:
            # Find the ancestor with the longest path
            for ancestor in graph[node]:
                new_path = path + [ancestor]
                ancestor_path = find_longest_path(ancestor, new_path)
                # Replace the existing `longest_path` with this ancestor's longest path
                # if it's longer, or if it's the same length but with a smaller ending value
                if ((len(ancestor_path) == len(longest_path) and ancestor_path[-1] < longest_path[-1]) or
                        len(ancestor_path) > len(longest_path)):
                    longest_path = ancestor_path

        return longest_path

    longest_path = find_longest_path(starting_node)
    return longest_path[-1]
