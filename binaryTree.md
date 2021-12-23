# 二叉树

### 二叉树的遍历

- 深度优先遍历 -- **栈**
	- 前序遍历（递归/迭代）
	- 中序遍历（递归/迭代）
	- 后序遍历（递归/迭代）
- 广度优先遍历 -- **队列**
	- 层先遍历（迭代）



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```

#### [144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)

**描述：**给你二叉树的根节点 `root` ，返回它节点值的 **前序** 遍历。 

- 递归写法：

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traversal(node):
            if node is None:
                return 
            result.append(node.val)
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return result
```

- 迭代写法：（栈）

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root] if root is not None else []
        result = []

        while len(stack) != 0:
            curr = stack.pop(-1)
            result.append(curr.val)
            if curr.right is not None: stack.append(curr.right)
            if curr.left is not None: stack.append(curr.left)
        return result
```



#### [102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)

**描述：**给你一个二叉树，请你返回其按 **层序遍历** 得到的节点值。 （即逐层地，从左到右访问所有节点）。

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        layer_node = [root] if root is not None else []
        while len(layer_node) != 0:
            layer_result = []
            next_layer_node = []
            while len(layer_node) != 0:
                the_node = layer_node.pop(0)
                layer_result.append(the_node.val)
                if the_node.left is not None: 
                    next_layer_node.append(the_node.left)
                if the_node.right is not None: 
                    next_layer_node.append(the_node.right)
            layer_node = next_layer_node
            result.append(layer_result)
        return result
```

`layer_node`中储存当前层中的节点，将`layer_node`的元素依次出队，出队的元素值记录到`layer_result`中，表示这一层的值，再将所出队的节点的左右子树分别入队到`next_layer_node`中，`next_layer_node`中储存下一层的节点，遍历完`layer_node`后，将该层的值`layer_result`合并到最终`result`中，开始遍历下一层：`layer_node=next_layer_node`。

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        	这段代码不考虑result的值为哪一层的，仅展示逻辑，无法通过leetcode测试
        '''
        result = []
        queue = [root] if root is not None else []
        while len(queue) != 0:
            curr = queue.pop(0)
            result.append(curr.val)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        return result
```

