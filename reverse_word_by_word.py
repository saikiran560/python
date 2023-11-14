class py_solution:
    def reverse_words(self, s):
        s=input("nter string::")
        return ' '.join(reversed(s.split()))


print(py_solution().reverse_words("s"))
