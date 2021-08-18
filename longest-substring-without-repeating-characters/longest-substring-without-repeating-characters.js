/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
  let maxLength = 0;
  let temp = ''
  for(let i = 0; i < s.length; i++) {
    temp = temp.slice(temp.indexOf(s[i]) + 1)
    temp += s[i]
    
    if(maxLength < temp.length) maxLength = temp.length
  }
  return maxLength
};