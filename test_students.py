import unittest
from student import ManageStudent, StudentA, StudentB


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.manager = ManageStudent()
        self.student_a1 = StudentA("123456789", "A001", "Alice", "123 Main St", 9.0, 8.5, 7.0)
        self.student_a2 = StudentA("987654321", "A002", "Bob", "456 Oak St", 8.0, 7.5, 6.0)
        self.student_b1 = StudentB("111111111", "B001", "Charlie", "789 Elm St", 7.0, 6.5, 8.0)
        self.student_b2 = StudentB("222222222", "B002", "David", "012 Pine St", 6.0, 5.5, 9.0)

        self.manager.add_student(self.student_a1)
        self.manager.add_student(self.student_a2)
        self.manager.add_student(self.student_b1)
        self.manager.add_student(self.student_b2)

    def test_find_existing_student(self):
        found_student = self.manager.find_student_by_exam_number_or_id("A001")
        self.assertEqual(found_student.name, "Alice")

    def test_find_non_existing_student(self):
        found_student = self.manager.find_student_by_exam_number_or_id("C001")
        self.assertIsNone(found_student)

    def test_remove_existing_student(self):
        self.assertTrue(self.manager.remove_student("A001"))

    def test_remove_non_existing_student(self):
        self.assertFalse(self.manager.remove_student("C001"))

    # def test_display_students_block_A(self):
    #     students_block_a = self.manager.display_students_by_block(StudentA)
    #     self.assertEqual(len(students_block_a), 2)
    #
    # def test_display_students_block_B(self):
    #     students_block_b = self.manager.display_students_by_block(StudentB)
    #     self.assertEqual(len(students_block_b), 2)
    #
    # def test_students_with_no_fails(self):
    #     students_no_fails = self.manager.students_with_no_fails()
    #     self.assertEqual(len(students_no_fails), 4)
    #
    # def test_students_achieving_scholarship_block_A(self):
    #     scholarship_students_a = self.manager.students_achieving_scholarship(StudentA)
    #     self.assertEqual(len(scholarship_students_a), 2)
    #
    # def test_students_achieving_scholarship_block_B(self):
    #     scholarship_students_b = self.manager.students_achieving_scholarship(StudentB)
    #     self.assertEqual(len(scholarship_students_b), 2)


if __name__ == '__main__':
    unittest.main()
