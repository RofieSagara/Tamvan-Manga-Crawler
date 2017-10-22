import os
import requests
from tools.enumhelper import FolderType
import glob


class InputOutput:

    @staticmethod
    def make_dir():
        if not os.path.exists(os.path.join(os.getcwd(), "Cache")):
            os.makedirs(os.path.join(os.getcwd(), "Cache"))
        if not os.path.exists(os.path.join(os.getcwd(), "Task")):
            os.makedirs(os.path.join(os.getcwd(), "Task"))
        if not os.path.exists(os.path.join(os.getcwd(), "Download")):
            os.makedirs(os.path.join(os.getcwd(), "Download"))

    def download_file(self, url, folder_type=FolderType.CACHE, chapter_title=None, title=None):
        if folder_type == FolderType.CACHE:
            InputOutput.make_dir()
            print(url)
            local_filename = url.split('/')
            file_name = local_filename[3]+local_filename[5]
            if self.is_file_cache(file_name):
                print("File already in cache!")
                return os.path.join(os.getcwd(), "Cache", file_name)
            # NOTE the stream=True parameter
            print("Download file : "+url)
            try:
                r = requests.get(url, stream=True)
                with open(os.path.join(os.getcwd(), "Cache", file_name), 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)
                            # f.flush() commented by recommendation from J.F.Sebastian
            except Exception as ex:
                print("Error :"+str(ex))
                self.delete_file_cache(file_name)
                return None
            return os.path.join(os.getcwd(), "Cache", file_name)
        elif folder_type == FolderType.DOWNLOAD:
            local_filename = url.rsplit('/', 1)[-1]
            path_folder = os.path.join(os.getcwd(), "Download", title)
            if not os.path.exists(path_folder):
                os.makedirs(path_folder)
            path_folder = os.path.join(os.getcwd(), "Download", title, chapter_title)
            if not os.path.exists(path_folder):
                os.makedirs(path_folder)
            try:
                r = requests.get(url, stream=True)
                with open(os.path.join(os.getcwd(), "Download", title, chapter_title, local_filename), 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)
                            # f.flush() commented by recommendation from J.F.Sebastian
            except Exception as ex:
                print("Error :" + str(ex))
                os.remove(os.path.join(os.getcwd(), "Download", title, chapter_title, local_filename))
                return None
            return os.path.join(os.getcwd(), "Download", title, chapter_title, local_filename)

    @staticmethod
    def is_file_cache(file_name):
        file_path = os.path.join(os.getcwd(), "Cache", file_name)
        if os.path.exists(file_path):
            return True
        else:
            return False

    @staticmethod
    def delete_file_cache(file_name):
        file_path = os.path.join(os.getcwd(), "Cache", file_name)
        os.remove(file_path)

    @staticmethod
    def read_all_file():
        list_file = glob.glob(os.path.join(os.getcwd(), "Task", "")+"*.txt")
        return list_file

    @staticmethod
    def delete_file(file_name):
        os.remove(file_name)

    @staticmethod
    def create_file(link, title, title_manga):
        local_filename = link.split('/')
        file_in = open(os.path.join(os.getcwd(), "Task", local_filename[4]+title+".txt"), "w", encoding="utf-8")
        file_in.write(link+"\n"+title+"\n"+title_manga)
        file_in.close()
