def defangIPaddr(self, address):
        defanged = ''
        for i in address:
            if i == '.':
                defanged += '[.]'
            else:
                defanged += i
        return defanged
        
def defangIPaddr(self, address):
        return address.replace('.', '[.]')
        
def defangIPaddr(self, address):
        add_split = address.split('.')
        new = '[.]'.join(add_split)
        return new
        
