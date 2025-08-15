import os
class mark:
    def __init__(self):
        self.dir=os.path.dirname(__name__).join('markdowns')
    
    def get_markdowns(self):
        markdowns=[]
        if os.path.exists(self.dir):
            for files in os.listdir(self.dir):
                if files.endswith('.md') or files.endswith('.markdown'):
                    markdowns.append(files)
        else:
            markdowns.append('No markdowns found')
        return markdowns