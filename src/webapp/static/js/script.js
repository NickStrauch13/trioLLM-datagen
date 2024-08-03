document.addEventListener("DOMContentLoaded", function () {
  const addFewshotButton = document.getElementById("addFewshotButton");
  const fewshotInputContainer = document.getElementById(
    "fewshotInputContainer"
  );
  const submitButton = document.getElementById("submitButton");
  const downloadButton = document.getElementById("downloadButton");
  const dataSampleCount = document.getElementById("dataSampleCount");
  const queryInput = document.getElementById("queryInput");
  const loadingContainer = document.getElementById("loadingContainer");
  const loadingBar = document.getElementById("loadingBar");
  const loadingText = document.getElementById("loadingText");
  let inputCount = 1;
  let csvContent = "";

  downloadButton.disabled = true;

  addFewshotButton.addEventListener("click", function () {
    if (inputCount < 3) {
      inputCount++;
      const newTextInputContainer = document.createElement("div");
      newTextInputContainer.classList.add("large-text-input-container");
      newTextInputContainer.innerHTML = `<textarea type="text" id="fewshotInput${inputCount}" class="textarea-box" placeholder="Optional few-shot input"></textarea>`;
      fewshotInputContainer.insertAdjacentElement(
        "afterend",
        newTextInputContainer
      );
      if (inputCount === 3) {
        addFewshotButton.disabled = true;
      }
    } else {
      addFewshotButton.disabled = true;
    }
  });

  submitButton.addEventListener("click", async function () {
    const count = parseInt(dataSampleCount.value);
    console.log(count);
    const topic = queryInput.value;
    const fewShotExamples = Array.from(
      { length: inputCount },
      (_, i) => document.getElementById(`fewshotInput${i + 1}`)?.value || ""
    ).filter((v) => v);

    const results = [];

    loadingContainer.style.display = "flex";

    for (let i = 0; i < count; i++) {
      const response = await fetch("/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          topic: topic,
          few_shot_examples: fewShotExamples,
        }),
      });

      if (response.ok) {
        const data = await response.json();
        results.push(data.output);
      } else {
        console.error("Error fetching from /generate");
      }

      // Update loading bar width
      const progress = ((i + 1) / count) * 100;
      loadingBar.style.width = `${progress}%`;
      if (progress === 100) {
        loadingText.textContent = "Done!";
      }
    }

    csvContent =
      "data:text/csv;charset=utf-8," +
      results.map((e) => `"${e.replace(/"/g, '""')}"`).join("\n");

    downloadButton.disabled = false; // Enable the download button
  });

  downloadButton.addEventListener("click", function () {
    if (csvContent) {
      const encodedUri = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", "results.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link); // Clean up
    }
  });
});
