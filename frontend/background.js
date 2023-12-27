const server_url = "http://localhost:8000/";
let activeTabUrl = "";

chrome.tabs.onUpdated.addListener(async () => {
  // returns active tab's url
  chrome.tabs.query({ highlighted: true }, async (tabs) => {
    let activeTab = tabs[0];
    activeTabUrl = activeTab.url;
    console.log(activeTabUrl);

    async function checkPhishing(url) {
      try {
        const response = await fetch(url);
        const data = await response.json();
        return data;
      } catch (error) {
        console.log(error);
        return false;
      }
    }
    let phishing_url = `${server_url}phishing?url=${activeTabUrl}`;
    phishing = await checkPhishing(phishing_url);

    if (phishing) {
      chrome.tabs.update({ url: "override.html" });
    }
    console.log(phishing);
  });
});

chrome.runtime.onInstalled.addListener(() => {
  // adds context menu needed for our extension on installation
  chrome.contextMenus.create({
    id: "validate",
    title: "validate",
    contexts: ["selection"],
  });
  console.log("test");
});

chrome.contextMenus.onClicked.addListener((clickData) => {
  // extracts the selected / highlighted value
  if (clickData.menuItemId == "validate" && clickData.selectionText) {
    let review = clickData.selectionText;
    const review_url = `${server_url}review`;

    let reviewData = {
      review: review,
    };

    fetch(review_url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(reviewData),
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.result);
      })
      .catch((error) => console.error(error));
    console.log(review);
  }
});
