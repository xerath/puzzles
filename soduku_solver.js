// Leetcode Sudoku challenge: https://leetcode.com/problems/sudoku-solver/description/
// Requires resursive guessing/backtracking algo


function solveSudoku(board) {
    if (!board || board.length === 0) return
    solve(board)
}

function solve(board) {
    for (let row = 0; row < board.length; row++) {
        for (let col = 0; col < board[row].length; col++) {
            if (board[row][col] === '.') {
                for (let num = 1; num <= 9; num++) {
                    if (isValid(board, row, col, num.toString())) {
                        board[row][col] = num.toString()
                        if (solve(board)) return true; // If solved, return true
                        board[row][col] = '.'; // Otherwise backtrack
                    }
                }
                return false // Trigger backtracking
            }
        }
    }
    return true // Return true if all cells are checked
}

function isValid(board, row, col, num) {
    for (let i = 0; i < 9; i++) {
        if (board[row][i] === num) return false; // If the number already exists in the row, it's invalid.
        if (board[i][col] === num) return false; // If the number already exists in the column, it's invalid.
        const startRow = 3 * Math.floor(row / 3); // Determines the starting row of the sub-grid
        const startCol = 3 * Math.floor(col / 3); // Determines the starting column of the sub-grid
        for (let gridRow = startRow; gridRow < startRow + 3; gridRow++) {
            for (let gridCol = startCol; gridCol < startCol + 3; gridCol++) {
                if (board[gridRow][gridCol] === num) return false // If the number exists in the 3x3 sub-grid, it's invalid.
            }
        }
    }
    return true // If none of the checks fail, the number placement is valid.
}
