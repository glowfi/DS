# https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1 , Medium


# Better
# T.C. - O(nlog(n)) + O(n^2)
# S.C  - O(deadline*2)+O(n)

# Selection criteria : select the jobs with max profit
# How to do :
# Suppose the deadline arr size is 4 create an auxiliary array with 5 elements
# Pick one job and check whether the element at that index is completed or not in the auxiliary arr
# if an element has deadline of 4 try to complete it as close as possible starting from index 4 in auxiliary array,
# otherwise a job having lower deadline value will not be able to complete the job if its put in the beginning by higher value deadline


class Solution:
    def jobSequencing(self, deadline, profit):
        jobs_arr: list[list[int]] = [[]] * len(deadline)

        for i in range(len(deadline)):
            jobs_arr[i] = [deadline[i], profit[i]]

        jobs_arr.sort(reverse=True, key=lambda x: x[1])
        tasks_done_arr = [-1] * (len(deadline) + 1)

        profit = 0
        jobs_completed = 0

        for job in jobs_arr:
            d, p = job

            for i in range(d, 0, -1):
                if tasks_done_arr[i] == -1:
                    tasks_done_arr[i] = 1
                    jobs_completed += 1
                    profit += p
                    break

        return [jobs_completed, profit]


# Optimal
# T.C. - O(nlog(n)) + O(n)
# S.C  - O(deadline*2)+O(n)

#  Greedy + Disjoint Set Union (DSU)
# Use the algorithm similar to union find parent kruskal mst
# In above algo we have to traverse the entire array in worst case
# But by using below algo we can get the next empty slot to place the current job in constant time
# we create a parent array with length deadline+1 and all the elements are like this [0,1,2,3,4,5,6] they are same as index
# for each job we try to find the empty slot to place them
# if we found a place where idx==element at that index we return that value
# while backtracking we also mark the elements in our traversed path with the empty slot value
# if we ever get 0 as empty slot we can ignore it as its not part of our problem


class Solution:
    def findParent(self, idx, parent_arr):
        if parent_arr[idx] == idx:
            return idx

        parent_arr[idx] = self.findParent(parent_arr[idx], parent_arr)
        return parent_arr[idx]

    def jobSequencing(self, deadline, profit):
        jobs_arr: list[list[int]] = [[]] * len(deadline)

        for i in range(len(deadline)):
            jobs_arr[i] = [deadline[i], profit[i]]

        jobs_arr.sort(reverse=True, key=lambda x: x[1])
        parent_arr = [i for i in range(max(deadline) + 1)]

        profit = 0
        jobs_completed = 0

        for job in jobs_arr:
            d, p = job

            slot = self.findParent(d, parent_arr)
            if slot > 0:
                jobs_completed += 1
                profit += p
                parent_arr[slot] = slot - 1

        return [jobs_completed, profit]
