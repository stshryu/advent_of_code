#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "md5.cpp"

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

int find_zero(string key) {
    string subhash;
    int counter = 0;
    while(subhash != "00000") {
        counter++;
        subhash = MD5(key + to_string(counter)).hexdigest().substr(0,5);
    }

    return counter;
}

int main() {
    string data = read_file()[0];

    cout << find_zero(data) << '\n';

    return 0;
}
