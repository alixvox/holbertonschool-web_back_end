export default function getStudentIdsSum(students) {
  return students.reduce(
    (prevValue, currValue) => prevValue + currValue.id, 0,
  );
}
