const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('returns rounded sum', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });
  it('rounds floats and returns their sum', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });
  it('rounds 1.5 up', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
});
