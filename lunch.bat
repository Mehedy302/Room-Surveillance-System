start runner.bat
timeout 45

start chrome http://127.0.0.1:5000/live
 
python detector_runner.py
timeout 20
