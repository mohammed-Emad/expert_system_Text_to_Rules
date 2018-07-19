# no import 

def write_start_up(file_rule_output):

    file = open(file_rule_output, "w" ,encoding="UTF-8") # open a file to write

    file.write("#Written on 19 July 2018 by Mohamed Emad" + "\n")
    file.write("#This was set up in January of the same year" + "\n" +"\n")
    file.write("from pyknow import *" + "\n" + "\n")
    file.write("class engine(KnowledgeEngine):" + "\n" + "\n")
    file.close()



def write_Rules_and_Facts(file_rule_output ,the_rule ,the_decision ,count_function):

   rule_word = the_rule.strip().rsplit(' ', 1)[0].strip()
   rule_val = the_rule.strip().rsplit(' ', 1)[1].strip()

   decision_word = the_decision.strip().rsplit(' ', 1)[0].strip()
   decision_val = the_decision.strip().rsplit(' ', 1)[1].strip()
   file = open(file_rule_output, "a" ,encoding="UTF-8") # open a file to write
   file.write("\t" + "@Rule(Fact({} = {}))".format(rule_word ,rule_val) + "\n")
   file.write("\t" + "def fact_P" + str(count_function) + "(self):" + "\n")
   file.write("\t" + "\t" + "{} = {}".format(decision_word ,decision_val) +"\n")
   file.write("\t" + "\t" + "print('{} :=', {})".format(decision_word ,decision_word) + "\n")
   file.write("\t" + "\t" + "''' Here write the rest of your operations and orders '''"  + "\n" + "\n"+ "\n")
   file.close()



def text_to_Rule(file_text_input ,file_rule_output):

    count_function = 0

    # read file_text_input
    with open( file_text_input ,'r' ,encoding="UTF-8")as text:
        text = text.readlines()
        for textB in text:

            if not textB.strip():
               continue

            if textB.find("%%") != -1: #Override the comments in the script expert file
               continue 
            # Find a division of the distinction between the base and the solution
            f_point = textB.rfind("::")

            the_rule = textB[0:f_point]

            the_decision = textB[f_point+2:len(textB)] # tow2 char "::"

            #try [int(s) for s in the_rule.split() if s.isdigit()][0]  #extra int from string

            write_Rules_and_Facts(file_rule_output ,the_rule ,the_decision ,count_function) #write

            count_function +=1


if __name__ == '__main__':

   print("Start compiler ...")

   write_start_up("compiled_knowledge.py")
   text_to_Rule("data/data_expert.txt" ,"compiled_knowledge.py")

   print("done compile")

