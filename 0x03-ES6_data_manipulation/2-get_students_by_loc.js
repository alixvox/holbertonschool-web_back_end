export default function getListStudentIds(students, city) {
  return students.filter((student) => student.location === city);
}
