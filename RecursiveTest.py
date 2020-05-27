

import json




def main():
    
    def walk(d):
        global path
       for k,v in d.items():
           if isinstance(v, str) or isinstance(v, int) or isinstance(v, float):
               path.append(k)
             print("{}={}".format(".".join(path), v)) 
             path.pop()
         elif v is None:
             path.append(k)
             # do something special
             path.pop()
         elif isinstance(v, list):
             path.append(k)
             for v_int in v:
                 walk(v_int)
             path.pop()
         elif isinstance(v, dict):
             path.append(k)
             walk(v)
             path.pop()
     else:
         print("###Type {} not recognized: {}.{}={}".format(type(v), ".".join(path),k, v))
    with open('full_project_structure.json') as f:
        myjson = json.load(f)
    path = []
    walk(myjson)

if __name__ == '__main__':
    main()
