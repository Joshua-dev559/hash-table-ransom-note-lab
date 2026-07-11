def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """

    # Dictionary (hash table) to store the frequency of each letter
    letter_counts = {}

    # Count how many times each character appears in the magazine
    for char in magazine:
        letter_counts[char] = letter_counts.get(char, 0) + 1

    # Check whether each character in the ransom note is available
    for char in ransomNote:
        # If the character doesn't exist or has been used up,
        # the ransom note cannot be constructed.
        if char not in letter_counts or letter_counts[char] == 0:
            return False

        # Use one occurrence of the character.
        letter_counts[char] -= 1

    # All characters were successfully matched.
    return True