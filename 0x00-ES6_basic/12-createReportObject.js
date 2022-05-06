export default function createReportObject(employeesList) {
  const obj = {
    allEmployees: { ...employeesList },
    getNumberOfDepartments(employeesList) {
      return Object.keys(employeesList).length;
    },
  };
  return obj;
}
