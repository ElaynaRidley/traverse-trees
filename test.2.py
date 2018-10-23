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
	#tree.prettyprint()
	
	print("man is a leaf? ", BST.isLeaf(tree.find("man")))
	print("zebra is a leaf? ", BST.isLeaf(tree.find("zebra")))
	print("fly is a leaf? ", BST.isLeaf(tree.find("fly")))