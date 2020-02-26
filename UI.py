#!/usr/local/bin/python3

from MMFolder import MMFolder as MMF
import os

class MainUI():
    def __init__(self, path):
        self.path = path

    def start(self):
        ans = True
        while ans:
            print (f'''
MAIN MENU | {os.getcwd()}
-------------------------------
1.Transcode
2.Download Images from Upsplash
3.Print all files
4.Generate project structure
            ''')
            ans=input("What would you like to do?")
            try:
                if ans[0]=="1": # transcode with FFBlade
                    MMF(self.path).transcode()

                elif ans[0]=="2": # download batch of dummy images from Upsplash
                    try:
                        MMF(self.path).downloadDummyImages(ans.split(' ')[1], ans.split(' ')[2], ans.split(' ')[3])
                    except:
                        MMF(self.path).downloadDummyImages()

                elif ans[0]=="3": # print all files
                    print(f'\n{MMF(self.path).allFiles}\n')

                elif ans[0]=="4":
                    MMF(self.path).createProjectStructure()

                elif ans[0]=='q':
                    break

                else:
                    print("\n Not Valid Choice Try again") 
                    continue

            except:
                print("\n Not Valid Choice Try again")
                ans = True
                continue

def main():
    MainUI(os.getcwd()).start()


if __name__ == "__main__":
    main()
