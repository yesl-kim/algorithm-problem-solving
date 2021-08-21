/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    const hash = {}
    for(let i = 0; i<nums.length; i++) {
      if(!hash[nums[i]]) hash[nums[i]] = 1
      else delete hash[nums[i]]
    }
  return Number(Object.keys(hash)[0])
};