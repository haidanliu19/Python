#C:/doit/sub_dir_search.py
import os

def search(dirname):
    #print(dirname)
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname,filename)
            #print(full_filename)
            #ext = os.path.splitext(full_filename)[-1]
            #if ext == '.py':
            #    print(full_filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass
            
#search("C:/")

#교재 289
for(path,dir,files) in os.walk("C:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))
