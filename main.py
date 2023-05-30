from task1 import *
from task2 import *
from scheduler import *
import time 
import cv2 

scheduler = Scheduler()
scheduler.SCH_Init()

# task1 = Task1()
# task2 = Task2()

# schedule.SCH_Add_Task(task1.Task1_Run, 1000, 50000)
# schedule.SCH_Add_Task(task2.Task2_Run, 2000, 60000)


# while True:
#     schedule.SCH_Update()
#     schedule.SCH_Dispatch_Tasks()

# print("Hello LAB2")
# import time
# from scheduler import *
# from task1 import *
# from task2 import *
# scheduler = Scheduler()
# scheduler.SCH_Init()

# task1 = Task1()
# task2 = Task2()

# scheduler.SCH_Add_Task(task1.Task1_Run, 1000,2000)
# scheduler.SCH_Add_Task(task2.Task2_Run, 2000,4000)

# while True:
#     scheduler.SCH_Update()
#     scheduler.SCH_Dispatch_Tasks()
#     time.sleep(1)

class TimerTask: 
    def __init__(self):
        self.timer = 0

    def run(self):
        print(f"At time: {self.timer}")
        self.timer += 1

    timer = 0

task1a = Task1(0)
task1b = Task1(1)
timer_task = TimerTask()

scheduler.SCH_Add_Task(task1.Task1_Run, 1000, 2000)
scheduler.SCH_Add_Task(task1b.Task1_Run, 1000, 4000)
scheduler.SCH_Add_Task(timer_task.run, 0, 1000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)
    keyboard_input = cv2.waitKey(1)
    if keyboard_input == 27:
        break

task1b.camera.release()
task1a.camera.release()
cv2.destroyAllWindows()