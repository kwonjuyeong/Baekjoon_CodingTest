#include <string>
#include <vector>

using namespace std;

string solution(string s, string skip, int index) {
    string answer = "";
    
    string alphabet = "abcdefghijklmnopqrstuvwxyz"; 
    string skipped = "";

    for(char c : alphabet) {
        if(skip.find(c) == string::npos) {
            skipped += c;
        }
    }
        
    for(int i = 0; i < s.length(); i ++){
            
        int pos = skipped.find(s[i]);
        char next = skipped[(pos + index) % skipped.size()];
        answer += next;
    }
    
    
    return answer;
}