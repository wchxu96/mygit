//
// Created by hp on 2016/7/16.
//

//登一个梯子有n层，每次只能上一层或两层有多少种方法
#include <iostream>
//http://www.csie.ntnu.edu.tw/~u91029/DynamicProgramming.html

/*直接用遞迴實作，而不使用記憶體儲存各個問題的答案，是最直接的方式，也是最慢的方式。
時間複雜度是 O(f(n)) 。
問題一而再、再而三的出現，不斷呼叫同樣的函式求解，效率不彰。剛接觸 DP 的新手常犯這種錯誤。
*/
/*int f(int n)
{
    if (n == 0 || n == 1)
    {
        return 1;
    }
    else
    {
        return f(n-1) + f(n-2);
    }


}
 */

//正确的DP：Top-dowm/buttom-up
int table[6];
bool solve[6];

int f(int n)
{
    //[initial]
    if(n == 0 || n== 1) return table[n] = 1;
    //[Compute]
    //如果已经计算过就直接取表格里的答案
    if(solve[n]) return table[n];
    //如果不曾计算过，就计算一边，存储答案
    table[n] = f(n-1)+f(n-2);
    solve[n] = true;
    return table[n];
}
void stairs_climbing()
{
    for (int i = 0;i<=5;i++)
    {
        solve[i] = false;
    }
    int n;
    while(std::cin >> n && (n >= 0&&n<=5))
    {
        std::cout << "爬到第" << n << "层有" << f(n) <<"种方法" <<std::endl;
    }
}

int main()
{
    stairs_climbing();
}

/*
    int table[6];
    table[0] = 1;
    table[1] = 1;
    for(i = 2;i<=5;i++)
    {
       table[i] = table[i-1]+table[i-2];
    }

*/

dp[i][j] = min(k + max(dp[i][k - 1], dp[k + 1][j]))
