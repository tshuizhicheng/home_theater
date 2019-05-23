
from django.shortcuts import render
import os
# Create your views here.


FILE_HOME_DIR = "D:\\Rmcache"
MEDIA = [ ".mp4",]


def movie_list(request):
    next = request.GET.get("next", '')
    print(f"next = {next}")
    print("request.path:", (request.build_absolute_uri()).replace(request.path,''))
    path = "/".join(request.path.split("/")[2:])
    print(f"request.path= {request.path}")
    print(f"path = {path}")
    print("lllllllllllllllllllllllllllllllllllllllllllllllll")

    #print os.listdir(FILE_HOME_DIR+".none/")
    data = {"files":[], "dirs":[]}
    print(data)
    child_path = FILE_HOME_DIR+path+next
    print(f"child_path = {child_path}")
    data['cur_dir'] = path+next
    
#    print(data)
    for dir in os.listdir(child_path):
        if os.path.isfile(child_path+"/"+dir):
            if os.path.splitext(dir)[1] in MEDIA:
                data['files'].append(dir)
        else:
            data['dirs'].append(dir)

    data['url'] = (request.build_absolute_uri()).replace(request.path,'')
    data['url'] = data['url'][0:data['url'].rfind(":")]+ ":8080" + path + next
    print(data)
    return render(request,"movie/index.html", data)
