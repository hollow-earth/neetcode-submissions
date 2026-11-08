class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        vector<int> c_array(26, 0);
        for (int i = 0; i < s.size(); i++) {
            c_array[int(s[i])-97] += 1;
            c_array[int(t[i])-97] -= 1;
        }
        for (int i: c_array) {
            if (i != 0) return false;
        }
        return true;
    }
};
