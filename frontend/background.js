let activeTabUrl = "";
let phishing;

chrome.tabs.onActivated.addListener(async () => {
  // returns active tab's url
  chrome.tabs.query({ highlighted: true }, async (tabs) => {
    let activeTab = tabs[0];
    activeTabUrl = activeTab.url;
    console.log(activeTabUrl);
    const server_url = "http://localhost:8000/";

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
      chrome.tabs.update(tabId, { url: '../forOverride/override.html' });
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
    console.log(review);
  }
});
