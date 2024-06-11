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

int find_floor(vector<string> dirs) {
    int current_floor = 0;

    for (string directions: dirs) {
        for (char direction : directions) {
            if (direction == '(') {
                current_floor++;
            } else {
                current_floor--;
            }
        } 
    }
    return current_floor;
}
int main(){
    vector<string> dirs = read_file();

    cout << find_floor(dirs) << '\n';

    return 0;
}
