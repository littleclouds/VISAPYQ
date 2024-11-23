/* Consider a big party where N guests came to it and a log register for guest’s entry and exit times was maintained. 
Find the minimum time at which there were maximum guests at the party. 
Note that entries in the register are not in any order.
Note: Guests are leaving after the exit times. */

//User function Template for Java

class Solution
{
	public int[] findMaxGuests(int[] Entry,int Exit[], int N){
        // add code here.
        TreeMap<Integer,Integer> sweep = new TreeMap<>();
        for(int i=0;i<N;i++){
            sweep.put(Entry[i],sweep.getOrDefault(Entry[i],0)+1);
            sweep.put(Exit[i]+1,sweep.getOrDefault(Exit[i]+1,0)-1);
        }
        int cnt = 0;int mx=0; int time =0;
        for(int x:sweep.keySet()){
            cnt+= sweep.get(x);//at present time how many are active
            if(cnt>mx){
                mx = cnt;
                time = x;
            }
        }
        return new int[]{mx,time};
	}
}
