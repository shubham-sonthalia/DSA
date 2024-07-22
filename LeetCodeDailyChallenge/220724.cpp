// https://leetcode.com/problems/sort-the-people/

class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<tuple<int, string>> temp; 
        int n = names.size();
        for (int i = 0; i < n; i++){
            temp.push_back(make_tuple(heights[i], names[i]));
        }
        vector<string> descSortedNames;
        sort(temp.begin(), temp.end(), [](const auto& lhs, const auto& rhs){
            return std::get<0>(lhs) > std::get<0>(rhs);
        });
        for(const auto& entry : temp) {
            descSortedNames.push_back(std::get<1>(entry));
        }
        return descSortedNames;
    }
};
