/*
Naive Backtracking
The naive or brute force approach will be to try every possible configuration of numbers from 1 to 9 for each of the empty cells. After filling all the empty cells in the matrix, we check that the matrix is a valid sudoku solution or not. If we don’t find it valid, we keep checking it for the next configurations recursively until we find one.

Time Complexity
O(9^K),  Where ‘K’ is the number of empty cells in the given 2d matrix.

 

As we are trying all the numbers from 1 to 9 for every empty cell, our time complexity is exponential and quite high.

Space Complexity
O(1), i.e., constant space complexity.

 

In the worst-case scenario, our recursion stack can grow maximum till size 9*9 = 81, which is constant.
*/




/*
    Time Complexity - O(9^K)
    Space Complexity - O(1)

    where K is the number of empty cells in the sudoku.
*/

#include <map>

// Function to check if the current sudoku array is valid or not.
bool isSudokuValid(vector<vector<int>> &sudoku)
{
    map<int, bool> row[9], col[9];
    map<int, bool> subGrid[3][3];

    for (int r = 0; r < 9; r++)
    {
        for (int c = 0; c < 9; c++)
        {
            if (sudoku[r][c] == 0)
            {
                continue;
            }

            // If the current value of sudoku was present in the current column, row, and subgrid previously, return false.
            if (subGrid[r / 3][c / 3][sudoku[r][c]] || col[c][sudoku[r][c]] || row[r][sudoku[r][c]])
            {
                return false;
            }

            // Mark the current value of sudoku as true in the current column, row, and subgrid.
            subGrid[r / 3][c / 3][sudoku[r][c]] = true;
            row[r][sudoku[r][c]] = true;
            col[c][sudoku[r][c]] = true;
        }
    }
    return true;
}

// Function to try all the possible ways to solve the sudoku.
bool bruteForce(vector<vector<int>> &sudoku, int i, int j)
{
    if (j == 9)
    {
        if (i == 8)
        {
            if (isSudokuValid(sudoku))
            {
                return true;
            }
            return false;
        }

        j = 0;
        i++;
    }

    if (sudoku[i][j] != 0)
    {
        return bruteForce(sudoku, i, j + 1);
    }

    // Try all the values possible.
    for (int put = 1; put <= 9; put++)
    {

        sudoku[i][j] = put;

        if (bruteForce(sudoku, i, j + 1))
        {
            return true;
        }

        sudoku[i][j] = 0;
    }
    return false;
}

void solveSudoku(vector<vector<int>> &sudoku)
{
    bruteForce(sudoku, 0, 0);
    return;
}