class Solution:
    def pathInZigZagTree(self, label: int) -> list[int]:
        return self.path_in_zigzag_tree_math(label);
    
    def path_in_zigzag_tree_math(self, label: int) -> list[int]:
        path: list[int] = []

        # Translate label to label in a non-zigzag complete binary tree
        label_bit_len = label.bit_length()
        label_location_index = label
        if label_bit_len % 2 == 0: # Label is in a right->left row
           label_location_index = 2 ** (label_bit_len-1) * 3 - 1 - label
        
        # Path in a non-zigzag complete binary tree
        while label_location_index > 0:
            path.append(label_location_index)
            label_location_index //= 2
        path.reverse()

        # Update path to zigzag labels
        min_label = 1
        for i in range(1, len(path)):
            min_label *= 2
            if i % 2: # is odd layer
                path[i] = 3*min_label - 1 - path[i]

        return path
