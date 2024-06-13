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
    vector<int> dimensions;
    string substr;
    char delim = 'x';

    while(getline(ss, substr, delim)) {
        dimensions.push_back(stoi(substr));
    }

    int l = dimensions[0];
    int w = dimensions[1];
    int h = dimensions[2];

    vector<int> small2;

    int large = dimensions[0];
    int ignore_index = 0;
    for (int i=1; i<3; i++) {
        if (dimensions[i] > large) {
            large = dimensions[i];
            ignore_index = i;
        }
    }
    
    int results = 0;
    for (int i=0; i<3; i++) {
        if (i != ignore_index) {
            results += dimensions[i] * 2;
        }
    }

    results += l*w*h;
    return results;
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
