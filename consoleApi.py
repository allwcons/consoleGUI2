import os
from os import name
import sys
from os import system
import subprocess
 
import json

class Console:
    def __init__(self, mainGui):
        self.__inputs = []
        self.gui = mainGui
        self.gui.setApiHandler(self)

    def addCommands(self,command):
        self.__Command = command

    def takeCommand(self,command):
        self.run(command)
    def space(self):
        self.gui.log("\n")

    def changePath(self,path):
        self.gui.changePath(path)
        self.__path = path
    
    def getPath(self):
        return self.gui.getPath()

    def run(self,command):

        try:
            self.__Command.run(command, self.getPath())
        except AttributeError as e:
            self.gui.log(f"no Commands added or {e}",type="error")

    def breakLoop(self):
        self.gui.exit()

    def clear(self):
      self.gui.clear()

    def mkdir(self,path):
        os.system(f"mkdir {path}")

    def rmdir(self,path):
        os.system(f"rmdir {path}")

    def dirExist(self,path):
        self.gui.log(os.path.isdir(path))

    def fileExist(self,path):
        self.gui.log(os.path.isfile(path))

    def cmdRunner(self,cmd):
        result = subprocess.getoutput(cmd)
        self.gui.log(result)


    def cd(self, path,console):
        try:
            path1 = os.path.join(os.getcwd(),path)
            os.chdir(path1)
            self.changePath(path1+">")
        except FileNotFoundError:
            self.gui.error("filenot found")

    def cdBack(self):
        parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
        os.chdir(parent_path)
        self.changePath(parent_path + ">")

    def dirR(self, path,space=""):
      current_path = path
      list_dir = os.listdir(path)
      if(len(list_dir) == 0):
        return
      for content in list_dir:
        os.chdir(path)
        if os.path.isdir(content):
          self.gui.log(space +"+ "+content)
          new_path = os.path.join(path,content)
          new_space =space +  "   "
          self.dirR(new_path,new_space)
        elif os.path.isfile(content):
          self.gui.log(space +"-- "+content)
      os.chdir(current_path)

    def dirs(self, recursive=False):
        if not recursive:
            #window
            if name == 'nt': 
                self.cmdRunner('dir') 
        
            # for mac and linux(here, os.name is 'posix') 
            else: 
                self.cmdRunner('ls')
        elif recursive:
            self.dirR(os.getcwd())



    def loadJson(self, file):
      with open(file,"r") as f:
        w = f.read()
        res = json.loads(w)
        return res

    def wconsBunddle(self, moduleName):
      filePath = os.path.join(moduleName + ".wcons")
      moduleJson = self.loadJson(filePath)
      return moduleJson["filename"]


