#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
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

int calc_dimensions(string dimension) {
    stringstream ss(dimension);
    vector<int> d;
    string substr;
    char delim = 'x';

    while(getline(ss, substr, delim)) {
        if (d.empty()) {
            d.push_back(stoi(substr));
        } else {
            int last = d.back();
            if (last <= stoi(substr)) {
                d.push_back(stoi(substr));
            } else {
                d.insert(d.begin(), stoi(substr));
            }
        }
    }

    return 2*d[0] + 2*d[1] + d[0]*d[1]*d[2];
}

int find_dimensions(vector<string> dims) {
    int total_paper = 0;
    
    for (string dimensions: dims) {
        total_paper += calc_dimensions(dimensions);
    }

    return total_paper;
}

int main() {
    vector<string> data = read_file();

    int result = find_dimensions(data);

    cout << result << '\n';
    return 0;
}
