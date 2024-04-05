"""

604. Design Compressed String Iterator

Design and implement a data structure for a compressed string iterator.
It should support the following operations: next and hasNext.

The given compressed string will be in the form of each letter followed
by a positive integer representing the number of this letter existing in the original uncompressed string.

next() - if the original string still has uncompressed characters,
return the next letter; Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.

Note:
Please remember to RESET your class variables declared in StringIterator,
as static/class variables are persisted across multiple test cases.
Please see here for more details.

Example:

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '
"""

# Solution
# Convert Compressed string to a sorted increasing list, for example
# L1e2t1C1o1d1e1 becomes [(1, "L"), (3, "e"), (4, "t"), ...]
# Use self.curr_index to track current letter
# bisect.bisect_left() to search for proper location of curr_index, thereby finding letter
