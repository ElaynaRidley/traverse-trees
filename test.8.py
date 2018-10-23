
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

	node = BST.find_anywhere(tree.root, "yak")
	if node is None:
		print("yak node not found")
	else:
		print("yak found at node: ",node.payload)

	node = BST.find_anywhere(tree.root, "octopus")
	if node is None:
		print("octopus node not found")
	else:
		print("octopus found at node: ",node.payload)