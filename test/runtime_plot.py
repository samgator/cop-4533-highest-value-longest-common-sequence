import subprocess
import time
import matplotlib.pyplot as plt
from pathlib import Path

input_files = [f"input/input{i}.in" for i in range(1, 11)]
output_files = [f"output/output{i}.out" for i in range(1, 11)]
runtimes = []

script = Path("src/main.py")

for input_file, output_file in zip(input_files, output_files):
    start = time.time()
    try:
        subprocess.run(
            ["python", str(script), input_file, output_file],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error with {input_file}: {e}")
        continue
    end = time.time()
    runtimes.append(end - start)
    print(f"{input_file} done in {end - start:.4f}s -> {output_file}")

print("Runtimes:", runtimes)

plt.plot(range(1, len(runtimes)+1), runtimes, marker='o')
plt.xticks(range(1, len(runtimes)+1))
plt.xlabel("Input file")
plt.ylabel("Runtime (seconds)")
plt.title("Weighted LCS Runtime on 10 Inputs")
plt.grid(True)
plt.savefig("test/runtime_graph.png")
plt.show()