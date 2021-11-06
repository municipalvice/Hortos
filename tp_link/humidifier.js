#!/usr/bin/env node

import { plugs } from '../keys/keys.js';
const util = require('util');
const { Client } = require('tplink-smarthome-api');

const humidifier = plugs.HUMIDIFIER;

const client = new Client({
    defaultSendOptions: { timeout: 20000, transport: 'tcp' },
});

function turnHumidifierOn() {
    client.getDevice({ host: '192.168.0.229', childId: humidifier })
    .then((plug) => {
        plug.setPowerState(true);
        plug.getSysInfo().then(console.log);
    }).catch(console.log);
}
function turnHumidifierOff() {
    client.getDevice({ host: '192.168.0.229', childId: humidifier })
    .then((plug) => {
        plug.setPowerState(false);
        plug.getSysInfo().then(console.log);
    }).catch(console.log);
}

function keepHumidityInRange() {
    const max_humidity = 80.0;
    const min_humidity = 55.0;

    // Call hortos.py every 60 s, returns as JSON string {"temperature": 77.0, "humidity": 64.7}
    if (reading.humidity <=  min_humidity) {
        turnHumidifierOn();
    } else if (reading.humidity >= max_humidity) {
        turnHumidifierOff();
    }
}