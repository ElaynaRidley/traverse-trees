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

	print("count of nodes is",BST.count(tree.root))

	print(tree.find("elephant"))
	print("count of nodes starting at elephant is",BST.count(tree.find("dog")))