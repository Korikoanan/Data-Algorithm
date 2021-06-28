def minValueNode(node):
    presentvalue = node
    while presentvalue.left is not None:
        presentvalue = presentvalue.left

    return presentvalue


def maxValueNode(node):
    presentvalue = node
    while presentvalue.right is not None:
        presentvalue = presentvalue.right
    return presentvalue


class Node(object):
    def __init__(object, value):
        object.value = value
        object.left = None
        object.right = None

    def bstInsert(object, value):
        if object.value == value:
            return False

        elif value < object.value:
            if object.left:
                return object.left.bstInsert(value)
            else:
                object.left = Node(value)
                return True

        else:
            if object.right:
                return object.right.bstInsert(value)
            else:
                object.right = Node(value)
                return True

    def bstRemove(object, value, root):
        if object is None:
            return None

        if value < object.value:
            object.left = object.left.bstRemove(value, root)
        elif value > object.value:
            object.right = object.right.bstRemove(value, root)
        else:
            if object.left is None:

                if object == root:
                    temp = minValueNode(object.right)
                    object.value = temp.value
                    object.right = object.right.bstRemove(temp.value, root)

                temp = object.right

                return temp
            elif object.right is None:

                if object == root:
                    temp = maxValueNode(object.left)
                    object.value = temp.value
                    object.left = object.left.bstRemove(temp.value, root)

                temp = object.left

                return temp

            temp = minValueNode(object.right)
            object.value = temp.value
            object.right = object.right.bstRemove(temp.value, root)

        return object

    def bstFind(object, value):
        if value == object.value:
            print("This number exists in the tree!")
        elif value < object.value:
            if object.left:
                return object.left.bstFind(value)
            else:
                print("This number does not exists in the tree!")
        elif value > object.value:
            if object.right:
                return object.right.bstFind(value)
            else:
                print("This number does not exists in the tree!")

    def preorder(object):
        if object:
            print(str(object.value), end=' ')
            if object.left:
                object.left.preorder()
            if object.right:
                object.right.preorder()

    def inorder(object):
        if object:
            if object.left:
                object.left.inorder()
            print(str(object.value), end=' ')
            if object.right:
                object.right.inorder()

    def postorder(object):
        if object:
            if object.left:
                object.left.postorder()
            if object.right:
                object.right.postorder()
            print(str(object.value), end=' ')


class BST(object):
    def __init__(object):
        object.root = None

    def bstInsert(object, value):
        if object.root:
            return object.root.bstInsert(value)
        else:
            object.root = Node(value)
            return True

    def bstRemove(object, value):
        if object.root is not None:
            return object.root.bstRemove(value, object.root)

    def bstFind(object, value):
        if object.root:
            return object.root.bstFind(value)
        else:
            print("This number does not exists in the tree!")

    def preorder(object):
        if object.root is not None:
            print('\nPreorder: ')
            object.root.preorder()

    def inorder(object):
        if object.root is not None:
            print('\nInorder: ')
            object.root.inorder()

    def postorder(object):
        if object.root is not None:
            print('\nPostorder: ')
            object.root.postorder()


if __name__ == '__main__':
    bstvalue = BST()
    bstvalue.bstInsert(9)
    bstvalue.bstInsert(3)
    bstvalue.bstInsert(1)
    bstvalue.bstInsert(6)
    bstvalue.bstInsert(5)
    bstvalue.bstInsert(20)
    bstvalue.bstInsert(30)
    bstvalue.bstInsert(21)
    bstvalue.bstInsert(20)
    print(bstvalue.bstFind(1))
    print(bstvalue.bstFind(12))
    print(bstvalue.bstFind(100))
    bstvalue.preorder()
    bstvalue.inorder()
    bstvalue.postorder()
    bstvalue.bstRemove(5)
    print("\nRespective order after 5 is deleted")
    bstvalue.preorder()
    bstvalue.inorder()
    bstvalue.postorder()
