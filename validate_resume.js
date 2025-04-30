const fs = require('fs');
const resumeSchema = require('@jsonresume/schema');

// Get the filename from command line arguments or use default
const filename = process.argv[2] || 'example.json';

try {
  const resumeObject = JSON.parse(fs.readFileSync(filename, 'utf8'));
  
  resumeSchema.validate(resumeObject, (err, report) => {
    if (err) {
      console.error('The resume was invalid:', err);
      process.exit(1);
    }
    console.log('Resume validated successfully!');
    console.log('Report:', JSON.stringify(report, null, 2));
    process.exit(0);
  });
} catch (error) {
  console.error('Error reading or parsing the resume file:', error.message);
  process.exit(1);
}