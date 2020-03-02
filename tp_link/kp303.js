#!/usr/bin/env node

const { Client } = require('tplink-smarthome-api');

const client = new Client();

client.getDevice({ host: '192.168.0.20' }).then(device => {
  device.getSysInfo().then(console.log);
});

