# Project_IN422 - Tasks Manager Scheduler in Python using Pygame

Tasks Manager Scheduler is a Python application with a graphical interface built using Pygame. It demonstrates five fundamental CPU scheduling algorithms (FCFS, SJN, Round Robin, Rate Monotonic, Earliest Deadline First) and allows users (even beginner) to:

    Choose an algorithm based on different characteristics.

    Input a custom set of processes (arrival times, burst times, periods, deadlines, quantum/limits).

    Visualize scheduling decisions step by step.

    Compare performance metrics (Completion Time, Turnaround Time, Waiting Time, and their averages) across different algorithms.

    Learn the core principles behind each algorithm through hands-on experimentation.

### Table of Contents

    Installation & Setup

    Launching the Application

    Navigating the UI

    Using the Scheduler

        1. Choose Expertise Level

        2. Select Scheduling Category

        3. Pick an Algorithm

        4. Define Processes & Parameters

        5. Validate & View Results

        6. Compare Algorithms

    Algorithm Reference

        First Come First Serve (FCFS)

        Shortest Job Next (SJN)

        Round Robin (RR)

        Rate Monotonic (RM)

        Earliest Deadline First (EDF)

    Function Signatures & I/O

### Installation & Setup

Clone the repository

    git clone https://github.com/Thibaud95/Project_IN422 cd tasks-manager-scheduler

Install dependencies

    pip install Pygame

### Launching the Application

Run the main module:

    python3 main.py

A window titled “Tasks Manager” will open. Use your mouse to click buttons and text fields.
### Navigating the UI

    Homepage Level 1

        Beginner: guided selection by category

        Expert: directly choose algorithm

        Quit: exit application

    Homepage Level 2

        Shows all five algorithms or filters based on your beginner choices.

    Algorithm Page

        Input number of processes.

        Enter arrival/burst times (plus periods/deadlines or quantum/limits).

        Validate to compute scheduling.

        Compare button appears to juxtapose against other algorithms.

### Using the Scheduler
1. Choose Expertise Level

    Beginner: Walks you through categories (preemptive vs. non-preemptive, real-time constraints, priority assignment).

    Expert: Skip categories and jump straight to any algorithm.

2. Select Scheduling Category

(Beginner only)

    Based on Preemption: Preemptive vs. non-preemptive.

    Based on Timing Constraints: Soft vs. hard real-time.

    Based on Priority Assignments: Static vs. dynamic priority.

3. Pick an Algorithm

    FCFS, SJN (non-preemptive)

    RR (preemptive, needs quantum)

    RM (static priority, needs periods & time limit)

    EDF (dynamic priority, needs deadlines, periods, & time limit)

4. Define Processes & Parameters

    Number of Processes: Enter N in the top-right box, click Add Processes.

    Arrival Time: For each process Pi, type when it enters the system (integer).

    Burst Time: CPU time required for Pi.

    Additional Fields

        Round Robin: Choose quantum then click on “Set quantum”).

        Rate Monotonic: Period for each Pi, then a global time limit.

        Earliest Deadline First: Period & Deadline per Pi, then a global time limit.

5. Validate & View Results

    Click Validate.

    The table updates to show, for each process:

        Completion Time

        Turnaround Time = Completion − Arrival

        Waiting Time = Turnaround − Burst

    Average Turnaround Time and Average Waiting Time appear below.

6. Compare Algorithms

    After validation, click Compare.

    Select another algorithm to run with the same inputs.

    Side-by-side tables and average metrics show which algorithm performed better.

### Algorithm Reference
First Come First Serve (FCFS)

    Type: Non-preemptive

    Rule: Schedule in order of arrival.

    Use-case: Simple batch systems; fairness by arrival order.


Shortest Job Next (SJN)

    Type: Non-preemptive

    Rule: Pick the process with the smallest burst time among arrived.

    Use-case: Minimizes average waiting time, but can starve long jobs.


Round Robin (RR)

    Type: Preemptive

    Rule: Give each process a fixed quantum in round-robin order.

    Use-case: Time-sharing systems; responsive user interfaces.

    Key Parameter: Quantum → too small ⇒ overhead; too large ⇒ behaves like FCFS.

Rate Monotonic (RM)

    Type: Static priority (preemptive)

    Rule: Periodic tasks; shorter period ⇒ higher priority.

    Use-case: Hard real-time systems where deadlines = period.

    Schedulability: Guaranteed if CPU utilization ≤ N(2^(1/N)−1).

Earliest Deadline First (EDF)

    Type: Dynamic priority (preemptive)

    Rule: At any moment, schedule the task whose deadline is soonest.

    Use-case: Optimal for uniprocessor soft/hard real-time tasks.

    Schedulability: Feasible if total utilization ≤ 1.

### Function Signatures & I/O

All algorithms share this signature pattern in their modules:

    Inputs

        process_list: e.g., ["P1","P2","P3"]

        arrival_times: [0, 2, 4]

        burst_times: [3, 6, 4]

        RR: append quantum (e.g., 2)

        RM: append periods list plus time_limit

        EDF: append deadlines list, periods list, then time_limit

    Outputs

        Three dictionaries mapping each process to its metric.

        Two floats: average metrics.


