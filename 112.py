if os.path.exist(path2):
    print("Moving" + file_name + "....")


    shutil.move(path1,path3)


else:
    os.makedirs(path2)
    print("Moving" + file_name + "....")
    shutil.move(path1,path3)
