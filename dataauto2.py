import os
import shutil

def organize_files(directory):
#Match file extension to folder name
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Spreadsheets': ['.xls', '.xlsx', '.csv'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Music': ['.mp3', '.wav'],
        'Archives': ['.zip', '.tar', '.gz'],
    }
    
    #If folder does not exist this will make the folder
    for folder in file_types():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
    #To run through files in directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)        
        
        #Skip directories
        if os.path.isdir(file_path):
            continue
        
    # Get file extension 
    _, ext = os.path.splittext(filename)
    
    # Move file to corresponding folder
    moved = False
    for folder, extensions in file_types.items():
        if ext.lower() in extensions:
            destination = os.path.join(directory, folder, filename)
            shutil.move(file_path, destination)
            print(f"Moved '{filename}' to '{folder}/'")
            moved = true
            break
        
    # Optional: move unknown file types to 'Others' folder
    if not moved:
         others_path = os.path.join(directory, 'Others')
        if not os.path.exists(others_path):
            os.makedirs(others_path)
        shutil.move(file_path, os.path.join(others_path, filename))
        print(f"Moved '{filename}' to 'Others/'")
        
# Replace path below with target directory
# Organize files ('/Users/yourname/Downloads')