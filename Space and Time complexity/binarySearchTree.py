def sum(node):
    if (node==null):
        return 0
        
     return sum(node.left)+node.value+sum(node.right)
     
## Just because its a binary search doesnt mean there is log in it!!

## The most straight forward way is to think about what this means. This code touches each node in the tree once and does a constant time amout
## of work with each "touch" (excluding the recursive calls).

## Therefore the runtime will be linear in terms of the number of nodes. If there are N Nodes, then the runtime in O(N)