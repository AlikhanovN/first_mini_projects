class Abonent():
    id =  1
    abonent_list = []
    abonent_overlimit = []
    def __init__(self, fio:str, address:str, credit_card:int, card_type:str, speaking_time:int):
        self.id = Abonent.id
        self.validation_fio(fio)
        self.fio = fio
        self.validation_adres(address)
        self.adres = address
        self.validation_credcard(credit_card)
        self.credit_card = credit_card
        self.validation_cardtype(card_type)
        self.card_type = card_type
        self.validation_time(speaking_time)
        self.speaking_time = speaking_time
        Abonent.id += 1
        Abonent.abonent_list.append({
            "ID": self.id,
            "fio": self.fio,
            "adres": self.adres,
            "credit_card": self.credit_card,
            "card_type": self.card_type,
            "speaking_time": self.speaking_time
        })
        if speaking_time > 50:
            Abonent.abonent_overlimit.append(fio)

    def print_info(self):
#         return f"""
#     {self.id} - {self.fio}
#     Address - {self.adres}
#     Credit card number - {self.credit_card}
#     Card type - {self.card_type}
#     Speaking time - {self.speaking_time}
# """
        return sorted(Abonent.abonent_list, key=lambda i:i["fio"])

    def print_over(self):
        return Abonent.abonent_overlimit

    def set(self, fio):
        self.validation_fio(fio)
        self.fio = fio

    @classmethod
    def validation_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("Enter string only")
        if len(fio.split()) != 3:
            raise ValueError("Enter full Name")
    @classmethod
    def validation_adres(cls, adr):
        if type(adr) != str:
            raise TypeError("Enter string only")
    @classmethod
    def validation_credcard(cls, credc):
        if type(credc) != int:
            raise TypeError("Enter only numbers")
        if len(str(credc)) != 16:
            raise ValueError("Enter 16 numbers")
    @classmethod
    def validation_cardtype(cls, cardt):
        if type(cardt) != str:
            raise TypeError("Enter string only")
        if cardt != "Debet" and cardt != "Credit":
            raise ValueError("Enter - 'Debet' or 'Credit'")
    @classmethod
    def validation_time(cls, speakt):
        if type(speakt) != int:
            raise TypeError("Enter only numbers")



Alex = Abonent("Alikhanov Namiq N", "Baku", 1234123412341234, "Debet", 55)
Sam = Abonent("AAJony Sam D", "UK", 1234123412341234, "Credit", 32)
Sam.set("Jayson Stethem O")
print(Alex.print_info())
print(Alex.print_over())
# print(Sam.print_info())
