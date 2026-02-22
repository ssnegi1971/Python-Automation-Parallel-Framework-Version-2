import sys
import threading
import subprocess

#This is a Python Automation Parallel Framework. It runs python scripts in parallel.
#It is programmed for maximum 5 python jobs in pythonJobs.txt seperated by a comma.
#The sixth or last element is null inserted for collecting the previous subprocesses.
#It can be expanded to more parallel jobs depending on requirement.

file_path=sys.argv[1];

def run_script(script_name, param):
    subprocess.run(["python", script_name, param]);
"""
with open(file_path, 'r') as file:
    file_content = file.read();
print (file_content);
split_list = file_content.split(',');
print (split_list);
"""
lines = [];
with open(file_path, "r") as file:
    for line in file:
        lines.append(line.strip());
print(lines);
"""
with open(file_path, 'r') as file:
    #lines = file.readlines()
    lines= list(file);
print(lines)
result_list = [
    int(num)               # Convert the string number to an integer
    for s in lines    # Iterate through the main list ['1,2\n', '2,3']
    for num in s.strip().split(',') # Split the stripped string into parts ('1', '2', etc.)
]
print (result_list);
deduplicated_list = [];
for item in result_list:
    if item not in deduplicated_list:
        deduplicated_list.append(item);
print(deduplicated_list);
"""
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
            '''
            if index==1:
                 script_thread1.join();
            elif index == 2:
                script_thread1.join();
                script_thread2.join();
            elif index == 3:
                script_thread1.join();
                script_thread2.join();
                script_thread3.join();
            elif index == 4:
                script_thread1.join();
                script_thread2.join();
                script_thread3.join();
                script_thread4.join();                
            elif index == 5:
                script_thread1.join();
                script_thread2.join();
                script_thread3.join();
                script_thread4.join();
                script_thread5.join();
'''                
            print("All scripts have finished executing.");