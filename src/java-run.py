import os
import sys

if __name__ == "__main__":

    """
    This script compiles and runs a java file in the current directory.
    It deletes all class files after it is done.
    """

    cmd_args: list = sys.argv[1:]

    if len(cmd_args) != 1:
        print("only one java file")
        exit()
    else:
        jfile: str = cmd_args[0]
        dirlst: list = os.listdir()
        if not jfile in dirlst:
            print(jfile + " is not in " + os.getcwd())
            exit()
        else:
            javac_exit_status: int = os.system("javac " + jfile)
            if javac_exit_status == 2:
                # this should never happen
                print("the file does not exist")
            elif javac_exit_status == 1:
                print("compilation error")
            elif javac_exit_status == 0:
                # make sure the class file was generated
                java_program_name: str = jfile.split(".")[0]
                if java_program_name + ".class" in os.listdir():
                    os.system("java " + java_program_name)
                    os.system("del *.class")
                else:
                    print("no class file was generated")
            else:
                print("unknown exit status")