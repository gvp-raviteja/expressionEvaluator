__author__  = 'hema_ganireddy'
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

d1={}

def remove_spaces(line):
    str=''
    i=0
    flag=0
    while i< len(line):
        if(line[i-1]==' ' and line[i].isdigit() and flag==1):
            return -1
        if(line[i].isdigit()):
            str=str+line[i]
            flag=1
            i=i+1
            continue
        if(line[i]!=' '):
            str=str+line[i]
        i=i+1
    return str

def generate_tokens(s):
    i=0
    l1=[]
    k=''
    flag=0
    while i<len(s):
        if(s[i].isdigit()):
            k=k+s[i]
            flag=1
            i=i+1
            continue
        elif(flag==1):
            l1.append(k)
            k=''
            flag=0
        """if(s[i]=="\n"):
            i=i+1
            continue"""
        l1.append(s[i])
        i=i+1
    if(flag==1):
        l1.append(k)
    return l1

def generate_parse_tree(l1):
    if(len(l1)>=3):
        root=node(l1[1])
        root.left=generate_parse_tree(l1[:1])
        root.right=generate_parse_tree(l1[2:])
    elif(len(l1)==2):
        root=node(l1[1])
        root.left=generate_parse_tree(l1[:1])
    elif(len(l1)==1):
        root=node(l1[0])
    else:
        return None
    return root

def is_initialized(var):
    try:
        x=d1[var]
        return True
    except KeyError:
        print var," is not initialized"
        return False

def error_checker(root):
    if(root is not None):
        if root.left is None and root.right is None:
            if(root.data.isdigit() ):
                return True
            elif(not('a'<=root.data<='z' or 'A'<=root.data<='Z')):
                return False
            else:
                return is_initialized(root.data)
        elif(root.left is not None and root.right is not None):
            if(root.data=='+' or root.data=='-' or root.data=='*' or root.data=='/' or root.data=='>'or root.data=='<'or root.data=='='):
                x=error_checker(root.left)
                y=error_checker(root.right)
                if(x is True and y is True):
                    return True
                return False
        elif(root.left is None or root.right is None):
            return False

def parser(root):
    if(('a'<=root.data<='z' or 'A'<=root.data<='Z') and root.left==None and root.right==None):
        if(is_initialized(root.data)):
            print"value of",root.data," is",d1[root.data]
        else:
            print "value is not initialazed"
        return False
    if(root is None or root.data!="="):
        return False
    if(not('a'<=root.left.data<='z' or 'A'<=root.left.data<='Z')):
        return False
    x=error_checker(root.right)
    return x

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if(y==0):
        return False
    return x/y

def compute(root):
    global d1
    if(root is not None):
        if(root.left is None and root.right is None):
            if(root.data.isdigit()):
                return int(root.data)
            #if('a'<=root.data<='b' or 'A'<=root.data<='Z'):
            return d1[root.data]
        elif(root.left is not None and root.right is not None):
            x=compute(root.left)
            y=compute(root.right)
            if(root.data=='+'):
                return add(x,y)
            if(root.data=='-'):
                return subtract(x,y)
            if(root.data=='*'):
                return multiply(x,y)
            if(root.data=='/'):
                return divide(x,y)

def evaluator(root):
    global d1
    d1[root.left.data]=compute(root.right)
    if(d1[root.left.data]!=False):
        print "value of ",root.left.data," is",d1[root.left.data]

def expression_evaluator(line):
    string = remove_spaces(line)
    print string
    if (string == -1):
        print "syntax error"
    else:
        l1 = generate_tokens(string)
        print l1
        root = generate_parse_tree(l1)
        x = parser(root)
        if (x == False):
            print("syntax not supported")
        else:
            evaluator(root)

if __name__=="__main__":
    #fp=open("sample_code.txt",'rt')
    #str=''
    while(1):
        str=raw_input("enter the expression")
        if(str=="exit"):
            break
        expression_evaluator(str)
