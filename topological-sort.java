/* Given an adjacency list for a Directed Acyclic Graph (DAG) where adj[u] contains a list of all vertices v such that there exists a directed edge u -> v. Return topological sort for the given graph.
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.
Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be 1 else 0.
Constraints:
2  ≤  V  ≤  103
1  ≤  E  ≤  (V * (V - 1)) / 2 */

class Solution {
    // Function to return list containing vertices in Topological order.
    static ArrayList<Integer> topologicalSort(ArrayList<ArrayList<Integer>> adj) {
        // Your code here
        int v=adj.size();
        boolean[]vis=new boolean[v];
        Stack<Integer>stack=new Stack<>();
        for(int i=0;i<v;i++){
            if(!vis[i]){
                dfs(adj,i,vis,stack);
            }
        }
        ArrayList<Integer>result=new ArrayList<>();
        while(!stack.isEmpty()){
            result.add(stack.pop());
        }
        return result;
    }
    static void dfs(ArrayList<ArrayList<Integer>> adj,int node, boolean[]vis,Stack<Integer>stack){
        vis[node]=true;
        for(int neighbour:adj.get(node)){
            if(!vis[neighbour]){
                dfs(adj,neighbour,vis,stack);
            }
        }
        stack.push(node);
    }
}
