export default function getListStudentIds(list) {
  try {
    return list.map((map) => map.id);
  } catch (error) {
    return [];
  }
}
