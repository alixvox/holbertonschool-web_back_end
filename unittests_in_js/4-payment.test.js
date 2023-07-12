// 4-payment.test.js
const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  let consoleSpy;
  let stubUtils;

  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
    stubUtils = sinon.stub(Utils, 'calculateNumber');
    stubUtils.returns(10);
  });

  afterEach(() => {
    consoleSpy.restore();
    stubUtils.restore();
  });

  it('validate the usage of the Utils function', () => {
    sendPaymentRequestToApi(100, 20);
    expect(stubUtils.calledWith('SUM', 100, 20)).to.be.true;
    expect(consoleSpy.calledWith('The total is: 10')).to.be.true;
    expect(consoleSpy.calledOnce).to.be.true;
  });
});
