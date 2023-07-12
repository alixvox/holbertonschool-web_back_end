const fs = require('fs').promises;

async function readDatabase() {
  const data = await fs.readFile(process.argv[2], 'utf8');
  const lines = data.split('\n');
  const fields = {};

  for (let i = 1; i < lines.length; i++) {
    const student = lines[i].split(',');
    const name = student[0];
    const field = student[3];

    if (!name || !field) {
      continue;  // Ignore lines with missing or improperly formatted data
    }

    if (!fields[field]) {
      fields[field] = [];
    }

    fields[field].push(name);
  }

  return fields;
}

module.exports = readDatabase;
