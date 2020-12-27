import os, sys

def main():
    count =1
    path_file = "crack_segmentation_dataset/Dataset"
    
    for filename in os.listdir(path_file):
        os.rename(os.path.join(path_file, filename), os.path.join(path_file, str(count)+ ".jpg"))
        count += 1
        
if __name__== '__main__':
    main()
