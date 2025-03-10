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