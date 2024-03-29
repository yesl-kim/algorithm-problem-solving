/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    // t의 문자열을 순회하며
    // s에 포함되는 것만 순서대로 복제한다 (temp)
    // temp와 s가 같으면 true 아니면 false
    
    //     let temp = ''
    
//     for (let i = 0; i < t.length; i++) {
//         if (!s.includes(t[i])) {
//             continue
//         } else {
//             temp += t[i]
//         }
//     }
    
//     return temp === s
    
    // 그런데 그러면- t 문자열을 모두 순회해야함
    // 1. s 보다 t 의 길이가 압도적으로 더 크고
    // 2. 무조건 (빨리 검사가 끝날 수 있어도) t 문자를 모두 순회해야한다

    // => s를 기준으로 답을 찾는다면?
    // t를 temp에 복제
    // s를 순회하면서
    // s[i]가 temp에 포함되어 있는지 확인. => 아니면 바로 false 반환
    
    // 포함되어 있다면 
    // 해당 idx기준 뒤의 자리 문자열만 잘라서 temp에 저장
    
    let temp = t
    
    if(s.length < 1) return true
    if(s.length > t.length) return false
    
    for (let i = 0; i < s.length; i++) {
        if(temp.length <= 0) return false
        const idx = temp.indexOf(s[i])
        if(idx < 0) return false
        temp = temp.slice(idx + 1)
    }
    
    return true
    
};