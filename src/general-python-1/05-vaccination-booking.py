'''
COVID-19 Vaccination Booking
Available Vaccines:
(0) Pfizer - 3000 Bath/person
(1) Moderna - 3300 Bath/person
(2) Sinopharm - 3400 Bath/person
(3) Sinovac - 0 Bath/person
Invalid input. Please enter a valid number.
Invalid input. Please enter a valid number.
Invalid input. Please enter a valid number.
Invalid choice. Please choose 1, 2, 3, or 4.

Booking Summary:
Total number of vaccinations booked: 1
Total price of vaccine(s): 3000 Bath
Total customer name list(s): ['Gun']
'''

class VaccinationBooking:
    def __init__(self):
        self.vaccine_prices = {1: 3000, 2: 3300, 3: 3400, 4: 0}
        self.vaccine_name = ['Pfizer','Moderna','Sinopharm','Sinovac']
        self.customers = []

    def run(self):
        print("COVID-19 Vaccination Booking")
        print("Available Vaccines:")
        for idx, vn in enumerate(self.vaccine_name):
            print(f"({idx}) {vn} - {self.vaccine_prices[idx+1]} Bath/person")

        vaccine_choice = self.get_choice("vaccine")
        num_customers = self.get_choice("number of customers")

        self.customers = [self.get_customer_name(i + 1) for i in range(num_customers)]

        total_vaccinations = len(self.customers)
        total_price = total_vaccinations * self.vaccine_prices[vaccine_choice]

        print("\nBooking Summary:")
        print("Total number of vaccinations booked:", total_vaccinations)
        print("Total price of vaccine(s):", total_price, "Bath")
        print("Total customer name list(s):", self.customers)

    def get_choice(self, label):
        while True:
            try:
                choice = int(input(f"Enter your {label} choice: "))
                if choice in self.vaccine_prices:
                    return choice
                print("Invalid choice. Please choose 1, 2, 3, or 4.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_customer_name(self, customer_number):
        while True:
            customer_name = input(f"Enter name of customer {customer_number}: ")
            if customer_name.isalpha():
                return customer_name
            print("Invalid input. Please enter alphabet characters only.")


# Create an instance of VaccinationBooking and run the program
booking = VaccinationBooking()
booking.run()