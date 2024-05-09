def visit_tree(tree: dict[int, list[int]], node: int):
    print(node)
    left_child, right_child= tree.get(node, [None, None])
    if left_child: #is not None
        visit_tree(tree, left_child)
    if right_child:
        visit_tree(tree, right_child)

tree = {
    4: [3,5], 
    3: [2, None],
    5: [4.5, 6],
    4.5: [None, None],
    6: [None, None]
}
#visit_tree(tree,3)


def visit_tree_iterative(tree: dict[int,list[int]], root: int):
    stack: list[int] = [root] #last-In-Firs-Out (LIFO)
    while stack:
        curr_node = stack.pop(0)
        print(curr_node)
        left_child, right_child = tree.get(curr_node, [None, None])
        if right_child:
            stack.append(left_child)
        if left_child:
            stack.append(right_child)
       

tree = {
    4: [3,5], 
    3: [2, None],
    5: [4.5, 6],
    4.5: [None, None],
    6: [None, None]
}
visit_tree_iterative(tree, 4)

def avg_level(tree: dict[int,list[int]], root: int):
    nodes_for_level: dict[int, float] = {}
    stack: list[int] = [(root,0)] #last-In-Firs-Out (LIFO)
    while stack:
        curr_node, curr_level = stack.pop(0)
        nodes_for_level[curr_level] = nodes_for_level.get(curr_level,0) + 1
        left_child, right_child = tree.get(curr_node, [None, None])
        if right_child:
            stack.append((left_child, curr_level + 1))
            avg_for_level[curr_level = avg_for_level.get(curr_level,0)]
        if left_child:
            stack.append(right_child)