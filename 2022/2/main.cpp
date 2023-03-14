#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <chrono>

enum Hand {
    ROCK = 1,
    PAPER,
    SCISSORS
};

enum Status {
    LOSS,
    DRAW,
    WIN,
};

std::ostream &operator<<(std::ostream &os, Hand hand) {
    os << "Hand::";
    if (hand == Hand::ROCK) {
        os << "ROCK";
    } else if (hand == Hand::PAPER) {
        os << "PAPER";
    } else {
        os << "SCISSORS";
    }
    return os;
}

std::map<Hand, Hand> winning_hand = {
    {Hand::ROCK, Hand::SCISSORS},
    {Hand::PAPER, Hand::ROCK},
    {Hand::SCISSORS, Hand::PAPER}
};

int trueMod(int x, int n) {
    return ((n + (x%n)) % n);
}

Hand getWinningHand(Hand hand) {
    return Hand(trueMod(hand, 3) + 1);
}

Hand getLosingHand(Hand hand) {
    return Hand(trueMod((hand - 2), 3) + 1);
}

Status play(Hand me, Hand op) {
    if (me == op) {
        return Status::DRAW;
    } else if (winning_hand[me] == op) {
        return Status::WIN;
    } else {
        return Status::LOSS;
    }
}

Hand decode(std::string me_char, Hand op) {
    if (me_char == "X") {
        return getLosingHand(op);
    } else if (me_char == "Y") {
        return op;
    } else {
        return getWinningHand(op);
    }
}

std::map<std::string, Hand> assoc = {
    {"A", Hand::ROCK},
    {"B", Hand::PAPER},
    {"C", Hand::SCISSORS},
    {"X", Hand::ROCK},
    {"Y", Hand::PAPER},
    {"Z", Hand::SCISSORS},
};

int main() {    
    std::ifstream file("strat.txt");
    std::vector<std::pair<std::string, std::string>> strat_string;
    std::vector<std::pair<Hand, Hand>> strat_1;
    std::vector<std::pair<Hand, Hand>> strat_2;
    std::string line;
    int score = 0;
    int score2 = 0;

    auto start_part_1 = std::chrono::high_resolution_clock::now();
    while (std::getline(file, line)) {
        std::string op = line.substr(0, 1);
        std::string me = line.substr(2, 1);
        
        strat_string.push_back(std::make_pair(op, me));
        strat_1.push_back(std::make_pair(assoc[op], assoc[me]));
        strat_2.push_back(std::make_pair(assoc[op], decode(me, assoc[op])));
    }

    for (std::size_t i = 0; i < strat_1.size(); i++) {
        auto pair1 = strat_1[i];
        auto pair2 = strat_2[i];
              
        score += pair1.second + play(pair1.second, pair1.first) * 3;
        score2 += pair2.second + play(pair2.second, pair2.first) * 3;
    }

    auto stop_part_1 = std::chrono::high_resolution_clock::now();
    auto time = std::chrono::duration_cast<std::chrono::microseconds>(stop_part_1 - start_part_1);

    std::cout << "part 1: " << score << std::endl;
    std::cout << "part 2: " << score2 << std::endl;

    std::cout << "total took " << time.count() << " ms" << std::endl;
    
    return 0;
}