function predict() {
  const text = document.getElementById("text-input").value;

  fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: `text=${encodeURIComponent(text)}`,
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById(
        "result"
      ).innerText = `Prediction: ${data.prediction}`;
    })
    .catch((err) => console.error(err));
}
