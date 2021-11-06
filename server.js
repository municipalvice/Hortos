const express = require('express');
const { spawn } = require('child_process');
const app = express();
const port = 3420;

app.get('/', (request, response) => {
    python = spawn('python3', ['hortos.py']);
    let reading;

    python.stdout.on('data', (data) => {
        // console.log("This is the object response:", data)
        reading = data.toString()
        console.log("This is the String response:", data)
        // response.send(reading);
    })
    // python.on('close', (code) => {
    //     console.log(`child process close all stdio with code ${code}`);
    //     // response.send(reading);
    // })
})


app.listen(port, () => {
    console.log("App is on port: " + port);
})