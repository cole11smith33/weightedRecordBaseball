const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname, 'website'))); // specifies the filepath from the working directory to the website directory

app.get('/results', (req, res) => {
  res.sendFile(path.join(__dirname, 'outputResults', '2015_results.csv'));
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
