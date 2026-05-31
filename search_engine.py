#import required module os & time
#----------------------------------------------------
import os
import time

#--------------------------------------------------------
#make a function for size of file into different sizes
#--------------------------------------------------------
def format_size(size):
    
    if size < 1024:
        return str(size) + " B"

    elif size < 1024 * 1024:
        return str(round(size/1024,2)) + " KB" #,2 mean after point only 2 digit

    else:
        return str(round(size/(1024*1024),2)) + " MB"
#---------------------------------------------------------

#make a function for search of file from differnt location & join path into complete location
#----------------------------------------------------------------
def search_files(folder, keyword):

    results = []

    for root, dirs, files in os.walk(folder):

        for file in files:

            if keyword.lower() in file.lower():

                full_path = os.path.join(root, file)
                size = os.path.getsize(full_path)

                results.append((full_path, size))

    return results
#----------------------------------------------------

#main function of project to take input by user for folder & keyword for search & then show result
#----------------------------------------------------------------------
def main():

    print("=== File Search Engine ===")

    folder = input("Enter folder path (leave blank for current): ")

    if folder == "":
        folder = os.getcwd()

    keyword = input("Enter file name to search: ")

    start = time.time()

    results = search_files(folder, keyword)

    end = time.time()

    if len(results) == 0:
        print("No files found")

    else:
        print("\nFound Files:\n")

        for i,(path,size) in enumerate(results,1):
            print(i,".",path,"-",format_size(size))

        print("\nTotal files found:",len(results))

    print("Search completed in",round(end-start,2),"seconds")
#-------------------------------------------------------------------

#for running for the program 
#------------------
main()
#---------------