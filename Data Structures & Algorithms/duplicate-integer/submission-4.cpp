class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hs;
        for (int i: nums) {
            if (hs.find(i) == hs.end()) hs.insert(i);
            else return true;
        }
        return false;
    }
};