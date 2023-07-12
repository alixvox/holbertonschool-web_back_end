const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  it('returns rounded sum when type is SUM', () => {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
  });
  it('returns rounded difference when type is SUBTRACT', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });
  it('returns rounded division when type is DIVIDE', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });
  it('returns Error when type is DIVIDE and b is 0', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
  it('returns Error when type is not SUM, SUBTRACT, or DIVIDE', () => {
    assert.strictEqual(calculateNumber('MULTIPLY', 1.4, 4.5), 'Error');
  });
});
