import os
import subprocess
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
project_path=os.getenv("PROJECT_PATH")
print(project_path)
# Paths to the files and directories
source_image_path = os.path.join(project_path,'hamzamfarooqi.png')
target_video_path = os.path.join(project_path,'imran_khan.mp4')
output_video_path = os.path.join(project_path,'output','output_video.mp4')
if not os.path.exists(os.path.join(project_path,'output')):
    os.makedirs(os.path.join(project_path,'output'))
print(source_image_path,target_video_path,output_video_path)

# Path to the virtual environment's activate script
roop_venv_activate_path = os.path.join(project_path,'venv/bin/activate')
roop_script_path = os.path.join(project_path,'run.py')

# Command to be executed
command = f'source {roop_venv_activate_path} && python {roop_script_path} -s {source_image_path} -t {target_video_path} -o {output_video_path} --execution-provider cuda'
print(command)

# Execute the command
subprocess.run(command, shell=True, check=True, executable='/bin/bash')
