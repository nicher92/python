
nodes = [
			("node1", "node1"),
			("node2", "node1"),
			("node3", "node8"),
			("node4", "node2"),
			("node5", "node1"),
			("node6", "node7"),
			("node7", "node7"),
			("node8", "node9"),
			("node9", "node6"),
		]
		


def construct_trees(nodes:list):

	"""
	given the following list where the first item in the tuple is the node_id and 
	the second item is the node_id of the parent; (NODE_ID, PARENT_NODE_ID)
	
	nodes = [
				("node1", "node1"),
				("node2", "node1"),
				("node3", "node8"),
				("node4", "node2"),
				("node5", "node1"),
				("node6", "node7"),
				("node7", "node7"),
				("node8", "node9"),
				("node9", "node6"),
				]

	create the following nested dict:

	{
		"node1": {
					"node2": {
								"node4":
										{
										
										}
								},
					"node5": {},

					},
		"node7": {
					"node6":{
								"node9":
										{
											"node8":{
														"node3":{}
													}
										}
								}

					}
 
		}



	Restrictions
	1) place_node() should be a recusive function
	
	Tips!
		- let construct_trees() run until all nodes are places, or until there are no more
		nodes to place!
		- you might need a special condition to deal with the root of trees, e.g, nodes that have themselves as parents.

	"""
	
	#Dictionary to be filled with nodes
	tree = dict()

	
	def place_node(TREE_DICT_SLICE, NODE):
		"""
		A recursive function which places a node in a nested dictionary structure. It takes two arguments:
			TREE_DICT_SLICE: A dictionary tree (which under recursion can be a subset of the original dictionary) which will be checked to see if a node can be placed. 
			NODE: Is the tuple (NODE_ID, PARENT_NODE_ID)
		On each iteration the function will check a set of conditions to see if it can place the node in the given dictionary slice/subset TREE_DICT_SLICE, and if not, will traverse the tree structure by calling itself recursively on each item/key within TREE_DICT_SLICE (see the 'else' condition and contained 'for-loop').
		Note that, once a node is placed, the placed node keys will be returned as a tuple (NODE_ID, PARENT_NODE_ID), and passed back through the recursion tree. This is so that we can know which items were not placed in the dictionary (because sometimes a directory doesn't exist yet) so we can run it again until all the items are in. 

		"""
		NODE_ID, PARENT_NODE_ID = NODE
		
		if NODE_ID == PARENT_NODE_ID:									#If the node is a root-level node...
			if not (PARENT_NODE_ID in TREE_DICT_SLICE.keys()):			#We don't want to accidentally replace a node if it already exists
				TREE_DICT_SLICE[NODE_ID] = dict()						#Make the node!
				return (NODE_ID, PARENT_NODE_ID)						#If the key is placed, we return the key
				
		elif PARENT_NODE_ID in TREE_DICT_SLICE:							#If the node is in the part of the tree we are traversing currently
			if not (NODE_ID in TREE_DICT_SLICE[PARENT_NODE_ID].keys()):	#Again, we don't want to accidentally replace a node if it already exists
				TREE_DICT_SLICE[PARENT_NODE_ID][NODE_ID] = dict()		#Make the node!
				return (NODE_ID, PARENT_NODE_ID)						#If the key is placed, we return the key
				
		else:
			for key in TREE_DICT_SLICE.keys():							#If the node we want to place isn't in this part of the directory, we check in all the children of the current node, by calling place_node() recursively and pass in the corresponding part of the tree we want to check (of child).
				placed_node = place_node(TREE_DICT_SLICE[key], (NODE_ID, PARENT_NODE_ID))
				if placed_node != None:	
					return placed_node									#Pass the placed node up the levels of recursion if one is found, otherwise will default None
	

	while True:															#Need to repeat until the tree is filled, because sometimes a parent node doesn't exist yet because of the arrangement of the keys/nodes in the 'nodes' list. The breaking condition is later. 
		for node in nodes:
			matched_node = place_node(tree, node)						#Attempt to place the node. If it is placed, we get back the node tuple back. 
			if matched_node != None:									#If a node was placed...
				nodes.remove(matched_node)								#Then, we can remove it from our list of nodes (to be placed in the tree)
		
		#Breaking condition, if we have no more nodes to place in the tree, then we are done. 
		if len(nodes) == 0:
			break

	#YES
	print(tree)

if __name__=="__main__":
	construct_trees(nodes)


