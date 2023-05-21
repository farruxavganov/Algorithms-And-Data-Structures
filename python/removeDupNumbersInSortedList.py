def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
	if head == None:
		return None
	prev = head
	temp = prev.next
	
	while temp != None:
		if temp.val == prev.val:
			temp = temp.next
			continue
		prev.next = temp
		prev = temp
		temp = temp.next
	prev.next = None
	return head
	
