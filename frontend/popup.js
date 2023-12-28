const server_url = "http://localhost:8000/";
let details_url = "";
let activeTabUrl = "";

chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
  let activeTab = tabs[0];
  activeTabUrl = activeTab.url;
  details_url = `${server_url}details?url=${encodeURIComponent(activeTabUrl)}`;

  fetch(details_url)
    .then((response) => response.json())
    .then((data) => {
      document.getElementById(
        "detail-1"
      ).innerText = `First seen: ${data.creation_date}`;
      document.getElementById(
        "detail-2"
      ).innerText = `Uses Dnssec: ${data.dnssec}`;
      document.getElementById(
        "detail-3"
      ).innerText = `Country: ${data.country_name}`;
      document.getElementById(
        "detail-4"
      ).innerText = `Organization : ${data.registrant}`;
      document.getElementById("siteUrl").innerText = `${data.domain}`;
    })
    .catch((error) => console.log(error));
});

const report_url = `${server_url}report`;

document.getElementById("submitReport").addEventListener("click", function () {
  let reportData = {
    url: activeTabUrl,
    reason: document.getElementById("reason").value,
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
      document.getElementById("reason").value = "";
      document.getElementById("submitReport").innerText = `${data.result}`;
      let submitButton = document.getElementById("submitReport");
      submitButton.disabled = true;
    })
    .catch((error) => console.log(error));
});

// Get the checkbox element
let checkbox = document.getElementById("toggleCheckBox");

// Load the checkbox state from localStorage
let checkboxState = localStorage.getItem("checkboxState");

// If the checkbox state is "checked", check the checkbox
if (checkboxState === "checked") {
  checkbox.checked = true;
}

// Add an event listener for the change event
checkbox.addEventListener("change", function () {
  // If the checkbox is checked, store the state as "checked"
  if (checkbox.checked) {
    localStorage.setItem("checkboxState", "checked");
  }
  // If the checkbox is not checked, store the state as "unchecked"
  else {
    localStorage.setItem("checkboxState", "unchecked");
  }
  chrome.runtime.sendMessage({ checkboxState: checkboxState });
});
