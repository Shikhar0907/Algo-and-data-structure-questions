class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def evaluate(root):

    if root is None:
        return(0)
    if root.left is None and root.right is None:
        return(root.data)

    left_sum = evaluate(root.left)
    right_sum = evaluate(root.right)

    if root.data == '+':
        return(left_sum + right_sum)

    elif root.data == '-':
        return(left_sum - right_sum)

    elif root.data == '*':
        return(left_sum * right_sum)
    else:
        return(left_sum/right_sum)
 
def main():
    root = Node('+')
    root.left = Node('*')
    root.left.left = Node(5)
    root.left.right = Node(4)
    root.right = Node('-')
    root.right.left = Node(100)
    root.right.right = Node(20)

    print(evaluate(root))

    evaluate(root)
    
main()
