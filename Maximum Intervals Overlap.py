'''Consider a big party where N guests came to it and a log register for guest’s entry and exit times was maintained. 
Find the minimum time at which there were maximum guests at the party. Note that entries in the register are not in any order.
Note: Guests are leaving after the exit times. '''


class Solution{
	public int[] findMaxGuests(int[] arrl, int[] exit, int n) {
        Arrays.sort(arrl);
        Arrays.sort(exit);
        int guests_in = 1, max_guests = 1, time = arrl[0];
        int i = 1, j = 0;
        while (i < n && j < n){
            if (arrl[i] <= exit[j]){
                guests_in++;
            if (guests_in > max_guests){
                max_guests = guests_in;
                time = arrl[i];
            }
                i++;
            }
            else{ 
            guests_in--;
            j++;
            }
        }
    
        return new int[]{max_guests,time};
	}
}
