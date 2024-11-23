'''There are ‘N’ people at a party. Each person has been assigned a unique id between 0 to 'N' - 1(both inclusive). A celebrity is a person who is known to everyone but does not know anyone at the party.

Given a helper function ‘knows(A, B)’, It will returns "true" if the person having id ‘A’ know the person having id ‘B’ in the party, "false" otherwise. Your task is to find out the celebrity at the party. Print the id of the celebrity, if there is no celebrity at the party then print -1.

Note:
1. The helper function ‘knows’ is already implemented for you.
2. ‘knows(A, B)’ returns "false", if A doesn't know B.
3. You should not implement helper function ‘knows’, or speculate about its implementation.
4. You should minimize the number of calls to function ‘knows(A, B)’.
5. There are at least 2 people at the party.
6. At most one celebrity will exist.'''

class CelebrityProblem:
    # Helper function knows(A, B) is assumed to be implemented
    def knows(self, A, B):
        # Implementation not shown
        return True  # Placeholder

    def findCelebrity(self, n):
        candidate = 0
        for i in range(1, n):
            if self.knows(candidate, i):
                candidate = i

        for i in range(n):
            if i != candidate and (self.knows(candidate, i) or not self.knows(i, candidate)):
                return -1

        return candidate

# Example usage
if __name__ == "__main__":
    solution = CelebrityProblem()
    n = 4  # Number of people at the party
    celebrity = solution.findCelebrity(n)
    print("Celebrity ID:", celebrity)
