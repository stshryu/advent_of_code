#include <iostream>
#include <fstream>
#include <string>
#include <map>
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

int visited_houses(string directions) {
    map<vector<int>, int> visits {{{0,0}, 1}}; 
    vector<int> pos {0, 0};
    for (char c: directions) {
        switch (c) {
            case '>':
                pos[0]++;
                break;
            case '<': 
                pos[0]--;
                break;
            case '^':
                pos[1]++;
                break;
            case 'v':
                pos[1]--;
                break;
        } 

        if (auto res = visits.find(pos); res != visits.end()) {
            int val = res->second;
            visits[pos] = val++;
        } else {
            visits[pos] = 1;
        }
    }

    return visits.size();
}

int main() {
    vector<string> data = read_file();

    cout << visited_houses(data[0]) << '\n';

    return 0;
}
