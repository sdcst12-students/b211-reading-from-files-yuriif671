#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

def findSum(filename: str) -> int:
        file = open(filename,'r').read()
        clusters = file.strip().split('\n\n')
        
        cluster_sum = []
        for i in clusters:
            num = 0
            for j in i.splitlines():
                num += int(j)
            cluster_sum.append(num)
        
        return max(cluster_sum)

print(f"Yo largest sum is {findSum('task03.txt')}")