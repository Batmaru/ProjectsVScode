# nodo in posizione 0 --> radice
# nodo in posizione i ---> figlio a sinistra sta in posizione 2*1+1
# nodo in posizione i ---> figlio a destra sta in  posizione 2*(i+1) 2*i + 2
# tree = (2,1,4 None, 6,7)

def is_symmetric(tree: list(int)) -> bool:
    pass

def are_mirrored(tree: list[int], left_index:int, right_index:int):
    if left_index >= len(tree) or right_index >=len(tree):
        return left_index == right_index
    
    if tree[left_index] != tree[right_index]:
        return False
    
    left_of_left = 2*left_index+2
    right_of_left = 2*left_index+2

    left_of_right = 2*right_index + 1
    right_of_right = 2*right_index + 2

    symmetric_extremes = are_mirrored(tree, 
                                      left_of_left,
                                      right_of_right)
    symmetric_internals = are_mirrored(tree,
                                       left_of_right,
                                        right_of_left)
    
    return symmetric_extremes and symmetric_internals