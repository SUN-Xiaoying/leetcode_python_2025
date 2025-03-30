class Solution:
    def main(self):
        dict1 = {'value':11}
        dict2 = dict1
        print("ID1: ", id(dict1))
        print("ID2: ", id(dict2))

        dict2['value']=22
        print(dict1['value'])
        print(dict2['value'])
        print("ID1: ", id(dict1))
        print("ID2: ", id(dict2))



solution = Solution()
solution.main()