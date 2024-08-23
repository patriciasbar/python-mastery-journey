class SuperList(list):
    def __len__(self):
        return 1000

print(len(SuperList()))
print(issubclass(SuperList, list))