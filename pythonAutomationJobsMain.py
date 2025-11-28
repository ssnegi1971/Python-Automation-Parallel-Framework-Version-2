import sys
import threading
import subprocess
#import os

#This is the main file for Python Automation Parallel Framework.
#It invokes the python automation script.
#Multiple data files containing python jobs can be passed as a parameter.
#Also multiple Main processes can be run for multiple sets of jobs each example different warehouses.

def run_script(script_name, param1, param2):
    subprocess.run(["python", script_name, param1, param2]);
#the below setting can be changed for more parallel jobs.
#Also the pythonAutomationJobs.py will have to be changed for more parallelism.
noparalleljobs = "5";

if __name__ == "__main__":
    script_thread1 = threading.Thread(target=run_script, args=("C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/SQLAlchemyPandasPythonProcedureCheckJobs.py","","",));
    script_thread1.start();
    script_thread1.join();
    with open('C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/keepprocessing.txt', "r") as file:
        loopjobs=file.read().rstrip('\n');
    while loopjobs!='STOP':
        script_thread1 = threading.Thread(target=run_script, args=("C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/SQLAlchemyPandasPythonProcedureFetchJobs.py",noparalleljobs,"",));
        script_thread1.start();
        script_thread1.join();    
        script_thread1 = threading.Thread(target=run_script, args=("C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/pythonAutomationJobs.py","C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/pythonJobs.txt","",));
        script_thread1.start();
        script_thread1.join();
#    os.remove("C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/pythonJobs.txt");
        script_thread1 = threading.Thread(target=run_script, args=("C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/SQLAlchemyPandasPythonProcedureCheckStatus.py","","",));
        script_thread1.start();
        script_thread1.join();
        with open('C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/status.txt', 'r') as file:
            file_content = file.read().rstrip('\n');
            print(file_content);
            if file_content == 'CONTINUE':
                print("Next Task");
            # Send email configuring your SMTP server.
#                script_thread1 = threading.Thread(target=run_script, args=("C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/sendmailoutlook.py","ssnegi@yahoo.com","Success",));
#                script_thread1.start();
#                script_thread1.join();
#                print ("email sent");
            else:
                print("Failure in Load");
                # Send email configuring your SMTP server.
                script_thread1 = threading.Thread(target=run_script, args=("C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/sendmailoutlook.py","ssnegi@yahoo.com","Failure",));
                script_thread1.start();
                script_thread1.join();
                print ("email sent");
                sys.exit(1);
        script_thread1 = threading.Thread(target=run_script, args=("C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/SQLAlchemyPandasPythonProcedureCheckJobs.py","","",));
        script_thread1.start();
        script_thread1.join();
        with open('C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/keepprocessing.txt', "r") as file:
            loopjobs=file.read().rstrip('\n');
#        print (loopjobs);
    print("All jobs finished");
print("Main script run");