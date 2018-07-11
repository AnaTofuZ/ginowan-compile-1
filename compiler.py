#!/usr/bin/env python3

import json

class Generete():

    def check(self,value,var):
        if isinstance(value,list):
            return self.run(value,var)
        return value

    def run(self,value,var):
        op = value[0]

        if op == '+':
            return self.check(value[1],var) + self.check(value[2],var)
        elif op == '*':
            return self.check(value[1],var) * self.check(value[2],var)
        elif op == 'set':
            var[self.check(value[1],var)] = self.check(value[2],var)
        elif op == 'get':
            return var[self.check(value[1],var)]
        elif op == 'step':
            for var_l in value[1:]:
                f = self.run(var_l,var)
            return f
hoge = Generete()

print(hoge.run(json.loads('["+",3,2]'),{}))
print(hoge.run(json.loads('["+",["*",3,3],2]'),{}))
print(hoge.run(json.loads('["set","i",32]'),{}))
print(hoge.run(json.loads('["step",["set","i",32],["get","i"]]'),{}))
