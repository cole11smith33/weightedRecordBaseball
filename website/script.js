//Following code was written with chatGPT (only this file)

async function loadCSV(url) {
  const response = await fetch(url);
  const text = await response.text();

  // Split into rows and then into cells
  const rows = text.trim().split("\n").map(row => row.split(","));
  return rows;
}

function renderTable(rows, containerId) {
  const container = document.getElementById(containerId);
  const table = document.createElement("table");

  rows.forEach((row, rowIndex) => {
    const tr = document.createElement("tr");
    row.forEach(cell => {
      const el = document.createElement(rowIndex === 0 ? "th" : "td");
      el.textContent = cell;
      tr.appendChild(el);
    });
    table.appendChild(tr);
  });

  container.appendChild(table);
}

// Load and render when page loads
document.addEventListener("DOMContentLoaded", () => {
  loadCSV("2015_results.csv").then(rows => {
    renderTable(rows, "CSVTable");
  });
});
