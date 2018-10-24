import subprocess


def get_str(param):
    x=((subprocess.Popen([str(param)],shell=True, bufsize=0,\
            stdout=subprocess.PIPE,stderr=subprocess.PIPE,\
            universal_newlines=False)).communicate()[0].decode('utf-8')).strip()
    return x


print("The text files available are : \n"+get_str("ls *txt"))
print("The word count is \n"+get_str("wc -w *.txt"))
print("The Words with above length minimum length are "+get_str("grep -o -w '\w\{5,\}' *.txt |wc -l"))

