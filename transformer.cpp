#include <iostream>
#include <string>

bool is_hangul(char32_t ch) {
    return ch >= U'\uAC00' && ch <= U'\uD7A3';
}

std::u32string transform_text(const std::u32string &text) {
    std::u32string result;

    for (char32_t ch : text) {
        if (!is_hangul(ch)) {
            result += ch;
        } else {
            int base = ch - U'\uAC00';
            int jongseong_base = base % 28;
            int jungseong_base = ((base - jongseong_base) / 28) % 21;
            int choseong_base = ((base - jongseong_base) / 28 - jungseong_base) / 21;

            if (jongseong_base == 0) {
                if (jungseong_base == 0 || jungseong_base == 2 || jungseong_base == 4 || jungseong_base == 6 || jungseong_base == 8 || jungseong_base == 12 || jungseong_base == 13 || jungseong_base == 17 || jungseong_base == 18 || jungseong_base == 20) {
                    jongseong_base = 8;
                } else {
                    jongseong_base = 17;
                }
            }

            char32_t transformed_char = U'\uAC00' + (choseong_base * 21 * 28) + (jungseong_base * 28) + jongseong_base;
            result += transformed_char;
        }
    }

    return result;
}

int main() {
    std::string input;
    std::cout << "Enter the text: ";
    std::getline(std::cin, input);

    std::u32string input32 = std::wstring_convert<std::codecvt_utf8<char32_t>, char32_t>{}.from_bytes(input);
    std::u32string output32 = transform_text(input32);
    std::string output = std::wstring_convert<std::codecvt_utf8<char32_t>, char32_t>{}.to_bytes(output32);

    std::cout << "Transformed text: " << output << std::endl;

    return 0;
}
