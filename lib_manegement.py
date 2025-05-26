class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id

    def display_info(self):
        print(f"Member Name: {self.name}")
        print(f"Membership ID: {self.membership_id}")

class StudentMember(Member):
    def __init__(self, name, membership_id):
        super().__init__(name, membership_id)
        self.borrowed_books = 0

    def add_book(self):
        self.borrowed_books += 1
        print(f"Book added. Total borrowed books: {self.borrowed_books}")

    def return_book(self):
        if self.borrowed_books > 0:
            self.borrowed_books -= 1
            print(f"Book returned. Total borrowed books: {self.borrowed_books}")
        else:
            print("No books to return.")

    def display_borrowing_status(self):
        print(f"{self.name} (ID: {self.membership_id}) has borrowed {self.borrowed_books} books.")

if __name__ == "__main__":
    student_member = StudentMember("Harshil","23DCE081")
    student_member.display_info()
    student_member.add_book()
    student_member.add_book()
    student_member.display_borrowing_status()
    student_member.return_book()
    student_member.display_borrowing_status()