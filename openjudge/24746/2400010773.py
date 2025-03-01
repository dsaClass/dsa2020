
		prev=self.head
		curr=self.head.next
		prev.next=None
		while curr!=None:
			p1=curr
			c1=curr.next
			curr.next=prev
			prev=p1
			curr=c1
		self.head=prev
			
			
		
		
			
		
		
	
