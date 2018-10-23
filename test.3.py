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
	
	x = tree.find("yak")
	print("The path to yak is ",end="")
	print([y.payload for y in tree.getPath(x)])