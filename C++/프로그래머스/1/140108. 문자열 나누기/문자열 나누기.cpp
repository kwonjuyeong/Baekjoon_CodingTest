#include <string>
using namespace std;

int solution(string s) {
    int answer = 0;

    char x = '\0';
    int now = 0, other = 0;

    for(int i = 0; i < s.length(); i++) {

        if(x == '\0') {
            x = s[i];
            now++;
        }
        else if(x == s[i]) {
            now++;
        }
        else {
            other++;
        }

        if(now == other) {
            answer++;
            x = '\0';
            now = 0;
            other = 0;
        }
    }

    if(now != 0 || other != 0) {
        answer++;
    }

    return answer;
}