"""
DSA Topic: Arrays / Lists

Focus:
- Clear logic
- Explainable approach
- Maintainable code
"""

def remove_duplicates_preserve_order(items):
    """
    Problem:
    Remove duplicates from a list while preserving order.

    Thought process:
    - Use a set to track seen items
    - Iterate once
    - Append only new elements

    Why this approach:
    - O(n) time
    - Readable
    - Works well for real data
    """
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


if __name__ == "__main__":
    data = [1, 2, 2, 3, 1, 4]
    print(remove_duplicates_preserve_order(data))



    '''📌 Rule for DSA files

One topic per file

Multiple problems allowed

Every function explains why, not just how'''
