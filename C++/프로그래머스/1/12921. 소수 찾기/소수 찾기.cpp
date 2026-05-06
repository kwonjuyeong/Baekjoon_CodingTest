#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int number[n];
    
    for(int i=2;i<=n;i++) {
        number[i] = i;
    }

    for(int i=2;i<=n;i++) {
        if(number[i]==0)
            continue;

        for(int j=2*i; j<=n; j+=i) {
            number[j] = 0;
        }
    }

    for(int i=2;i<=n;i++) {
        if(number[i]!=0){
            answer++;
        }
    }
    
    return answer;
}