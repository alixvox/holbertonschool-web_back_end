export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const st = newGrades.filter((grade) => grade.studentId === student.id);
      const grade = st.length ? st[0].grade : 'N/A';
      return { ...student, grade };
    });
}
