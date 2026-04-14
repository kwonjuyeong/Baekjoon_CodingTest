#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 1;
    sort(nums.begin(), nums.end());
    int current = nums[0];
    
    for(int i = 0; i<nums.size(); i++){
        if(nums.size()/2 <= answer){
            return answer;            
        }
        
        if(nums[i] != current){
            current = nums[i];
            answer++;
        }
    }
    return answer;
}