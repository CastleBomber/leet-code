# Example 1
if __name__ == "__main__":
    # Sample inputs from problem
    # Build l1 = 342 , 2 -> 4 -> 3 -> None
    l1_node3 = ListNode(3)
    l1_node2 = ListNode(4, l1_node3)
    l1_head = ListNode(2, l1_node2)

    # Build l2 = 465, 5 -> 6 -> 4 -> None
    l2_node3 = ListNode(4)
    l2_node2 = ListNode(6, l2_node3)
    l2_head = ListNode(5, l2_node2)

    # Create solution instance and call the function
    sol = Solution()
    result = sol.addTwoNumbers(l1_head, l2_head)

    print(result)

# ---------
# Example 2
if __name__ == "__main__":
    # Sample inputs from problem
    # Build l1 = 0 , 0 -> None
    l1_head = ListNode(0)

    # Build l2 = 0 , 0 -> None
    l2_head = ListNode(0)

    # Create solution instance and call the function
    sol = Solution()
    result = sol.addTwoNumbers(l1_head, l2_head)

    print(result)
