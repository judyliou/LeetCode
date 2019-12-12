def toLowerCase(self, str):
        lowercase = ''
        for i in str:
            if ord(i) <= ord('Z') and ord(i) >= ord('A'):
                lowercase += chr(ord(i)+97-65)
            else:
                lowercase += i
        return lowercase
