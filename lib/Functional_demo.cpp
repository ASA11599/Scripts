#include "Functional.hpp"
#include <vector>
#include <iostream>

class Square : public Functional::Function<int, int>
{
    public:
        int operator()(int x) override
        {
            return x*x;
        }
};

class Even : public Functional::Function<bool, int>
{
    public:
        bool operator()(int x) override
        {
            return x%2 == 0;
        }
};

template <typename T>
void printVector(std::vector<T>& v)
{
    std::cout << "{ ";
    for (int i = 0 ; i < v.size() ; i++) {
        if (i == v.size() - 1) std::cout << v.at(i) << " ";
        else std::cout << v.at(i) << ", ";
    }
    std::cout << "}" << std::endl;
}

int main(void)
{
    std::vector<int> data;
    Square squareFunction;
    Even evenFunction;
    for (int i = 0 ; i < 10 ; i++) {
      data.push_back(i);
    }
    std::vector<int> squares = Functional::map(squareFunction, data);
    std::vector<int> evens = Functional::filter(evenFunction, data);
    printVector<int>(squares);
    printVector<int>(evens);
    return 0;
}