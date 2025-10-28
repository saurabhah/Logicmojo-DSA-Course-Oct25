"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
nums = [1,1,1,2,2,3]
k = 2

def topKFrequent(nums,k):
    """
    O(n)
    """
    freq = [[] for i in range(len(nums)+1)]
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num,0)

    for key, value in count.items():
        freq[value].append(key)

    res = []
    for i in range(len(freq)-1,0,-1):
        # print(freq[i])
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res
    

print(topKFrequent(nums,k))


def topKFrequent2(nums, k):
    """
    O(n logn)
    """
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # Sort by frequency (descending)
    sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    print(sorted_items[:k])
    # Take top k elements
    return [item[0] for item in sorted_items[:k]]

print(topKFrequent2(nums,k))