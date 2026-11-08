class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int loop_target;
        unordered_map<int,int> hm;

        for (int i = 0; i < nums.size(); i++) {
            loop_target = target - nums[i];
            if (hm.find(loop_target) != hm.end()) {
                return {hm[loop_target], i};
            }
            else {
                hm.insert({nums[i], i});
            }
        }     

    }
};
