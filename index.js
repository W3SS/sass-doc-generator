var PythonShell = require('python-shell');

var input = process.argv[2];
var output = process.argv[3];

var options = {
	mode: 'text',
	pythonOptions: ['-u'],
	scriptPath: '.',
	args: ['-i', input, '-o', output]
};

PythonShell.run('main.py', options, function (err, results) {
	if (err) throw err;
	// results is an array consisting of messages collected during execution
	console.log('results: %j', results);
	console.log(input + ' ' + output);
});
