const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function() {
  it('returns rounded sum', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });
  it('rounds floats and returns their sum', function() {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });
  it('rounds 1.5 up', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
});
