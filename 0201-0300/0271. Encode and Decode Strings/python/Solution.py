from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings into a single serialized string.
        
        Methodology:
        We use 'Length-Prefixing'. Each string is prefixed by its 
        own length and a delimiter ('#'). This ensures that the 
        original boundaries are preserved regardless of the string content.
        """
        # Using a generator expression with "".join() is more memory-efficient
        # than repeated string concatenation in Python.
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """
        Decodes the serialized string back into the original list.
        
        Methodology:
        We utilize a 'Two-Pointer' approach or 'Pointer Jumping'.
        1. Find the delimiter to identify the end of the 'length' metadata.
        2. Parse the integer to determine the segment size.
        3. Extract the exact slice and jump the pointer to the next header.
        """
        res = []
        i = 0  # 'i' represents the starting index of the current segment header
        
        while i < len(s):
            # Locate the next delimiter starting from index i
            # .find() is a C-optimized method, providing high performance.
            j = s.find("#", i)
            
            # Extract the metadata (length) and convert it to an integer
            length = int(s[i:j])
            
            # Slice the string from the character immediately after '#' 
            # to the end of the specified length.
            # Start index: j + 1, End index: j + 1 + length
            res.append(s[j + 1 : j + 1 + length])
            
            # Update the pointer 'i' to the beginning of the next segment
            i = j + 1 + length
            
        return res

# --- Testing Block (Educational Main) ---
if __name__ == "__main__":
    codec = Solution()
    # Test Case 1: Standard strings
    test1 = ["Hello", "World"]
    encoded1 = codec.encode(test1)
    decoded1 = codec.decode(encoded1)
    print(f"Test 1 - Encoded: {encoded1}") # Output: 5#Hello5#World
    print(f"Test 1 - Decoded: {decoded1}")
    assert test1 == decoded1

    # Test Case 2: Strings containing the delimiter itself
    test2 = ["#", "##", "3#test"]
    encoded2 = codec.encode(test2)
    decoded2 = codec.decode(encoded2)
    print(f"\nTest 2 - Encoded: {encoded2}") # Output: 1##2###6#3#test
    print(f"Test 2 - Decoded: {decoded2}")
    assert test2 == decoded2
    
    # Test Case 3: Empty string and empty list
    test3 = [""]
    encoded3 = codec.encode(test3)
    decoded3 = codec.decode(encoded3)
    print(f"\nTest 3 - Encoded: {encoded3}") # Output: 0#
    print(f"Test 3 - Decoded: {decoded3}")
    assert test3 == decoded3

    print("\nAll test cases passed!")