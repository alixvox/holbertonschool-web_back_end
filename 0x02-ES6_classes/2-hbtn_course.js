export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(name) {
    if (typeof name !== 'string') throw Error('name must be a String');
    this._name = name;
  }

  set length(length) {
    if (typeof length !== 'number') throw Error('length must be a Number');
    this._length = length;
  }

  set students(students) {
    if (!Array.isArray(students)) throw Error('students must be an Array');
    for (const x of students) {
      if (typeof x !== 'string') throw Error('students must contain Strings');
    }
    this._students = students;
  }
}
