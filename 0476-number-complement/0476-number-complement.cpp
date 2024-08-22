class Solution {
public:
    int findComplement(int num) {
        int power=0,ans=0;
        while(num){
            int unit=num&1;
            if(unit==0)
                ans+=pow(2,power);
            num>>=1;
            power++;
        }
        return ans;
    }
};