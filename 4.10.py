#Elayna Ridley
#Problem 10
class BST:
	class Node:
		def __init__(self, payload):
			self.payload = payload
			self.left = None
			self.right = None
	
	def __init__(self):
		self.root = None

	def prettyprint(self):
		BST.prettyprint_aux(self.root, 0)

	def prettyprint_aux(somenode, indentLevel):
		if somenode.right != None: 
			BST.prettyprint_aux(somenode.right, indentLevel+1)
		for k in range(indentLevel):
			print("    ", end="")
		print(somenode.payload)
		print()
		if somenode.left != None: 
			BST.prettyprint_aux(somenode.left, indentLevel+1)
	
	def find(self, target):
		return BST.find_aux(self.root, target)

	def find_aux(treeptr, target):
		if treeptr == None:
			return None
		if treeptr.payload == target:
			return treeptr
		elif target < treeptr.payload:
			return BST.find_aux(treeptr.left, target)
		else:      # look in right subtree
			return BST.find_aux(treeptr.right, target)

	def attach_in_order(self, new_value):
		if self.root == None:
			self.root = BST.Node(new_value)
		else:
			BST.attach_in_order_aux(self.root, new_value)

	def attach_in_order_aux(treeptr, new_value):
		#  if new_value is less than treeptr's payload,
		if new_value < treeptr.payload:
			if treeptr.left == None:
				treeptr.left = BST.Node(new_value)
			else:
				BST.attach_in_order_aux(treeptr.left, new_value)
		#             if the left child is None then add a new node as left child
		#             else go down the left child subtree
		else:
			if treeptr.right == None:
				treeptr.right = BST.Node(new_value)
			else:
				BST.attach_in_order_aux(treeptr.right, new_value)
		#  else do the same on the right side

	def flip(self):
		flip_aux(self.root)

	def flip_aux(some_node):
		pass

	def isLeaf(some_node):
		return some_node.right == None and some_node.left == None

	def getPath(self, some_node):
		runner = self.root
		returnlist = []
		while runner != None and runner != some_node:
			returnlist.append(runner)
			if some_node.payload < runner.payload:
				runner = runner.left
			else:
				runner = runner.right
		returnlist.append(some_node)
		return returnlist

	def find_parent(self, some_node):
		pass
		runner = self.root
		prev = runner

		if some_node == self.root:
			return None

		while runner != None and runner != some_node:
			if some_node.payload < runner.payload:
				prev = runner
				runner = runner.left
			else:
				prev = runner
				runner = runner.right           
		return prev

	def isBST(some_node):
		if BST.isLeaf(some_node):
			return True
		elif some_node.left is not None:
			if some_node.left.payload > some_node.payload:
				return False
			else:
				return True
		elif some_node.right.payload is not None:
			if some_node.right.payload < some_node.payload:
				return False
			else:
				return True
		else:
			if some_node.left is not None:
				if BST.isBST(some_node.left) is False:
					return False
			elif some_node.right is not None:
				if BST.isBST(some_node.right) is False:
					return False

	def flip(self):
		BST.flip_aux(self.root)

	def flip_aux(someNode):
		#runner = self.root
		someNode.left,someNode.right = someNode.right,someNode.left
		if someNode.left != None:
			BST.flip_aux(someNode.left)
		if someNode.right != None:
			BST.flip_aux(someNode.right)
		#BST.flip(runner.left)

	def traverse(some_node, order):
		orderlist = []
		
		if some_node == None:
			return []

		if order == "preorder":
			orderlist.append(some_node)

		orderlist += BST.traverse(some_node.left,order)
		
		if order == "inorder":
			orderlist.append(some_node)
			
		orderlist += BST.traverse(some_node.right,order)

		if order == "postorder":
			orderlist.append(some_node)
		
		#if order == "inorder":
			#BST.traverse(some_node.left, "inorder") #only goes into each if statement once, stops at the parent, doesn't print any of the parent's children depending on the order because it doesn't actually see the base case
			#orderlist.append(some_node)
			#print(some_node.payload)
			#BST.traverse(some_node.right, "inorder")

		#if order == "preorder":
			#orderlist.append(some_node)
			#print(some_node.payload)
			#BST.traverse(some_node.left, "preorder")
			#BST.traverse(some_node.right, "preorder")
			
		#if order == "postorder":
			#BST.traverse(some_node.left, "postorder")
			#BST.traverse(some_node.right, "postorder")
			#print(some_node.payload)
			#orderlist.append(some_node)
		return orderlist

	def find_anywhere(some_node, value):
		if some_node == None:
			return None
		elif some_node.payload == value:
			return some_node
		value1 = BST.find_anywhere(some_node.left, value)
		value2 = BST.find_anywhere(some_node.right, value)
		if value1 == None and value2 == None:
			return None
		elif value1 != None and value2 == None:
			return value1
		elif value1 == None and value2 != None:
			return value2
		else:
			return None

	def count(some_node):
		count = 1
		if some_node == None:
			return 0
		else:
			return count + BST.count(some_node.left) + BST.count(some_node.right)

	def height(some_node):
		count = 1
		if some_node.left == None and some_node.right == None:
			return 0
		elif some_node.right == None:
			return count + BST.height(some_node.left)
		elif some_node.left == None:
			return count + BST.height(some_node.right)
		else:
			value1 = BST.height(some_node.left)
			value2 = BST.height(some_node.right)
			if value1 > value2:
				return count + BST.height(some_node.left)
			else:
				return count + BST.height(some_node.right)
def main():
	tree = BST()
	tree.root = BST.Node("man")
	tree.attach_in_order("dog")
	tree.attach_in_order("zebra")
	tree.attach_in_order("ape")
	tree.attach_in_order("elephant")
	tree.attach_in_order("yak")
	tree.attach_in_order("zorse")
	tree.attach_in_order("fly")
	tree.prettyprint()

	print("height of tree is",BST.height(tree.root))

	print("height of the tree at node elephant is ",BST.height(tree.find("elephant")))
	print("height of the tree at node yak is ",BST.height(tree.find("yak")))

main()
