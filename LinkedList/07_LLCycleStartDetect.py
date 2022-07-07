def lengthCycle(self,head):
        fast=head
        slow=head
        length=0
        while(fast!=None and fast.next!=None):
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                temp=slow
                while True:
                    temp=temp.next
                    length+=1
                    if temp==slow:
                        break
            return length
            
        return 0

def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Find the length of the cycle
        length =0
        fast=head
        slow=head
        
        while(fast!=None and fast.next!=None):
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                temp=slow
                while True:
                    temp=temp.next
                    length+=1
                    if temp==slow:
                        break
                
        if length==0:
            return -1
        # Find the start node
        f=head
        s=head
        # we have to move s by length(l) of the cycle times
        while(length>0):
            s=s.next
            length-=1
        # we move both f(start to k) and s(l-(l-k)) till they meet at the start of the cycle
        while(f!=s):
            print('in')
            f=f.next
            s=s.next
        
        return s
 