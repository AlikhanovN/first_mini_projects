class ContactList(list):
    all_contacts = ["Sam", "Jenny", "Jon", "Samuel"]
    def search_by_name(self):
        self.find = input("Enter name for search: ")
        for i in ContactList.all_contacts:
            if self.find.lower() in i.lower():
                print(i, end=", ")

a = ContactList()
print(a.search_by_name())
