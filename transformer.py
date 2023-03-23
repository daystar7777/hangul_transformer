import re

def is_hangul(char):
    return re.match(u'[\uAC00-\uD7A3]', char) is not None

def decompose_char(char):
    base = ord(char) - 44032
    jongseong_base = base % 28
    jungseong_base = ((base - jongseong_base) // 28) % 21
    choseong_base = (((base - jongseong_base) // 28) - jungseong_base) // 21
    return choseong_base, jungseong_base, jongseong_base

def compose_char(choseong_base, jungseong_base, jongseong_base):
    return chr(44032 + (choseong_base * 21 * 28) + (jungseong_base * 28) + jongseong_base)

def transform_text(text):
    choseong_list = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
    jungseong_list = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
    jongseong_list = [""] + list("ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ")

    def transform_char(char):
        if not is_hangul(char):
            return char
        else:
            choseong_base, jungseong_base, jongseong_base = decompose_char(char)
            
            # 받침이 있는 경우 변환하지 않음
            if jongseong_base != 0:
                return char
            
            jongseong_base = jongseong_list.index('ㅀ')

            return compose_char(choseong_base, jungseong_base, jongseong_base)

    return ''.join(map(transform_char, text))

