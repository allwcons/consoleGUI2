import os
import sys
import subprocess
from import_file import import_file

def entries(console,commands):
    log = console.gui.log
    error = console.gui.error
    warn = console.gui.warn

    def importer(path, moduleName):
        p = console.getPath()
        filename = console.wconsBunddle(moduleName)
        mylib = import_file(os.path.join(p, filename))
        e = mylib.entries(console, commands)
        commands.addCommands(e[0])
        commands.modules.addModule(e[0], moduleName)
        if(len(e[1]) > 0):
            commands.setDobuleCommandDict(e[1])
        log("imported")




    cmd = {
        "exit()" :{
            "*":lambda path,args: console.breakLoop()
        },
        "cls": lambda path,args:console.clear(),
        "ls":{
            "*": lambda path,args:console.dirs(),
            "-r":lambda path,args: console.dirs(True),
            "${other}":lambda path,args: warn("only -r supported yet " + args + " not suporeted")
        },
        "cd":{
            "*": lambda path,args: warn("please provide path"),
            "${path}":lambda path,args: console.cd(args,console),
            "..": lambda path,args: console.cdBack()
        },
        "pwd": lambda path,args:log(console.getPath(),type="special"),
        "mkdir":{
            "*":lambda path,args: warn("pleae provide dir path"),
            "${folder}":lambda path,args:console.mkdir(args)
        },
        "rmdir":{
            "*":lambda path,args: warn("pleae provide dir path"),
            "${folder}":lambda path,args:console.rmdir(args)            
        },
        "isexist": {
            "*":lambda path,args: warn("pleae provide dir path"),
            "${path}":{
                "*": lambda path,args: warn("please provide check type"),
                "-dir":lambda path,args: console.dirExist(args["path"]),
                "-file":lambda path,args: console.fileExist(args["path"])
            }
        },
        #import should be in wcons extension file
        "import": {
            "*": lambda path,args:warn("please provide path"),
            "${path}": lambda path,args: importer(path,args)
        },
        "delete":{
            "*": lambda path,args:warn("please provide path"),
            "${path}": lambda path,args: commands.modules.delModule(args)
        }

    }
    newCmds = {
    "dir":"ls",
    "clear":"cls"
}

    return [cmd,newCmds]