# Hanio
Tower of Hanoi Using Recursion  
![image](tower-of-hanoi.png)  

最近在复习Python  
拿这个经典汉诺塔来练练手  
## 汉诺塔  
有3个pillows和n个碟子disks  
每次只能操作1个碟子disk  
大的碟子disk不能叠放到小的碟子disk之上  
初始情况为：  
n个碟子disks已经按照大小从下往上依次堆叠在第1个pilow上  
问：把所有的disks从第1个pillow搬运到第3个pillow时需要多少个步骤  
## 解题思路
将disks分解为1和n-1  
n-1个disks作为一个整体来看待  
对于1个disk的情况  
只需要将其从source move到dest即可  
剩下的n-1个disks则递归调用n个disks的解法  
将其move到那个辅助的pillow上即可  

## code output
step 1 : Move disk 1 from source A to destination C  
step 2 : Move disk 2 from source A to destination B  
step 3 : Move disk 1 from source C to destination B  
step 4 : Move disk 3 from source A to destination C  
step 5 : Move disk 1 from source B to destination A  
step 6 : Move disk 2 from source B to destination C  
step 7 : Move disk 1 from source A to destination C  
