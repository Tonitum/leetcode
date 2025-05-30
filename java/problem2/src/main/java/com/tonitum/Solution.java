package com.tonitum;

public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // track the tail end of the list.
        ListNode tail = new ListNode(0);
        // if tail ends up being 0, we want to drop it, so we need the prev node.
        ListNode prev = tail;
        // we need this to be able to return the entire linked list.
        ListNode head = tail;
        // this is used to carry any 1's that result from adding numbers >= 5
        int carryover = 0;

        // l1 and l2 may not be the same size, so we need to iterate until
        // we reach the end of BOTH lists.
        while (l1 != null || l2 != null) {
            // first, add any ones that were carried over.
            int newVal = carryover;
            // if the first list node isn't null, grab the value and walk the
            // list forward.
            if (l1 != null) {
                newVal += l1.val;
                l1 = l1.next;
            }
            // if the second list node isn't null, grab the value and walk the
            // list forward.
            if (l2 != null) {
                newVal += l2.val;
                l2 = l2.next;
            }
            // capture any 1's that would be carried over.
            carryover = newVal / 10;

            // for the current node value, we only care about what wouldn't get
            // carried over.
            tail.val = newVal % 10;

            // create a new node for our tail
            tail.next = new ListNode(0);
            // track the current tail so we can drop the tail if we need to.
            prev = tail;

            // point the tail to the new node.
            tail = tail.next;
        }
        // if there is a carryover from the last nodes, we need to add that 
        // to the list.
        if (carryover > 0) {
            tail.val += carryover;
        }
        // if the tail has a value of 0, that would be equivalent to a leading
        // 0, which we do not want to include.
        if (tail.val == 0) {
            prev.next = null;
        }
        return head;
    }
}
