/* Anish is given a string S and has been asked to determine if the given string S contains two non-overlapping substrings "AB" and "BA" (the substrings can go in any order).

As a friend of Anish, your task is to return “True” if the string S contains two non-overlapping substrings "AB" and "BA" (the substrings can go in any order) otherwise return “False” (without quotes).

Example:-
The string “ABBA” has two non-overlapping substrings “AB” and “BA” respectively. So “True” will be printed(without quotes).*/

public class NonOverlappingSubstrings {
    public boolean hasNonOverlappingSubstrings(String s) {
        int n = s.length();
        boolean foundAB = false, foundBA = false;

        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) == 'A' && s.charAt(i + 1) == 'B') {
                if (foundBA) {
                    return true;
                }
                foundAB = true;
                i++;
            } else if (s.charAt(i) == 'B' && s.charAt(i + 1) == 'A') {
                if (foundAB) {
                    return true;
                }
                foundBA = true;
                i++;
            }
        }

        return false;
    }

    // Driver code
    public static void main(String[] args) {
        NonOverlappingSubstrings solution = new NonOverlappingSubstrings();
        String s = "ABBA";
        System.out.println(solution.hasNonOverlappingSubstrings(s)); // Output: true
    }
}
