class Zoo:
    def get_ticket_price(self, age):
        if age < 0: #add cases for negative age
            return "Don't have negative age"
        elif 0 <= age <= 12: #from if 0 < age <= 12 to elif 0 <= age <= 12 because 0 must be in this condition
            return 50
        elif 13 <= age <= 20: #from elif 13 <= age < 20 to elif 13 <= age <= 20 because 20 must be in this condition
            return 100
        elif 21 <= age <= 60: #from elif 21 < age <= 60 to elif 21 <= age <= 60 because 13 must be in this condition
            return 150
        elif age > 60: #from  elif age >= 60 to elif age > 60 because 60 must be in previous condition
            return 100