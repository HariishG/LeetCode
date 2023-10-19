class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        vector<int> vect(pref.size()); 
        vect[0]=pref[0];
        for(int i=1;i<pref.size();i++){
            vect[i]=pref[i-1]^pref[i];
        }
        return vect;
    }
};