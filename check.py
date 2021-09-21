def entries(console,commands):
  log = console.gui.log
  cmd = {
     "check1":{
       "${hello}":lambda path,args:log(args),
       "${hi}":{
          "lol":lambda path,args:log(args),
          "${ok}": lambda path,args:log(args)
       }
     }
     }
  return [cmd,{"check":"check1"}]