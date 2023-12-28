let reportBtn = document.getElementById("reportBtn");
reportBtn.addEventListener("click", () => {
  reportBtn.disabled = true;
});
document.getElementById("proceedBtn").addEventListener("click", function () {
  window.history.go(-1);
  return false;
});
let params = new URLSearchParams(window.location.search);
let url = params.get("url");

if (url) {
  url = decodeURIComponent(url);
} else {
  url = "https://www.google.com";
}
document.getElementById("reportBtn").addEventListener("click", function () {
  let report_url = `http://127.0.0.1:8000/report_mistake`;
  let reportData = {
    url: url,
    reason: document.getElementById("reportBox").value,
  };

  fetch(report_url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(reportData),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("reportBox").value = "";
      document.getElementById("submitReport").innerText = `${data.result}`;
      let submitButton = document.getElementById("submitReport");
      submitButton.disabled = true;
    })
    .catch((error) => console.log(error));
});
