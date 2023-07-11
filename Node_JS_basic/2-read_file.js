const fs = require('fs');

function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf8'); 
        const lines = data.split('\n');
        const students = lines.filter((line, index) => index !== 0 && line.trim() !== ''); // Ignore header and empty lines
        const count = students.length;
        let csCount = 0;
        let csStudents = [];
        let sweCount = 0; 
        let sweStudents = [];

        for (let i = 0; i < students.length; i++) { // start from index 0 since we've already removed the header
            const student = students[i].split(',');
            if (student[3] === 'CS') {
                csCount += 1;
                csStudents.push(student[0]);
            } else if (student[3] === 'SWE') {
                sweCount += 1;
                sweStudents.push(student[0]);
            }
        }

        console.log(`Number of students: ${count}`);
        console.log(`Number of students in CS: ${csCount}. List: ${csStudents.join(', ')}`);
        console.log(`Number of students in SWE: ${sweCount}. List: ${sweStudents.join(', ')}`)
    } catch (err) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;
