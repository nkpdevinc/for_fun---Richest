class Solution(object):
    def __init__(self) -> None:
        pass


    def maximumWealth(self, accounts: list) -> int:
        richest=''
        sum_wealth = []
        max_wealth = 0
        for i in range(len(accounts)):
            wealth = sum(accounts[i])
            sum_wealth.append(f'Customer #{i+1}  has wealth = {wealth}  ')
            if wealth > max_wealth:
                max_wealth = wealth
                richest = i+1
            elif wealth == max_wealth:
                richest = str(richest) + f' and #{i+1}'
    
        print(f'Input: accounts = {accounts}')
        print(f'Output: customer #{richest} have {max_wealth}')
        print('Explanation:')
        for j in sum_wealth:
            print(j)

        return max_wealth


if __name__ == "__main__":
    accounts = [[21,3],[7,3],[3,5],[1,4],[22,2],[0,9],[12,12]]
    s = Solution()
    s.maximumWealth(accounts) 
    