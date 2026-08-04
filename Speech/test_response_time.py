from Speech.response_time import ResponseTimer
import time

timer = ResponseTimer()

print("Question Asked")

timer.start()

print("Candidate Thinking...")

time.sleep(3)

timer.stop()

print()

print("Response Time :", timer.response_time())

print("Score :", timer.response_score())

print(timer.feedback())