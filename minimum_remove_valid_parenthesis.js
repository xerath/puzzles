// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

/**
 * @param {string} s
 * @return {string}
 */
var minRemoveToMakeValid = function(s) {
    let stack = []

    let arr = s.split('')
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] === '(') stack.push(i)
        if(arr[i] === ')') {
            if(stack.length > 0) stack.shift()
            else arr[i] = '|'
        }
    }

    // Mark any remaining open parenthesis
    for(let i = 0; i < stack.length; i++) arr[stack[i]] = '|'

    // Final cleanup
    let result = []
    for(let i = 0; i < arr.length; i++) if(arr[i] !== '|') result.push(arr[i])
    return result.join('')
}
