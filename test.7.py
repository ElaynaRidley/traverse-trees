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

	traversed = BST.traverse(tree.root, "preorder")
	#print(traversed)
	print([x.payload for x in traversed])

	traversed = BST.traverse(tree.root, "inorder")
	print([x.payload for x in traversed])

	traversed = BST.traverse(tree.root, "postorder")
	print([x.payload for x in traversed])