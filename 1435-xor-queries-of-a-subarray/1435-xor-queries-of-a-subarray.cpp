class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int> ans, preList;
        preList.push_back(0);
        for(int i=0; i<arr.size(); i++){
            preList.push_back(preList[i]^arr[i]);
        }
        for(int i=0; i<queries.size(); i++){
            ans.push_back(preList[queries[i][1]+1]^preList[queries[i][0]]);
        }
        return ans;
    }
};