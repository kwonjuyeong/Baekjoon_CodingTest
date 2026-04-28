#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<vector<int>> lines) {
    int answer = 0;
    unordered_map<int, int> m;
    
    for(int i = 0; i < lines.size(); i++){
        for(int j = lines[i][0]; j < lines[i][1]; j++){
            m[j]++;
        } 
    }
    
    for(unordered_map<int, int>::iterator it = m.begin(); it != m.end(); ++it){
        if(it->second > 1){
            answer++;
        }
    }
    
    return answer;
}