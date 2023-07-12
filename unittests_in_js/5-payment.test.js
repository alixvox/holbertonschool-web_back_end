const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToAPI = require('./5-payment.js');
const Utils = require('./utils.js');

describe('sendPaymentRequestToAPI', function() {
  let consoleSpy;

  beforeEach(function() {
    // Before each test, set up the spy on console.log
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(function() {
    // After each test, restore the console.log to its original state
    consoleSpy.restore();
  });

  it('logs correct output for 100, 20', function() {
    sendPaymentRequestToAPI(100, 20);
    expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
  });

  it('logs correct output for 10, 10', function() {
    sendPaymentRequestToAPI(10, 10);
    expect(consoleSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
  });
});
