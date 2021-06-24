import sys
import textwrap
import time
def quit():
  sys.close
class ui:
  def pause():
    input("press enter to continue\n")
  def quitask():
    input("press enter to quit\n")
    quit()
  def ask(question):
    input(question)
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    def printc(text, color):
      print(f'{color}{text}{colors.ENDC}')

try:
    colors.printc("found text.txt", colors.OKBLUE) 
    colors.printc("reading", colors.OKCYAN)   
    f = open("text.txt", "r")
    colors.printc("done", colors.OKCYAN)   
    time.sleep(1.5)
except FileNotFoundError:
    print("Error: File 'text.txt' wasn't found. Make sure it is in the same directory as this script and run again.")
    input("Press any key + Enter to end program...")
    ui.quitask()

text = f.read()
lines = textwrap.wrap(text, 19)
i = 0
fi = open("booktext.txt", "w")
print("lines to print:", len(lines))
paged = 0
for line in range(len(lines)):
  summ = line % 14
  if summ == 0:
    pages += 1
colors.printc("pages to print: "+pages, colors.OKCYAN)
ui.pause()
for line in range(len(lines)):
    println = "generating line:", line + 1
    summ = line % 14
    if summ == 0:
        i += 1
        fi.write("\n")
        fi.write(f" ====Page: {i}====\n")
        colors.printc("=====New page=====", colors.OKBLUE)
    fi.write(lines[line] + "\n")
    colors.printc(println, colors.OKCYAN)
    time.sleep(.01)
println = "printing line:", 0
line = 1
for line in range(len(lines)):
  colors.printc(println, colors.OKCYAN)
  println = "printing line:", line + 1
  summ = line % 14
  if summ == 0:
      i += 1
      fi.write("\n")
      fi.write(f" ====Page: {i}====\n")
      colors.printc("=====New page=====", colors.OKBLUE)
colors.printc(println, colors.OKCYAN)

colors.printc("done", colors.OKGREEN)
colors.printc("\n\nWARNING:if booktext.txt is empty delete the file and try again, if that did not work use a longer text", colors.WARNING)
colors.printc("\nyou can generate a long text at lipsum.com", colors.HEADER)
