class Student:
    def __init__(self, id_card, exam_number, name, address):
        self.id_card = id_card
        self.exam_number = exam_number
        self.name = name
        self.address = address


class StudentA(Student):
    def __init__(self, id_card, exam_number, name, address, math, physics, chemistry):
        super().__init__(id_card, exam_number, name, address)
        self.math = math
        self.physics = physics
        self.chemistry = chemistry

    def calculate_score(self):
        return self.math * 1.5 + self.physics + self.chemistry


class StudentB(Student):
    def __init__(self, id_card, exam_number, name, address, math, chemistry, biology):
        super().__init__(id_card, exam_number, name, address)
        self.math = math
        self.chemistry = chemistry
        self.biology = biology

    def calculate_score(self):
        return self.math + self.chemistry + self.biology * 1.5


class ManageStudent:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student_by_exam_number_or_id(self, search_key):
        for student in self.students:
            if student.exam_number == search_key or student.id_card == search_key:
                return student
        return None

    def remove_student(self, exam_number):
        for i, student in enumerate(self.students):
            if student.exam_number == exam_number:
                del self.students[i]
                return True
        return False

    # def display_students_by_block(self, block):
    #     block_students = [student for student in self.students if isinstance(student, block)]
    #     for student in block_students:
    #         print(student.name, student.exam_number)

    def display_students_by_block(self, block):
        block_students = [student for student in self.students if isinstance(student, block)]
        for student in block_students:
            print(student.name, student.exam_number)

    def calculate_total_score(self, student):
        if isinstance(student, StudentA):
            return student.math * 1.5 + student.physics + student.chemistry
        elif isinstance(student, StudentB):
            return student.math + student.chemistry + student.biology * 1.5
        else:
            return 0

    def students_with_no_fails(self):
        return [student for student in self.students if self.calculate_total_score(student) >= 2]

    def calculate_average_score(self):
        total_score = 0
        count = 0
        for student in self.students:
            total_score += self.calculate_total_score(student)
            count += 1
        if count > 0:
            return total_score / count
        return 0

    def sort_students_by_score(self, block, reverse_order=False):
        block_students = [student for student in self.students if isinstance(student, block)]
        block_students.sort(key=lambda student: self.calculate_total_score(student), reverse=reverse_order)
        return block_students

    def students_achieving_scholarship(self, block):
        block_students = [student for student in self.students if isinstance(student, block)]
        block_students.sort(key=lambda student: self.calculate_total_score(student), reverse=True)
        top_students = [student for student in block_students if self.calculate_total_score(student) > 32][:5]
        return top_students


def main():
    manager = ManageStudent()

    student_a1 = StudentA("123456789", "A001", "Hoàng Đức Thiện", "Quảng Bình", 9.0, 8.5, 7.0)
    student_a2 = StudentA("987654321", "A002", "Trần Nam", "Hồ Chí Minh", 8.0, 7.5, 6.0)
    student_b1 = StudentB("111111111", "B001", "Nguyễn Kiều Anh", "Nghệ An", 7.0, 6.5, 8.0)
    student_b2 = StudentB("222222222", "B002", "Hoàng Thị Bê", "Hà Nội", 6.0, 5.5, 9.0)

    manager.add_student(student_a1)
    manager.add_student(student_a2)
    manager.add_student(student_b1)
    manager.add_student(student_b2)

    while True:
        print("---- Menu ----")
        print("1. Thêm mới thí sinh")
        print("2. Tìm kiếm thí sinh")
        print("3. Sửa thông tin thí sinh")
        print("4. Xoá thí sinh")
        print("5. Hiển thị danh sách thí sinh theo từng khối thi")
        print("6. Hiển thị danh sách thí sinh có điểm để xét vào đại học")
        print("7. Hiển thị danh sách thí sinh đạt học bổng")
        print("8. Hiển thị danh sách thí sinh không liệt môn nào")
        print("9. Thoát chương trình")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            id_card = input("Nhập số căn cước công dân: ")
            exam_number = input("Nhập số báo danh: ")
            name = input("Nhập họ tên: ")
            address = input("Nhập địa chỉ: ")

            block_choice = input("Chọn khối thi (A/B): ")
            if block_choice.upper() == "A":
                math = float(input("Nhập điểm Toán: "))
                physics = float(input("Nhập điểm Lý: "))
                chemistry = float(input("Nhập điểm Hóa: "))
                new_student = StudentA(id_card, exam_number, name, address, math, physics, chemistry)
            elif block_choice.upper() == "B":
                math = float(input("Nhập điểm Toán: "))
                chemistry = float(input("Nhập điểm Hóa: "))
                biology = float(input("Nhập điểm Sinh: "))
                new_student = StudentB(id_card, exam_number, name, address, math, chemistry, biology)
            else:
                print("Khối thi không hợp lệ.")
                continue

            manager.add_student(new_student)

        elif choice == "2":

            search_key = input("Nhập số báo danh hoặc số căn cước công dân: ")

            found_student = manager.find_student_by_exam_number_or_id(search_key)

            if found_student:
                print("Thông tin thí sinh:")

                print("Họ tên:", found_student.name)

                print("Số báo danh:", found_student.exam_number)

                print("Địa chỉ:", found_student.address)

        elif choice == "3":

            exam_number = input("Nhập số báo danh của thí sinh cần sửa: ")

            found_student = manager.find_student_by_exam_number_or_id(exam_number)

            if found_student:

                print("Thông tin thí sinh cần sửa:")

                print("Họ tên:", found_student.name)

                print("Số báo danh:", found_student.exam_number)

                print("Địa chỉ:", found_student.address)

                new_name = input("Nhập tên mới: ")

                new_address = input("Nhập địa chỉ mới: ")

                found_student.name = new_name

                found_student.address = new_address

                print("Thông tin thí sinh sau khi cập nhật:")

                print("Họ tên:", found_student.name)

                print("Số báo danh:", found_student.exam_number)

                print("Địa chỉ:", found_student.address)

            else:

                print("Không tìm thấy thí sinh có số báo danh này.")


        elif choice == "4":

            # Xoá thí sinh

            exam_number = input("Nhập số báo danh của thí sinh cần xoá: ")

            if manager.remove_student(exam_number):

                print("Thí sinh có số báo danh", exam_number, "đã được xoá.")

            else:

                print("Không tìm thấy thí sinh có số báo danh này.")


        elif choice == "5":

            block_choice = input("Chọn khối thi để hiển thị (A/B): ")

            if block_choice.upper() == "A":

                print("Danh sách thí sinh khối A:")

                manager.display_students_by_block(StudentA)

            elif block_choice.upper() == "B":

                print("Danh sách thí sinh khối B:")

                manager.display_students_by_block(StudentB)

            else:

                print("Khối thi không hợp lệ.")


        elif choice == "6":

            block_choice = input("Chọn khối thi để hiển thị (A/B): ")

            if block_choice.upper() == "A":

                print("Danh sách thí sinh khối A có điểm để xét vào đại học:")

                students = manager.sort_students_by_score(StudentA)

                for student in students:

                    if manager.calculate_total_score(student) >= 2:
                        print(f"{student.name}: {manager.calculate_total_score(student)}")

            elif block_choice.upper() == "B":

                print("Danh sách thí sinh khối B có điểm để xét vào đại học:")

                students = manager.sort_students_by_score(StudentB)

                for student in students:

                    if manager.calculate_total_score(student) >= 2:
                        print(f"{student.name}: {manager.calculate_total_score(student)}")

            else:

                print("Khối thi không hợp lệ.")


        elif choice == "7":

            block_choice = input("Chọn khối thi để hiển thị (A/B): ")

            if block_choice.upper() == "A":

                print("Danh sách thí sinh khối A đạt học bổng:")

                students = manager.students_achieving_scholarship(StudentA)

                for student in students:
                    print(f"{student.name}: {manager.calculate_total_score(student)}")

            elif block_choice.upper() == "B":

                print("Danh sách thí sinh khối B đạt học bổng:")
                students = manager.students_achieving_scholarship(StudentB)
                for student in students:
                    print(f"{student.name}: {manager.calculate_total_score(student)}")

            else:

                print("Khối thi không hợp lệ.")


        elif choice == "8":
            print("Danh sách thí sinh không liệt môn nào:")
            students_no_fails = manager.students_with_no_fails()
            for student in students_no_fails:
                print(student.name)


        elif choice == "9":
            print("Chương trình kết thúc. Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()
