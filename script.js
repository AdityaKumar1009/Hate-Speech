async function predict() {
  const text = document.getElementById("inputText").value;

  const response = await fetch("/predict", {
      method: "POST",
      headers: {
          "Content-Type": "application/json"
      },
      body: JSON.stringify({ text: text })
  });

  const data = await response.json();
  const resultDiv = document.getElementById("result");

  if (data.error) {
      resultDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
  } else {
      let predictions = data.predictions[0]
          .map(p => `${p.label}: ${(p.score * 100).toFixed(2)}%`)
          .join("<br>");
      resultDiv.innerHTML = `<strong>Input:</strong> ${data.input}<br><br><strong>Predictions:</strong><br>${predictions}`;
  }
}
