class Question:
    def __init__(self,question,answer,incorrect):
        self.q = question.replace("&quot","")
        self.a = answer
        self.incorrect = incorrect
        self.responses = [self.a,self.incorrect[0], self.incorrect[1], self.incorrect[2]]


logo = """
===========================================
████████╗██████╗ ██╗██╗   ██╗██╗ █████╗ ██╗
╚══██╔══╝██╔══██╗██║██║   ██║██║██╔══██╗██║
   ██║   ██████╔╝██║██║   ██║██║███████║██║
   ██║   ██╔══██╗██║╚██╗ ██╔╝██║██╔══██║╚═╝
   ██║   ██║  ██║██║ ╚████╔╝ ██║██║  ██║██╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═╝╚═╝                   
===========================================
"""