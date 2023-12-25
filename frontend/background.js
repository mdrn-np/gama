chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
  // returns active tab only
  let activeTab = tabs[0];
  let activeTabUrl = activeTab.url
  console.log(activeTabUrl)
});

let contextMenuItem = {
  "id": "validate",
  "title": "validate",
  "contexts": ["selection"]
}

chrome.contextMenus.create(contextMenuItem)