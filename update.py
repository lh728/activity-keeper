import random, subprocess, sys

def sh(cmd):
    subprocess.run(cmd, check=True)

# 确保有身份
sh(["git", "config", "user.name", "lh728"])
sh(["git", "config", "user.email", "65521533+lh728@users.noreply.github.com"])

weights = [0.4] + [0.6 / 10] * 10
choices = list(range(0, 11))
n = random.choices(choices, weights)[0]
print(f"Today's commits: {n}")

if n == 0:
    print("No commit today")
    sys.exit(0)

for i in range(n):
    with open("log.txt", "a") as f:
        f.write(f"Commit {i+1} at run\n")
    sh(["git", "add", "log.txt"])
    sh(["git", "commit", "-m", f"Auto commit {i+1}/{n}"])


