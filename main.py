from task1 import *
from task2 import *
from scheduler import *
import time

scheduler = Scheduler()
scheduler.SCH_Init()

class TimerTask: 
    def __init__(self):
        pass

    def run(self):
        print("At time: {self.timer}")
        self.timer += 1

    timer = 0

task1 = Task1()
task2 = Task2()
timer_task = TimerTask()

scheduler.SCH_Add_Task(task1.Task1_Run, 1000, 2000)
scheduler.SCH_Add_Task(task2.Task2_Run, 1000, 4000)
scheduler.SCH_Add_Task(timer_task.run, 0,1000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(1)
