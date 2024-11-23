'''Consider a big party where N guests came to it and a log register for guest’s entry and exit times was maintained. 
Find the minimum time at which there were maximum guests at the party. Note that entries in the register are not in any order.
Note: Guests are leaving after the exit times. '''

class Solution:
    def findMaxGuests(self, Entry, Exit, N):
        start = min(Entry)
        end = max(Exit)
        time = [0]*(end-start+2)
        res_t = cur_t = 0
        res_g = cur_g = 0
        for s, e in zip(Entry, Exit):
            s-=start
            e -=start
            time[s] +=1
            time[e+1] -=1
        for t, g in enumerate(time):
            t+=start
            cur_g += g
            if cur_g > res_g:
                res_g = cur_g
                res_t = t
        return [res_g, res_t]
