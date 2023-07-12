const sinon = require('sinon');
const { assert } = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    consoleSpy.restore();
  });

  it('validate the usage of the Utils function', () => {
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);

    assert(calculateNumberSpy.calledWith('SUM', 100, 20));
    assert(consoleSpy.calledWith('The total is: 120'));

    calculateNumberSpy.restore();
  });
});
