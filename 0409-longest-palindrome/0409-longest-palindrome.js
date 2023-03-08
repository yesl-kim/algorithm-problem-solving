/**
 * @param {string} s
 * @return {number}
 */
const longestPalindrome = (s) => {
  const ss = s.split('')
  let odd = false
  let res = 0
  
  const m = ss.reduce((acc, cur) => {
    if(acc.has(cur)) {
      acc.set(cur, acc.get(cur) + 1)
    } else {
      acc.set(cur, 1)
    }
    return acc
  }, new Map())
  
  for(const l of m.values()) {
    let value = l
    if(l % 2 === 1) {
      odd = true
      value = l - 1
    }
    res += value
  }
  
  if(odd) return res + 1
  return res
}