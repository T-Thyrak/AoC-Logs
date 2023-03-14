#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <chrono>

using std::cout, std::endl;

int main() {
    std::fstream file("section.txt");
    std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>> sections;
    std::string line;

    auto before_setup = std::chrono::high_resolution_clock::now();

    while (std::getline(file, line)) {
        // split by comma
        auto comma = line.find(',');
        auto sec1 = line.substr(0, comma);
        auto sec2 = line.substr(comma + 1);

        // split by dash
        auto dash = sec1.find('-');
        auto sec1_1 = sec1.substr(0, dash);
        auto sec1_2 = sec1.substr(dash + 1);

        dash = sec2.find('-');
        auto sec2_1 = sec2.substr(0, dash);
        auto sec2_2 = sec2.substr(dash + 1);

        sections.push_back({{std::stoi(sec1_1), std::stoi(sec1_2)}, {std::stoi(sec2_1), std::stoi(sec2_2)}});
    }

    auto start = std::chrono::high_resolution_clock::now();

    int count_full_overlap = 0;
    for (auto& section: sections) {
        auto& sec1 = section.first;
        auto& sec2 = section.second;

        if ((sec1.first <= sec2.first && sec1.second >= sec2.second) ||
            (sec2.first <= sec1.first && sec2.second >= sec1.second)) {
            count_full_overlap++;
        }
    }

    auto part_1 = std::chrono::high_resolution_clock::now();

    int count_partial_overlap = 0;
    for (auto& section: sections) {
        auto& sec1 = section.first;
        auto& sec2 = section.second;

        if ((sec1.first <= sec2.first && sec1.second >= sec2.first) ||
            (sec2.first <= sec1.first && sec2.second >= sec1.first)) {
            count_partial_overlap++;
        }
    }

    auto part_2 = std::chrono::high_resolution_clock::now();

    cout << "Answer to part 1: " << count_full_overlap << endl;
    cout << "Answer to part 2: " << count_partial_overlap << endl;

    cout << "Setup took: " << std::chrono::duration_cast<std::chrono::nanoseconds>(start - before_setup).count() << "ms" << endl;

    cout << "Part 1 took " << std::chrono::duration_cast<std::chrono::nanoseconds>(part_1 - start).count() << "ns" << endl;
    cout << "Part 2 took " << std::chrono::duration_cast<std::chrono::nanoseconds>(part_2 - part_1).count() << "ns" << endl;

    return 0;
}