// https://leetcode.com/problems/sliding-window-maximum/description/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
    if (nums.length == 0 || k == 0) return [];
    let deque = [];
    let result = [];

    for (let i = 0; i < nums.length; i++) {
        // Remove indices that are out of the current window
        while (deque.length && deque[0] < i - k + 1) {
            deque.shift();
        }

        // Remove from deque indices of all elements smaller than the current element
        while (deque.length && nums[deque[deque.length - 1]] < nums[i]) {
            deque.pop();
        }

        // Add current element index to the deque
        deque.push(i);

        // The front of the deque is the max of the current window
        if (i >= k - 1) {
            result.push(nums[deque[0]]);
        }
    }

    return result;
}
