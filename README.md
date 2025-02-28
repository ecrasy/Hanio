# Hanio
Tower of Hanoi Using Recursion  
最近在复习Python  
拿这个经典汉诺塔来练练手  
## 汉诺塔  
有三个pillows和N个碟子disks  
每次只能操作一个碟子disk  
大的碟子disk不能叠放到小的碟子disk之上  
初始情况为：  
N个碟子disks已经按照大小从下往上依次堆叠在第一个pilow上  
问：把所有的disks从第一个pillow搬运到第三个pillow时需要多少个步骤  
## 解题思路
将disks分解为1和n-1  
n-1个disks作为一个整体来看待  
对于1个disk的情况  
只需要将其从source move到dest即可  
剩下的n-1个disks则递归调用n个disks的解法  
将其move到那个辅助的pillow上即可  
