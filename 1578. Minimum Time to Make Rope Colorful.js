/**
 * @param {string} colors
 * @param {number[]} neededTime
 * @return {number}
 */
 var minCost = function(colors, neededTime) {
    let minTime = 0
    let cur = 0
    for(let i = 0 ; i<neededTime.length; i++) {
        if(i>0 && colors[i]!==colors[i-1]) {
            cur = 0
        }
        minTime += Math.min(cur,neededTime[i])
        cur = Math.max(cur,neededTime[i])
    }

    return minTime
};



// Runtime: 169 ms, faster than 47.68% of JavaScript online submissions for Minimum Time to Make Rope Colorful.
// Memory Usage: 52.5 MB, less than 76.34% of JavaScript online submissions for Minimum Time to Make Rope Colorful.
