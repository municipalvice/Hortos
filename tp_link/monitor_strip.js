#!/usr/bin/env node

const util = require('util');
const { Client } = require('tplink-smarthome-api');

const client = new Client({
  defaultSendOptions: { timeout: 20000, transport: 'tcp' },
});


const logEvent = function logEvent(eventName, device, state) {
  const stateString = state != null ? util.inspect(state) : '';
  console.log(
    `${new Date().toISOString()} ${eventName} ${device.model} ${device.host}:${
      device.port
    } ${device.childId} ${stateString}`
  );
};

const monitorEvents = function monitorEvents(device) {
  // Device (Common) Events
  // device.on('emeter-realtime-update', (emeterRealtime) => {
  //   logEvent('emeter-realtime-update', device, emeterRealtime);
  // });

  // Plug Events
  device.on('power-on', () => {
    logEvent('power-on', device);
  });
  device.on('power-off', () => {
    logEvent('power-off', device);
  });
  device.on('power-update', (powerOn) => {
    logEvent('power-update', device, powerOn);
  });
  // device.on('in-use', () => {
  //   logEvent('in-use', device);
  // });
  // device.on('not-in-use', () => {
  //   logEvent('not-in-use', device);
  // });
  // device.on('in-use-update', (inUse) => {
  //   logEvent('in-use-update', device, inUse);
  // });

  device.startPolling(5000);
};

(async () => {
  const device = await client.getDevice({ host: '192.168.0.229' });

  console.log(device.alias);

  if (!device.children) {
    console.log('device has no children');
    return;
  }

  device.children.forEach((child) => {
    console.log(child);
  });

  await Promise.all(
    Array.from(device.children.keys(), async (childId) => {
      const childPlug = await client.getDevice({ host: '192.168.0.229', childId });
      monitorEvents(childPlug);
    })
  );

  monitorEvents(device);
})();