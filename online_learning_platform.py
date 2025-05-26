class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"User Name: {self.name}")
        print(f"Email: {self.email}")

class Instructor(User):
    def __init__(self, name, email, subject_expertise):
        super().__init__(name, email)
        self.subject_expertise = subject_expertise
        self.uploaded_content = []

    def upload_content(self, content):
        self.uploaded_content.append(content)
        print(f"Content '{content}' uploaded successfully.")

    def display_info(self):
        super().display_info()
        print(f"Role: Instructor")
        print(f"Subject Expertise: {self.subject_expertise}")
        print(f"Uploaded Content: {', '.join(self.uploaded_content) if self.uploaded_content else 'No content uploaded.'}")

class CourseCreator(Instructor):
    def __init__(self, name, email, subject_expertise):
        super().__init__(name, email, subject_expertise)
        self.courses = {}

    def create_course(self, course_name, modules):
        self.courses[course_name] = modules
        print(f"Course '{course_name}' created with modules: {', '.join(modules)}")

    def display_info(self):
        super().display_info()
        print(f"Role: Course Creator")
        if self.courses:
            print("Courses Created:")
            for course, modules in self.courses.items():
                print(f"  - {course}: Modules -> {', '.join(modules)}")
        else:
            print("Courses Created: None")

if __name__ == "__main__":
    user = User("Harshil", "pharshil748@gmail.com")
    user.display_info()
    print("\n---\n")
    instructor = Instructor("Harnish", "harnish697@gmail.com", "Mathematics")
    instructor.display_info()
    instructor.upload_content("Introduction to Calculus")
    instructor.upload_content("Linear Algebra Basics")
    instructor.display_info()
    print("\n---\n")
    course_creator = CourseCreator("Tirth", "tirth1705@gmail.com", "Computer Science")
    course_creator.display_info()
    course_creator.upload_content("Data Structures and Algorithms")
    course_creator.create_course("Python Programming", ["Introduction", "Data Types", "Control Structures", "Functions", "Modules"])
    course_creator.create_course("Web Development", ["HTML", "CSS", "JavaScript", "Frontend Frameworks", "Backend Development"])
    course_creator.display_info()