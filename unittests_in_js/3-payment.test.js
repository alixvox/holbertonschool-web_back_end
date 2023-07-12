const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');
const { assert } = require('chai');

describe('sendPaymentRequestToApi', function() {
  let consoleSpy;

  beforeEach(function() {
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(function() {
    consoleSpy.restore();
  });

  it('validate the usage of the Utils function', function() {
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);

    assert(calculateNumberSpy.calledWith('SUM', 100, 20));
    assert(consoleSpy.calledWith('The total is: 120'));

    calculateNumberSpy.restore();
  });
});
