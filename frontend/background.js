chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
  // returns active tab only
  let activeTab = tabs[0];
  let activeTabUrl = activeTab.url
  console.log(activeTabUrl)
});