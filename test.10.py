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