#*************************************************************************
 # File Name: hanoi.py
 # Author: Carbon (ecrasy@gmail.com)
 # Created Time: 2025-02-28 11:25:11 UTC
 # Modified Time: 2025-02-28 11:25:48 UTC
 # Description: feel free to use
 # ┏┛ ┻━━━━━┛ ┻┓
 # ┃           ┃
 # ┃      ━     ┃
 # ┃  ┳┛    ┗┳   ┃
 # ┃           ┃
 # ┃      ┻     ┃
 # ┃           ┃
 # ┗━┓      ┏━━━┛
 #   ┃      ┃   神兽保佑
 #   ┃      ┃   代码无虫
 #   ┃      ┗━━━━━━━━━┓
 #   ┃                ┣┓
 #   ┃               ┏┛
 #   ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
 #     ┃ ┫ ┫   ┃ ┫ ┫
 #    ┗━┻━┛   ┗━┻━┛
##**********************************************************************/

#!/usr/bin/python3

step = 1

# move n disks from source to destination by using x as helping pillow
def TowerOfHanoi(n, source, x, dest):
    if n == 1:
        global step
        print("step", step, ": Move disk", n, "from source", source, "to destination", dest)
        return

    # treat n-1 disks like a single disk
    # move them to the helping pillow x by using the dest as the new helping pillow
    TowerOfHanoi(n-1, source, dest, x)
    step = step + 1
    print("step", step, ": Move disk", n, "from source", source, "to destination", dest)
    # since the source pillow is empty
    # move n-1 disks to the destination pillow by using the source as helping pillow
    step = step + 1
    TowerOfHanoi(n-1, x, source, dest)


if __name__ == "__main__":
    TowerOfHanoi(3, 'A', 'B', 'C')
