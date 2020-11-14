const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
    const { spawn } = require('child_process');
    // const pythonProcess = spawn('python3', ['model/test.py', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]);

    console.dir(req.query);

    const pythonProcess = spawn('python3', ['model/execute-model.py',
        req.query.age,
        req.query.height,
        req.query.weight,
        req.query.gender,
        req.query.systolicBloodPressure,
        req.query.diastolicBloodPressure,
        req.query.cholesterol,
        req.query.glucose,
        req.query.smoking,
        req.query.alcohol,
        req.query.physical
    ]);

    pythonProcess.stdout.on('data', (data) => {
        console.dir(data);
        console.log(data.toString());
        res.send(data.toString());
        res.end();
    });
});

app.get('/test', (req, res) => {
    res.send("Test!");
});

app.listen(port, '0.0.0.0', () => {
    console.log(`Example app listening at http://localhost:${port}`);
});
