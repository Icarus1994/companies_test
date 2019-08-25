# 实现经典堆排序(升序排列)
class solution:
    def heapSort(self,arr):
        for i in range(len(arr)//2,0,-1):
            self.buildHeap(arr,i,len(arr))
        for j in range(len(arr),1,-1):
            arr[j-1], arr[0] = arr[0], arr[j-1]
            self.buildHeap(arr,1,j-1)
        return arr

    def buildHeap(self,arr, start, end):
        while start*2<=end:
            max_loca = start*2 if arr[start-1] < arr[2*start-1] else start
            print(max_loca)
            if start*2<end:
                max_loca = start*2+1 if arr[start*2]>arr[max_loca-1] else max_loca
            if max_loca == start:
                break
            else:
                arr[start-1], arr[max_loca-1] = arr[max_loca-1], arr[start-1]
                start = max_loca

# 思路
# 原地构建最大堆；构建完后，每次将堆顶和堆最后一个元素交换，最后一个元素不动，移动前面的元素使之成为最大堆
# 细节
# 1、构建最大堆的buildHeap方法和往堆新加元素方法类似，start是需要移位的元素的位置
# 2、用数组表示堆时，一般数组下标从1开始，这样每个节点和左儿子节点是2倍关系，但arr已经给定，所以注意下标
# 3、第一步原地构建最大堆时，移位的第一个节点从len(arr)//2开始即可，是因为之后的节点都没有儿子节点
# 4、第一步原地构建最大堆时，因为构建的顺序是从len(arr)//2往前构建的，所以当要移位下标比较小的元素时，
# 它的左右子树都已经是堆了，因此可以沿用bulidHeap方法


