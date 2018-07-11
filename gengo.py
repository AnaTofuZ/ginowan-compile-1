import json

class Engine:
    def eval(self,value,var_s):
        if isinstance(value,list):
            return self.run(value,var_s)
        return value

    def run(self,value,var_s):
        op = value[0]

        if op  == "+":
            return self.eval(value[1],var_s) + self.eval(value[2],var_s)
        elif op  == "-":
            return self.eval(value[1],var_s) - self.eval(value[2],var_s)
        elif op == '*':
            return self.eval(value[1],var_s) * self.eval(value[2],var_s)
        elif op == '==':
            return self.eval(value[1],var_s) == self.eval(value[2],var_s)
        elif op == 'set':
            var_s[self.eval((value[1]),var_s)] = self.eval(value[2],var_s)
        elif op == 'get':
            return var_s[self.eval(value[1],var_s)]
        elif op == 'while':
            while self.eval(value[1],var_s):
                self.run(value[2],var_s)
        elif op == 'until':
            while not(self.eval(value[1],var_s)):
                v = self.run(value[2],var_s)
            return v
        elif op == '<=':
            return self.eval(value[1],var_s) <= self.eval(value[2],var_s)
        elif op == 'step':
            for var in value:
                v = self.run(var,var_s)
            return v
        elif op == '&&':
            return (self.eval(value[1],var_s))and(self.eval(value[2],var_s))
        elif op == '||':
            return (self.eval(value[1],var_s))or(self.eval(value[2],var_s))
        elif op == 'if':
            if self.eval(value[1],var_s):
                return self.run(value[2],var_s)
        elif op == 'print':
            return print(self.eval(value[1],var_s))

engine = Engine()
#print(engine.eval(json.loads('["+", 4, 3]'),{}))
#print(engine.eval(json.loads('["*", 4, 3]'),{}))
#
#json2 = '''
#["step",
#  ["set", "i", 10],
#  ["set", "sum", 0],
#  ["until", ["==", ["get", "i"], 0], [
#    "step",
#    ["set", "sum", ["+", ["get", "sum"], ["get", "i"]]],
#    ["set", "i", ["+", ["get", "i"], -1]]
#  ]],
#  ["get", "sum"]
#]
#'''
#
#print(engine.eval(json.loads(json2),{}))
#print(engine.eval(json.loads('["&&",["==",3,3],["==",3,3]]'),{}))
#print(engine.eval(json.loads('["if",["==",3,3],["print",3]]'),{}))

s = input()
print(s)

