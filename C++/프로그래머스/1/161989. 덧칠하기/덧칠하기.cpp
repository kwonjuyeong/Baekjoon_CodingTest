#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(int n, int m, vector<int> section) {
    int answer = 0;
    unordered_map<int, int> map;    //칠해진 범위
    
    //i = 총 벽의 범위
    //for(int i = 0; i < n; i++){
        //section에 있는 값이 전부 칠해져야함.
        for(int j = 0; j < section.size(); j++){
            if(map[section[j]] > 0){    //0 이상이면 이미 한번 칠해진 것
                continue;   //다음 범위로 넘어감
            }else{  //아직 칠해지지 않은 범위라면
                for(int k = 0; k < m; k++){
                    map[section[j]+k]++;    //해당 값부터 m만큼 칠함
                }
                answer ++;                  //칠했으니까 값 ++
            }    
        }   
    //}
    return answer;
}