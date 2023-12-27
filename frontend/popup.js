const server_url = "http://localhost:8000/";
let details_url = "";

chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
  let activeTab = tabs[0];
  let activeTabUrl = activeTab.url;
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
      //   document.getElementById(
      //     "detail-5"
      //   ).innerText = `Expiration Date: ${data.expiration_date}`;
      //   document.getElementById(
      //     "detail-6"
      //   ).innerText = `Last Updated: ${data.last_updated}`;
      //   document.getElementById("detail-7").innerText = `DNSSEC: ${data.dnssec}`;
      //   document.getElementById(
      //     "detail-8"
      //   ).innerText = `Registrant: ${data.registrant}`;
      //   document.getElementById("detail-9").innerText = `Emails: ${data.emails}`;
      //   document.getElementById(
      //     "detail-10"
      //   ).innerText = `Country Name: ${data.country_name}`;
    })
    .catch((error) => console.error(error));
});
