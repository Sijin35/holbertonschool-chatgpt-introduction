class Checkbook:
    """
    Function Description:
        A class that simulates a simple checkbook system.
        It allows users to deposit money, withdraw money,
        and check their current account balance.

    Parameters:
        None

    Returns:
        None
    """

    def __init__(self):
        """
        Function Description:
            Initializes the checkbook account with a starting balance of 0.

        Parameters:
            None

        Returns:
            None
        """

        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
            Adds money to the current account balance.

        Parameters:
            amount (float): The amount of money to deposit.

        Returns:
            None
        """

        self.balance += amount

        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
            Withdraws money from the account if sufficient funds exist.

        Parameters:
            amount (float): The amount of money to withdraw.

        Returns:
            None
        """

        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount

            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
            Displays the current account balance.

        Parameters:
            None

        Returns:
            None
        """

        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Function Description:
        Runs the main program loop and handles user interaction
        with the checkbook system.

    Parameters:
        None

    Returns:
        None
    """

    cb = Checkbook()

    while True:

        action = input(
            "What would you like to do? "
            "(deposit, withdraw, balance, exit): "
        )

        if action.lower() == 'exit':
            break

        elif action.lower() == 'deposit':

            try:
                amount = float(
                    input("Enter the amount to deposit: $")
                )

                cb.deposit(amount)

            except ValueError:
                print(
                    "Invalid input. "
                    "Please enter a numeric value."
                )

        elif action.lower() == 'withdraw':

            try:
                amount = float(
                    input("Enter the amount to withdraw: $")
                )

                cb.withdraw(amount)

            except ValueError:
                print(
                    "Invalid input. "
                    "Please enter a numeric value."
                )

        elif action.lower() == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
