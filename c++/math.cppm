export module math;

import std;

export namespace math {
    constexpr double pi = 3.14159265358979323846;

    int square(int x) {
        return x * x;
    }

    template<typename T>
    T clamp(T value, T lo, T hi) {
        return std::max(lo, std::min(hi, value));
    }
}
