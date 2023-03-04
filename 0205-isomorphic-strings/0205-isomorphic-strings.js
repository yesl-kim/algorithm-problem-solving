/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const convert = (s) => {
  const map = new Map()
  let count = 1
  let temp = ''
  for (let i = 0; i < s.length; i++) {
    if(map.has(s[i])) {
      temp += map.get(s[i])
    } else {
      map.set(s[i], count)
      temp += count
      count++
    }
  }
  
  return temp
}

const isIsomorphic = (s, t) => {
  return convert(s) === convert(t)
};