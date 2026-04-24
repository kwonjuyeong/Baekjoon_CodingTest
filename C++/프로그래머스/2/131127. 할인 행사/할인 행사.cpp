#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    
    unordered_map<string, int> target;
    unordered_map<string, int> items;
    
    for(int i = 0; i < want.size(); i++){
        target[want[i]] = number[i];
    }  
    
    for (int i = 0; i <= discount.size() - 10; i++)
    {
        if(i == 0){
            for(int j = 0; j < 10; j++){
               items[discount[j]]++;            
            }
        }
        else{
            items[discount[i-1]]--;
            if (items[discount[i-1]] == 0) {
                items.erase(discount[i-1]);
            }
            
            items[discount[i+9]]++;
        }
        
        if(target == items)
            answer++;
    }
         
    return answer;
}