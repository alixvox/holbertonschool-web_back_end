const chai = require('chai');

const { expect } = chai;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  it('returns rounded sum when type is SUM', () => {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });
  it('returns rounded difference when type is SUBTRACT', () => {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });
  it('returns rounded division when type is DIVIDE', () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });
  it('returns Error when type is DIVIDE and b is 0', () => {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  });
  it('returns Error when type is not SUM, SUBTRACT, or DIVIDE', () => {
    expect(calculateNumber('MULTIPLY', 1.4, 4.5)).to.equal('Error');
  });
});
