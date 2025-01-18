class Regex:
    def __init__(self):
        self.transitions = {} #change to regex, main 
        self.transitions2 = {} # copy self.transitions = {} fuc = checkaccept
        self.untransitions = {} # مقصد → {مبدأ: ورودی}
        self.firststate = ""
        self.finalstates = []
        self.inputstring = ""

    def adtrans(self, state, x, tostate): # add newtran to main ,2
        if self.transitions.get(state) is not None:
            self.transitions.get(state)[x] = tostate
            self.transitions2.get(state)[x] = tostate
        else:
            self.transitions[state] = {x: tostate}
            self.transitions2[state] = {x: tostate}

    def inputtxt(self, textfile):
        file = open(textfile, "r").readlines()
        for line in file:
            line = line.replace(" ", "").replace("\n", "")
            if line.startswith("("):
                self.adtrans(line[1], line[3], line[-1])
            elif line.startswith("final"):
                for i in line[line.find("=") + 1:]:
                    if i.isnumeric():
                        self.finalstates.append(i)
            elif line.startswith("initial"):
                self.firststate = line[-1]
            elif line.startswith("user"):
                self.inputstring = line[line.find("=") + 2: -1]
            else:
                continue

    def checkaccept(self, string):
        currentstate = self.firststate
        # print(self.firststate)
        for word in string:
            currentstate = self.transitions2[currentstate].get(word)
        if currentstate in self.finalstates:
            return True
        else:
            return False

    def showresults(self): 
        self.__finaledit()
        self.__toregex()
        # print(self.firststate)
        # exit()
        output = open("output.txt", "w")
        output.write("#REGEX\n\n")
        for regex in self.transitions[self.firststate]:
            result = regex
            output.write(result + "\n\n")
        if self.checkaccept(self.inputstring):
            output.write("string accepted")

    def __finduseless(self): # find
        temp = self.transitions.copy()
        for state in temp:
            tempdic = {}
            temp1 = self.transitions[state].copy()
            for trans in temp1:
                if self.transitions.get(self.transitions[state].get(trans)) is not None or self.transitions[state].get(trans) == "F":
                    if tempdic.get(self.transitions[state].get(trans)) is None:
                        tempdic[self.transitions[state].get(trans)] = trans
                    else:# A -> (a+b) -> B 
                        if tempdic[self.transitions[state].get(trans)].endswith(")") and tempdic[self.transitions[state].get(trans)].startswith(")"):
                            tempdic[self.transitions[state].get(trans)] = tempdic[self.transitions[state].get(trans)][:-1] + "+" + trans + ")"
                        else:
                            tempdic[self.transitions[state].get(trans)] = "(" + tempdic[self.transitions[state].get(trans)] + "+" + trans + ")"
            self.transitions[state] = {} # update tran
            for trans2 in tempdic:
                value = tempdic.get(trans2)
                self.transitions[state][value] = trans2

    def __findloop(self):# find
        temp = self.transitions.copy()
        for state in temp:
            temp1 = self.transitions[state].copy()
            for trans in temp1:
                if self.transitions[state].get(trans) == state:
                    self.transitions[state].pop(trans)
                    for trans2 in temp1:
                        if trans2 == trans:
                            continue
                        # add * to loop
                        self.transitions[state]["(" + trans + ")*" + trans2] = temp1.get(trans2)
                        self.transitions[state].pop(trans2)
                    break

    def __untrans(self): # A → B → C، A → C     x.y
        self.untransitions = {}
        temp = self.transitions
        for state in temp:
            temp1 = self.transitions[state].copy()
            for trans in temp1:
                if self.transitions[state].get(trans) == "F" or self.transitions[state].get(trans) == self.firststate:
                    continue
                elif self.untransitions.get(self.transitions[state].get(trans)) is None:
                    self.untransitions[self.transitions[state].get(trans)] = {state: trans}
                elif self.untransitions[self.transitions[state].get(trans)].get(state) is None:
                    self.untransitions[self.transitions[state].get(trans)][state] = trans

    def __toregex(self): #remove extra states
        temp = self.transitions.copy()
        for state in temp:
            self.__finduseless()
            self.__findloop()
            self.__untrans()
            temp1 = self.transitions[state].copy()
            if state is not self.firststate:
                for unstate in self.untransitions[state]:
                    for trans in temp1:
                        self.transitions[unstate][self.untransitions[state][unstate] + trans] = self.transitions[state][trans]
                self.transitions.pop(state)
        self.__finduseless()
        self.__findloop()
        self.__untrans()

    def __finaledit(self):
        for finals in self.finalstates:
            if finals not in self.transitions:
                self.transitions[finals] = {}
            self.transitions[finals][""] = "F"


# main
myregex = Regex()
myregex.inputtxt("input.txt")
myregex.showresults()