class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> st;
        int res = 0;
        
        for (auto &c : operations) {
            if (c == "C") {
                res -= st.top();
                st.pop(); 
            }
            else if (c == "+") {
                int _temp1 = st.top(); 
                st.pop();
                int _temp2 = st.top() + _temp1;
                st.push(_temp1);
                st.push(_temp2);
                res += _temp2;
            }
            else if (c == "D") {
                res += 2 * st.top();
                st.push(2 * st.top());
            }
            else {
                int _temp = std::stoi(c);
                st.push(static_cast<int>(_temp));
                res += _temp;
            }
        }
        return res;
    }
};