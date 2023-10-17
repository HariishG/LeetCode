class Solution {
public:
    int fib(int n) {
        int a=0, b=1, t;
        for(int i=0; i<n; i++){
            t=b;
            b=a+b;
            a=t;
        }
        return a;
    }
};