class calculate_bow:
    def __init__(self, length):
        self.length = length
        baseline_length = 124
        self.length_ratio = self.length/baseline_length
        self.user_sectors = self.calculate_sectors()
        print(type(self.user_sectors))

    def calculate_sectors(self):
        baseline_sectors = {'A': 16, 'B': 26, 'C': 14, 'D_half': 6}

        user_sectors = {}

        for sector in baseline_sectors:
            user_sectors[sector] = round(
                baseline_sectors[sector]*self.length_ratio, 1)

        return user_sectors

    def print_values(self):
        total = 0
        for sector in self.user_sectors:
            print(f"{sector}: {self.user_sectors[sector]} cm")
            total = total+self.user_sectors[sector]
        print(f"with rounding, that is {total*2} cm")


bow_length = input('please enter length of your bow in cm: ')
my_bow = calculate_bow(int(bow_length))
my_bow.print_values()
