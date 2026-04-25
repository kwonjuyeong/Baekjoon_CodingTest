#include <string>
#include <vector>

using namespace std;

vector<int> solution(int num, int total) {
    vector<int> answer;
    double middle = 0;
    double middle2 = 0;
    if(num % 2 == 1){
        middle = total / num;
    for(int i = middle - ((num-1)/2); i <= middle + ((num-1)/2); i++){
        answer.push_back(i);
    } 
    }else{
        middle = total / num;
        for(int i = middle - ((num-1)/2); i <= middle + ((num-1)/2)+1; i++){
        answer.push_back(i);
    } 
    }
    

    
    return answer;
}