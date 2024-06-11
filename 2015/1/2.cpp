#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<string> read_file() {
    string filename = "input.txt";
    vector<string> data;

    string line;
    ifstream file(filename);
    if (file.is_open()) {
        while(getline(file, line)) {
            data.push_back(line);
        }
    }
    return data;
}

tuple<int, int> find_floor(vector<string> dirs) {
    int current_floor = 0;
    int current_index = 0;
    int final_index = 0;
    int flag = 0;

    for (string directions: dirs) {
        for (char direction : directions) {
            if (direction == '(') {
                current_floor++;
                current_index++;
            } else {
                current_floor--;
                current_index++;
            }
            if (current_floor < 0 && flag != 1) {
                final_index = current_index;
                flag = 1;
            }
        } 
    }
    return {current_floor, final_index}; 
}
int main(){
    vector<string> dirs = read_file();
    tuple<int, int> result = find_floor(dirs);
    cout << get<0>(result) << '\n';
    cout << get<1>(result) << '\n';

    return 0;
}
