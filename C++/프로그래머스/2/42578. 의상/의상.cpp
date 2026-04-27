#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string, int> items;

    for(int i = 0; i < clothes.size(); i++){
         items[clothes[i][1]]++;
    }
    
    for (unordered_map<string, int>::iterator it = items.begin(); it != items.end(); it++) {
        answer *= (it->second + 1);
    }
    
    
    return answer-1;
}