​### best practice

```javascript
var maxProfit = function (prices) {
  let left = 0;
  let right = 1;
  let maxProfit = 0;

  while (right < prices.length) {
    const buy = prices[left];
    const sell = prices[right];
    const profit = sell - buy;
    if (profit > 0) {
      maxProfit = Math.math(profit, maxProfit);
    } else {
      left = right;
    }
    right++;
  }

  return maxProfit;
};
```

- 수익이 나지 않았을 때, 즉 buy > sell 인 경우 left 가 right의 위치로 오면 된다. **left를 하나 증가시키는 것이 아니라**
- left 는 right보다 무조건 왼쪽에 있어야 하고
- buy는 right의 왼쪽에 있는 값 중에서 가장 최솟값이어야 하기 때문에
