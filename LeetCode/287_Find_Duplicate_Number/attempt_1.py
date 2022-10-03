# O(n) time | O(1) space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        catch = 0
        
        # slow same distance from start of cycle as start of LL/root
        while catch != slow:
            catch = nums[catch]
            slow = nums[slow]
        
        return catch
