import subprocess
import sys
def shell_output(param):
    """
        This method just takes the shell commands to be executed and returns what
        this command outputs in shell
        :param param: command (example "ls")
        :return: string of commands output on shell
        """
    try:
        #the power of this function shall not be looked down,
        #if you are an admin, you know what it is to have a
        #shell command that can do job for you
        #what if I say, you can leverage the power python brings to you
        #and also the shell commands combined? is it not a gizmo for you?
        #well atleast it is sure an important thing for me
        #do not touch the variable x, it is but to make a
        #comfortable operation and to make use of it later
        x = ((subprocess.Popen(
                    [str(param)],#takes each part of command as a list element, but bro! i can also pass everything
                                 # in one element
                    shell=True,#to run in shell
                    bufsize=0, #need to check why
                    stdout=subprocess.PIPE, #to give it to pipe
                    stderr=subprocess.PIPE, #to give errors also to pipe
                    universal_newlines=False,#shall it include the newline charecters?
                                             # i wonder if anyone likes it that way
                                             #it gives a list instead of string
                )).communicate()[0]#this is to get the value from shell
            .decode("utf-8")#this is to remove 'b i.e to convert from byte to string
        ).strip()
        return x #this function does only one thing, but does it quiet well.
    except Exception as e:
        print("Error with execution in get_str " + str(e))
        return e



print("The text files available are : \n"+shell_output("ls *txt"))
# print("The word count is \n"+shell_output("wc -w *.txt"))
# print("The Words with above length minimum length are "+shell_output("grep -o -w '\w\{5,\}' *.txt |wc -l"))

