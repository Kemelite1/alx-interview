#!/usr/bin/python3

def canUnlockAll(boxes):
     """
    Function that checks with boolean value if the list type and
    length to invoke two for iterations one to traverse the list
    and the other to compaer if key is idx or not in order to open
    """
     opened_boxes = set([0])
     keys_to_use = [0]
     
     while keys_to_use:
        current_key = keys_to_use.pop()
        
        for key in boxes[current_key]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                keys_to_use.append(key)
                return len(opened_boxes) == len(boxes)