export default function createReportObject(employeesList) {
const obj = {
    allEmployees: { ...employeesList },
    getNumberOfDepartments(employeesList) {
        return employeesList.departments.length;
        },
    };
    return obj;
}
