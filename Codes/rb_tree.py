'''
this module has classes that are data structures
'''

'''
node for the Red-Black tree
count is the satellite data
ngrams is the key value
_Node is an internal class, can't be imported
'''
# internal class
class _Node:
	def __init__(self, ngrams, sentinel):
		
		# left child for the node
		self.l_child = sentinel
		
		# right child for the node
		self.r_child = sentinel
		
		# parent of the node
		self.parent = sentinel
		
		# 3-grams, 5-grams and 7-grams
		self.ngrams = ngrams
		
		# Red - 0, Black - 1
		self.colour = 0
		
		# no. of times this ngrams has appeared
		self.count = 1

'''
internal methods can't be accessed from outside
Red-Black Trees
'''
class RedBlackTree:
	def __init__(self):
		self.sentinel = _Node([], None)
		self.sentinel.colour = 1
		self.sentinel.parent = self.sentinel
		self.root = self.sentinel



	# internal method
	def __left_rotate(self, node_x):
		node_y = node_x.r_child
		node_y.l_child.parent = node_x
		node_x.r_child = node_y.l_child
		node_y.parent = node_x.parent
		if node_x.parent == self.sentinel:
			self.root = node_y
			self.root.parent = self.sentinel
		else:
			if node_x == node_x.parent.l_child:
				node_x.parent.l_child = node_y
			else:
				node_x.parent.r_child = node_y
		node_x.parent = node_y
		node_y.l_child =node_x





	# internal method
	def __right_rotate(self, node_x):
		node_y = node_x.l_child
		node_y.r_child.parent = node_x
		node_x.l_child = node_y.r_child
		node_y.parent = node_x.parent
		if node_x.parent == self.sentinel:
			self.root = node_y
			self.root.parent = self.sentinel
		else:
			if node_x.parent.l_child == node_x:
				node_x.parent.l_child = node_y
			else:
				node_x.parent.r_child = node_y
		node_y.r_child = node_x
		node_x.parent = node_y





	# internal method
	def __red_black_insert_fixup(self, node_z):
		while 0 == node_z.parent.colour:
			if node_z.parent == node_z.parent.parent.l_child:
				node_y = node_z.parent.parent.r_child
				if 0 == node_y:
					node_z.parent.colour = 1
					node_y.colour = 1
					node_z.parent.parent.colour = 0
					node_z = node_z.parent.parent
				else:
					if node_z == node_z.parent.r_child:
						node_z = node_z.parent
						self.__left_rotate(node_z)
					node_z.parent.colour = 1
					node_z.parent.parent.colour = 0
					self.__right_rotate(node_z.parent.parent)
			else:
				node_y = node_z.parent.parent.l_child
				if 0 == node_y:
					node_z.parent.colour = 1
					node_y.colour = 1
					node_z.parent.parent.colour = 0
					node_z = node_z.parent.parents
				else:
					if node_z == node_z.parent.l_child:
						node_z = node_z.parent
						self.__right_rotate(node_z)
					node_z.parent.colour = 1
					node_z.parent.parent.colour = 0
					self.__left_rotate(node_z.parent.parent)
		self.root.colour = 1




	#--------------------------------------------------------------------------------------------------------------------------------------
	"""
	usage - red_black_insert((x1, x2, x3,...))
	"""
	def red_black_insert(self, tuple_insert_grams):
		insert_grams = list(tuple_insert_grams)
		node_y = self.sentinel
		node_x = self.root
		while node_x != self.sentinel:
			node_y = node_x
			if -1 == self.__compare(insert_grams, node_x.ngrams):
				node_x = node_x.l_child
			elif +1 == self.__compare(insert_grams, node_x.ngrams):
				node_x = node_x.r_child
			else:
				node_x.count += 1
				return
		node_z = _Node(insert_grams, self.sentinel)
		node_z.parent = node_y
		if node_y == self.sentinel:
			self.root = node_z
		else:
			if -1 == self.__compare(node_z.ngrams, node_y.ngrams):
				node_y.l_child = node_z
			else:
				node_y.r_child = node_z
		self.__red_black_insert_fixup(node_z)
	#--------------------------------------------------------------------------------------------------------------------------------------




	#--------------------------------------------------------------------------------------------------------------------------------------
	"""
	usage - output = get_elements()
	output type = dictionary
	output is the ngrams with their periodicity
	"""
	def get_elements(self):
		dictionary = {}
		if self.sentinel == self.root:
			return dictionary
		self.__recursive_copy(self.root, dictionary)
		return dictionary
	#--------------------------------------------------------------------------------------------------------------------------------------
	
	
	
	# internal method
	def __recursive_copy(self, node_x, dictionary):
		if node_x.l_child != self.sentinel:
			self.__recursive_copy(node_x.l_child, dictionary)
		if node_x.r_child != self.sentinel:
			self.__recursive_copy(node_x.r_child, dictionary)
		dictionary[tuple(node_x.ngrams)] = node_x.count
	
	
	
	'''
	-1 if ngrams1 is less than ngrams2
	 0 if ngrams1 is equal to ngrams2
	+1 if ngrams1 is greater than ngrams2
	'''
	# internal method
	def __compare(self, ngrams1, ngrams2):
		size_of_grams = len(ngrams1)
		for i in range(0, size_of_grams):
			if ngrams1[i] > ngrams2[i]:
				return 1
			elif ngrams1[i] < ngrams2[i]:
				return -1
			elif i == size_of_grams - 1:
				return 0
