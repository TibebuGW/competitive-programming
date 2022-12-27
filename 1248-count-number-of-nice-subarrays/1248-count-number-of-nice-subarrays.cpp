class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        /*
            i need to know where it doesn't start the violation
            // if i am starting here
            // i need to know the position of odds that i have counted
            this means whenever i am poping a q i know my next index that i am not violating
        */
        for (auto &x: nums) {
            x &= 1;
        }
        int last = 0;
        int r = 0;
        int l = 0;
        int ans = 0;
        int cnt = 0;
        while (r < nums.size()) {
            if(nums[r]) {
                cnt++;
            }
            r++;
            while(cnt > k) {
                if(nums[l]) {
                    cnt--;
                }
                l++;
                last = l;
            }
            while(nums[last] == 0) {
                last++;
            }
            
            if(cnt == k) {
                ans += (last - l) + 1;
            }
        }
        return ans;
    }
};