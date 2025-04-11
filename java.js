const { spawn } = require('child_process');

// java.js

// Spawn a Python process to execute aap.py
const pythonProcess = spawn('python', ['aap.py']);

// Capture the output from the Python script
pythonProcess.stdout.on('data', (data) => {
    console.log(`Output from Python script: ${data.toString()}`);
});

// Capture any errors from the Python script
pythonProcess.stderr.on('data', (data) => {
    console.error(`Error from Python script: ${data.toString()}`);
});

// Handle the close event
pythonProcess.on('close', (code) => {
    console.log(`Python script exited with code ${code}`);
});