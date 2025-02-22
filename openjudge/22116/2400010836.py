		if not self.size:
			return None
		flag = 0
		nd = self.tail.next
		fnd = self.tail
		for i in range(self.size):
			if nd.data == data:
				flag = 1
				break
			nd = nd.next
			fnd = fnd.next
		if flag:
			self.size -= 1
			fnd.next = nd.next
			if nd == self.tail:
				self.tail = fnd
			return True
		return False