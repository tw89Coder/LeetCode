class Solution {
    public int strStr(String haystack, String needle) {
        // If needle is an empty string, return 0 as per problem definition
        if (needle.isEmpty()) {
            return 0;
        }
        // Use the indexOf method to find the first occurrence of needle in haystack
        return haystack.indexOf(needle);
    }
}
