#include <string>
#include <vector>

using namespace std;

int solution(vector<string> babbling) {
    int answer = 0;
    vector<string> words = {"aya", "ye", "woo", "ma"};
    
    for (int i = 0; i < babbling.size(); i++) {

        string prev = "";
        bool isValid = true;
        
        for (int j = 0; j < babbling[i].size();) {
            bool matched = false;
            
            for (int k = 0; k < words.size(); k++) {
                if (babbling[i].substr(j, words[k].size()) == words[k] && prev != words[k]) {
                    prev =  words[k];
                    j +=  words[k].size();
                    matched = true;
                    break;
                }
            }
            
            if (!matched) {
                isValid = false;
                break;
            }
        }
        
        if (isValid) answer++;
    }
    
    return answer;
}