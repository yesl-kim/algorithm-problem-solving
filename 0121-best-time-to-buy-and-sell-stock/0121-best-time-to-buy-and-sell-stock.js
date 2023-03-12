/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
   let left = 0
    let right = 1
    let maxProfit = 0
    
    while(right < prices.length) {
      const buy = prices[left]
      const sell = prices[right]
      const profit = sell - buy
      if(profit > 0) {
        maxProfit = profit > maxProfit ? profit : maxProfit
        right += 1
      } else {
        left += 1
        right = left + 1
      }
    }
  
  return maxProfit
};