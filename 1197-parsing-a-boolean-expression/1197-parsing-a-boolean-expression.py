class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack=[]
        for i in expression:
            if i in ('(', '!', '&', '|', 't','f'):
                stack.append(i)
            elif i==')':
                t_c=0
                f_c=0
                while stack[-1]!='(':
                    e=stack.pop()
                    if e=='t':
                        t_c+=1
                    else:
                        f_c+=1
                stack.pop()
                op=stack.pop()
                if op=='&':
                    if f_c==0:
                        stack.append('t')
                    else:
                        stack.append('f')
                elif op=='|':
                    if t_c!=0:
                        stack.append('t')
                    else:
                        stack.append('f')
                else:
                    if t_c:
                        stack.append('f')
                    else:
                        stack.append('t')
        return stack[-1]=='t'