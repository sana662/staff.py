class Staff:
    """
    Represents a staff member submitting a requisition.

    Design Principle: Encapsulation
    This class bundles staff-related data (staff_id, name) together
    with a method that operates on that data (display_info). This
    keeps related data and behavior grouped in one place, rather
    than passing loose variables around the program.
    """

    def __init__(self, staff_id, name):
        self.staff_id = staff_id
        self.name = name

    def display_info(self):
        """
        Displays the staff member's details.

        Design Principle: Single Responsibility Principle (SRP)
        This method has one job — formatting and printing staff info.
        It doesn't handle requisition logic, keeping the class focused.
        """
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.name}")


# Example usage
if __name__ == "__main__":
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")

    staff_member = Staff(staff_id, staff_name)
    staff_member.display_info() 