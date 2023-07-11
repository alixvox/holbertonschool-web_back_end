const fs = require('fs');

function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf8');
        const lines = data.split('\n');
        let count = 0;
        let csCount = 0;
        let csStudents = [];
        let sweCount = [];
        let sweStudents = [];

        for (let i = 1; i < lines.length; i++) {
            const student = lines[i].split(',');
            if (student[3] === 'CS') {
                csCount += 1;
                csStudents.push(student[0]);
            } else if (student[3] === 'SWE') {
                sweCount += 1;
                sweStudents.push(student[0]);
            }
            count += 1;
        }

        console.log(`Number of students: ${count}`);
        console.log(`Number of students in CS: ${csCount}. List: ${csStudents.join(', ')}`);
        console.log(`Number of students in SWE: ${sweCount}. List: ${sweStudents.join(', ')}`)
    } catch (err) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;