#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> data, string ext, int val_ext, string sort_by) {
    vector<vector<int>> answer;
    int row = 0;
    
    // 필터 기준
    if(ext == "code") row = 0;
    else if(ext == "date") row = 1;
    else if(ext == "maximum") row = 2;
    else if(ext == "remain") row = 3;
    
    for(int i = 0; i < data.size(); i++){
        if(data[i][row] < val_ext){
            answer.push_back(data[i]);
        }  
    }

    if(sort_by == "code") row = 0;
    else if(sort_by == "date") row = 1;
    else if(sort_by == "maximum") row = 2;
    else if(sort_by == "remain") row = 3;

    sort(answer.begin(), answer.end(), [row](const vector<int>& a, const vector<int>& b) {
        return a[row] < b[row];
    });
    
    return answer;
}