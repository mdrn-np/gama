let activeTabUrl = "";

chrome.tabs.onActivated.addListener(() => {
  // returns active tab's url
  chrome.tabs.query({ highlighted: true }, (tabs) => {
    let activeTab = tabs[0];
    activeTabUrl = activeTab.url;
    console.log(activeTabUrl);
    const server_url = "http://localhost:8000/";

    async function checkPhishing(url) {
      try {
        const response = await fetch(url);
        const data = await response.json();
        console.log(data);
      } catch (error) {
        console.error(error);
      }
    }
    let phishing_url = `${server_url}phishing?url=${activeTabUrl}`;
    let phishing = checkPhishing(phishing_url);
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
