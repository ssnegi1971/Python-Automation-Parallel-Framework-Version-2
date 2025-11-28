I have written a Python Automation Parallel Framework.

It is used to run python jobs, listed in a database repository, in parallel. 

It consists of the below components:

pythonAutomationJobsMain.py

pythonAutomationJobs.py

pythonJobs.txt

The process flow is as follows:

The pythonAutomationJobsMain.py fetches the jobs to be run from the database and passes them to pythonAutomationJobs.py.

pythonAutomationJobs.py extracts the jobs contained in pythonJobs.txt

It runs the job in separate thread processes in parallel.

Each job writes status information to a database status table.

When all the jobs running in parallel have finished it stops.

Then it processes the next set of jobs from the Main program.

The jobs in the database repository are run in dependency between jobs.

The framework has been designed for 5 parrallel jobs at a time but can be expanded to more parallel jobs.

Multiple Main programs can be invoked for different data sources, example warehouses.
