/*
approch 2 
optimized backtracking
Backtracking is a general algorithm for finding all (or some) solutions to a problem that incrementally builds candidates to the solution. As soon as it determines that a candidate can not possibly be the solution to the problem, it abandons it (“backtracks”). We can solve this problem using backtracking. 

Before we assign a number in an empty cell, we will check whether it is safe to assign. We will have an ‘isSafe’ function for it, which will check that the same number is not present in the current row, current column, and in the current sub-grid.
If it is safe to assign the number, we will assign it to the empty cell and recursively check whether this assignment leads to a solution or not.
If this assignment doesn’t lead to a solution, then we will try the next number for the current empty cell. And if none of the numbers from 1 to 9 leads to a solution, we will return false.
Time Complexity
O(9^K),  Where ‘K’ is the number of empty cells in the given 2d matrix.

 

The time complexity remains the same, but there will be some early pruning, so the time taken will be much less than the naive algorithm, but the upper bound time complexity remains the same.

Space Complexity
O(1), i.e., constant space complexity.

 

In the worst-case scenario, our recursion stack can grow maximum till size 9*9 = 81, which is constant.
*/
/*
    Time Complexity - O(9^K)
    Space Complexity - O(1)

    where K is the number of empty cells in the sudoku.
*/

// Function to check whether we can put a particular value
// to a particular position or not.
bool canPut(vector<vector<int>> &sudoku, int row, int col, int num)
{
    for (int i = 0; i < 9; i++)
    {
        if (sudoku[i][col] == num || sudoku[row][i] == num)
        {
            return false;
        }
        if (sudoku[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == num)
        {
            return false;
        }
    }

    return true;
}

// Function to check all the valid way to solve the sudoku.
bool backTrack(vector<vector<int>> &sudoku, int i, int j)
{
    if (j == 9)
    {
        if (i == 8)
        {
            return true;
        }

        j = 0;
        i++;
    }

    if (sudoku[i][j] != 0)
    {
        return backTrack(sudoku, i, j + 1);
    }

    // Trying all possible values.
    for (int put = 1; put <= 9; put++)
    {
        if (canPut(sudoku, i, j, put))
        {
            sudoku[i][j] = put;

            if (backTrack(sudoku, i, j + 1))
            {
                return true;
            }

            sudoku[i][j] = 0;
        }
    }

    return false;
}

void solveSudoku(vector<vector<int>> &sudoku)
{
    backTrack(sudoku, 0, 0);
    return;
}