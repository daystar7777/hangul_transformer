function isHangul(char) {
    const unicode = char.charCodeAt(0);
    return 0xAC00 <= unicode && unicode <= 0xD7A3;
}

function decomposeChar(char) {
    const base = char.charCodeAt(0) - 0xAC00;
    const jongseongBase = base % 28;
    const jungseongBase = ((base - jongseongBase) / 28) % 21;
    const choseongBase = (((base - jongseongBase) / 28) - jungseongBase) / 21;
    return [choseongBase, jungseongBase, jongseongBase];
}

function composeChar(choseongBase, jungseongBase, jongseongBase) {
    return String.fromCharCode(0xAC00 + (choseongBase * 21 * 28) + (jungseongBase * 28) + jongseongBase);
}

function transformText(text) {
    const jungseongList = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ";
    const jongseongList = ["", ..."ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"];

    return text.split('').map(char => {
        if (!isHangul(char)) {
            return char;
        } else {
            const [choseongBase, jungseongBase, jongseongBase] = decomposeChar(char);
            
            if (jongseongBase !== 0) {
                return char;
            }
            
            if (jungseongList[jungseongBase].match(/[ㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣ]/)) {
                return composeChar(choseongBase, jungseongBase, jongseongList.indexOf('ㄹ'));
            } else {
                return composeChar(choseongBase, jungseongBase, jongseongList.indexOf('ㅀ'));
            }
        }
    }).join('');
}
