import random
import subprocess

weights = [0.4] + [0.6 / 10] * 10   # 0 的权重是 0.4，1-10 各占 6%
choices = list(range(0, 11))       # [0,1,...,10]
n = random.choices(choices, weights)[0]
print(f"Today's commits: {n}")

if n == 0:
    print("No commit today")
else:
    for i in range(n):
        # 随机修改一个文件，这里用 log.txt
        with open("log.txt", "a") as f:
            f.write(f"Commit {i+1} at run\n")
        # 每次提交
        subprocess.run(["git", "add", "log.txt"])
        subprocess.run(["git", "commit", "-m", f"Auto commit {i+1}/{n}"])
