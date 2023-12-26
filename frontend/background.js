chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
  // returns active tab only
  let activeTab = tabs[0];
  let activeTabUrl = activeTab.url
  console.log(activeTabUrl)
});

chrome.runtime.onInstalled.addListener(() => {
  // adds context menu needed for our extension on installation
  chrome.contextMenus.create({
    "id": "validate",
    "title": "validate",
    "contexts": ["selection"]
  })
  console.log('test')
})

chrome.contextMenus.onClicked.addListener((clickData) => {
  // extracts the selected / highlighted value
  if (clickData.menuItemId == "validate" && clickData.selectionText) {
    let review = clickData.selectionText;
    console.log(review)
  }
})
