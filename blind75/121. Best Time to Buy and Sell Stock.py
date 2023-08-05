class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lwst_price,hist_price = prices[0],0
        topPrices=[]
        for price in prices:
            if price <= lwst_price:
                lwst_price = price
                hist_price = 0 
                continue 
            if price > hist_price:
                hist_price = price
            if hist_price:
                topPrices.append(hist_price-lwst_price)
            print(f'price {price}, lwst {lwst_price}, highest {hist_price}')
            print(f'My topPrices are {topPrices}')
        if max(topPrices):
            return (max(topPrices))
        
        return 0 # if there's no price greater than the lowest


s = Solution
print(s.maxProfit(s,[2,4,100,1,3,200,6000]))



# very great work by me , covers all the cases :))))))))))))))))) So proud of me so certain it will pay very will in the future, a brick in my 160,000$++ a year journey 