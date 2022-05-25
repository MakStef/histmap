import zipfile
import pathlib
import os

from django.shortcuts import get_object_or_404

from main.models import History_Object
from histmap.settings import MEDIA_ROOT

def unzip(obj_slug):
    object = get_object_or_404(History_Object, slug=obj_slug)
    unwrap_dir = pathlib.Path.joinpath(MEDIA_ROOT, "layout_unwrapped")
    if pathlib.Path.exists(unwrap_dir) == False:
        pathlib.Path.mkdir(unwrap_dir)
    path = pathlib.Path.joinpath(unwrap_dir, object.slug)
    if pathlib.Path.exists(path):
        print("Layout was unwrapped already")
        pass
    else:
        with zipfile.ZipFile(object.layout) as arch:
            print("Layout is unwrapping")
            pathlib.Path.mkdir(path)
            arch.extractall(path)
def path_to_files(obj_slug):
    path = MEDIA_ROOT.joinpath("layout_unwrapped/"+obj_slug)
    if pathlib.Path.exists(path):
        for myfile in path.glob("*.wasm"):
            obj_wasm = +str(myfile.relative_to(MEDIA_ROOT)).replace("\\","/")
        for myfile in path.glob("*.data"):
            obj_data = str(myfile.relative_to(MEDIA_ROOT)).replace("\\","/")
        return "/media/"+obj_wasm, "/media/"+obj_data
    else:
        return print("Was lookup for non-existing file")