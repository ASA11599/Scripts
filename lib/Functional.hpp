#include <vector>

namespace Functional
{

    template <typename R, typename ... As>
    class Function
    {
        public:
            virtual R operator()(As ... args) = 0;
    };

    template <typename T>
    std::vector<T> map(Function<T, T>& f, std::vector<T>& v)
    {
        std::vector<T> result;
        for (int i = 0 ; i < v.size() ; i++) {
            result.push_back(f(v.at(i)));
        }
        return result;
    }

    template <typename T>
    std::vector<T> filter(Function<bool, T>& f, std::vector<T>& v)
    {
        std::vector<T> result;
        for (int i = 0 ; i < v.size() ; i++) {
            if (f(v.at(i))) result.push_back(v.at(i));
        }
        return result;
    }

}