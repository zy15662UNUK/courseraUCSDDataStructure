
class Node(object):

	def __init__(self, data):
		self.data = data;
		self.nextNode = None;# atthe benginning is the none
		
class LinkedList(object):

	def __init__(self):
		self.head = None;# the first node in the list
		self.size = 0;# we are only able to access the first and access the other with the help of the next node
		
		
	# O(1) !!!	
	def insertStart(self, data):# insert some data at the beginning of the list
	
		self.size = self.size + 1;
		newNode = Node(data);
		
		if not self.head:# i.e. the head == None(adding in the first item)
			self.head = newNode;
		else:
			newNode.nextNode = self.head;# link the last head to the new head
			self.head = newNode;# switch
			
	def remove(self, data):
	
		if self.head is None:
			return;
			
		self.size = self.size - 1;
		
		currentNode = self.head;
		previousNode = None;
		
		while currentNode.data != data:
			previousNode = currentNode;
			currentNode = currentNode.nextNode;
			
		if previousNode is None:
			self.head = currentNode.nextNode;# remove the first
		else:
			previousNode.nextNode = currentNode.nextNode;# remove the current node			
		
	# O(1)	
	def size1(self):
		return self.size;
		
	# O(N) not good !!!	
	def size2(self):
		
		actualNode = self.head;
		size = 0;
		
		while actualNode is not None:
			size+=1;
			actualNode = actualNode.nextNode;
			
		return size;
		
	# O(N)
	def insertEnd(self, data):
	
		self.size = self.size + 1;
		newNode = Node(data);
		actualNode = self.head;
		
		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode;# remove the nodes to create a space for the new end
			
			
		actualNode.nextNode = newNode;# set the new item be the last item
		
	def traverseList(self):
	
		actualNode = self.head;
		
		while actualNode is not None:
			print("%d " % actualNode.data);
			actualNode = actualNode.nextNode;


			
linkedlist = LinkedList();

linkedlist.insertStart(12);
linkedlist.insertStart(122);
linkedlist.insertStart(3);
linkedlist.insertEnd(31);

linkedlist.traverseList();

linkedlist.remove(3);
linkedlist.remove(12);
linkedlist.remove(122);
linkedlist.remove(31);

print(linkedlist.size1());












			
