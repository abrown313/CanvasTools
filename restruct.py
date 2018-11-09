import os
import sys

def restructure():

    if len(sys.argv) != 2:

        # incorrect arguments
        print("Incorrect number of arguments. Use: python restruct.py [path to submissions folder]")
        return

    directory = sys.argv[1]

    if not os.path.exists(directory):

        # incorrect path
        print("Incorrect path. Make sure the path passed in is valid.")
        return

    for submission in os.listdir(directory):

        # find/create student folder
        name = submission.split("_")[0]
        student_folder = '%s/%s/Submission attachment(s)' % (directory, name)
        if not os.path.exists(student_folder):
            os.makedirs(student_folder)

        # find/clean file name
        file_name = submission.split("_")[-1]
        if len(file_name.split("-")) == 2:
            file_name = file_name.split("-")[0]
            file_name += '.java'

        # rename & move submission
        old_file_path = '%s/%s' % (directory, submission)
        new_file_path = '%s/%s' % (student_folder, file_name)
        if os.path.exists(new_file_path):
            os.remove(new_file_path)
        os.rename(old_file_path, new_file_path)

restructure()
