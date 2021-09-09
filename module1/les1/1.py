class MyList(list):
    def new_len(self):
        return len(self)


lst = MyList()

lst.append(1)
lst.append(2)
lst.append(-2)
lst.sort()

print(lst)
print(lst.new_len())