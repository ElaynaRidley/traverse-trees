def main():
	tree = BST()
	tree.root = BST.Node("man")
	somenode = tree.find("man")
	somenode.left = BST.Node("dog")
	somenode.right = BST.Node("zebra")

	tree.attach_in_order("ape")
	tree.attach_in_order("elephant")
	tree.attach_in_order("yak")
	tree.attach_in_order("zorse")
	tree.attach_in_order("fly")
	tree.prettyprint()
	
	payload = "yak"
	parent = tree.find_parent(tree.find("yak"))
	print("The parent of ",payload,"is",parent.payload)

	parent = tree.find_parent(tree.find("zebra"))
	print("The parent of zebra is ",parent.payload)

	parent = tree.find_parent(tree.find("man"))
	if parent is None:
		print("Man has no parent")
	else:
		print("The parent of man is",parent.payload)