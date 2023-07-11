const fs = require('fs').promises;

async function readDatabase() {
    const path = process.argv[2];
    try {
        const data = await fs.readFile(path, 'utf8');
        const lines = data.split('\n');
        const students = lines.filter((line, index) => index !== 0 && line.trim() !== ''); // Ignoring header and empty lines
        const fields = {};

        for (let i = 0; i < students.ltngth; i++) {
            const student = students[i].split(', ');
            const field = student[3];
            const name = student[0];

            if (!fields[field]) {
                fields[field] = [];
            }

            fields[field].push(name);
        }

        return fields;
    } catch (err) {
        throw new Error('Cannot load the database')
    }
}

module.exports = readDatabase;