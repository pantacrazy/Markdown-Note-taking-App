import language_tool_python,os
class grammar_check:
    def __init__(self):
        self.tool = language_tool_python.LanguageTool('en-US')
    def is_bad_rule(self,rule):
        return rule.message=='Possible spelling mistake found.' and len(rule.replacements)>0 and rule.replacements[0][0].isupper()
    def check(self,text):
        matches=self.tool.check(text)
        return [match for match in matches if not self.is_bad_rule(match)]
    def correct(self,text):
        matches=self.check(text)
        return language_tool_python.utils.correct(text,matches)
    