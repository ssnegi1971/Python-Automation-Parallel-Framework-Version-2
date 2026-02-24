import sys
import threading
import subprocess

#This is a Python Automation Parallel Framework. It runs python scripts in parallel.
#It is programmed for maximum 5 python jobs in pythonJobs.txt seperated by a comma.
#The sixth or last element is null inserted for collecting the previous subprocesses.
#It can be expanded to more parallel jobs depending on requirement.

file_path=sys.argv[1];

def run_script(script_name, param):
    subprocess.run(["pythonw", script_name, param]);
lines = [];
with open(file_path, "r") as file:
    for line in file:
        lines.append(line.strip());
print(lines);
for index, item in enumerate(lines):
    print(f"Index: {index}, Item: {item}")
    if __name__ == "__main__":
        if index == 0 and item != 'null':
            script_thread1 = threading.Thread(target=run_script, args=(item,item));
            script_thread1.start();
        elif index == 1 and item != 'null':
            script_thread2 = threading.Thread(target=run_script, args=(item,item));
            script_thread2.start();
        elif index == 2 and item != 'null':
            script_thread3 = threading.Thread(target=run_script, args=(item,item));
            script_thread3.start();
        elif index == 3 and item != 'null':
            script_thread4 = threading.Thread(target=run_script, args=(item,item));
            script_thread4.start();
        elif index == 4 and item != 'null':
            script_thread5 = threading.Thread(target=run_script, args=(item,item));
            script_thread5.start();
        elif item == "null":
            print("All scripts have finished executing.");